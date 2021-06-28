/*
 * Bibliotecas
 */
 
//Bibliotecas Sensor
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"

//Bibliotecas Conexão Wi-fi e MQTT
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//bibliotecas Display
#include <GxEPD.h>
#include <GxGDEW027W3/GxGDEW027W3.h> 

#include GxEPD_BitmapExamples

//Tamanhos da letra do ecrã
#include <Fonts/FreeMonoBold9pt7b.h>
#include <Fonts/FreeMonoBold12pt7b.h>
#include <Fonts/FreeMonoBold18pt7b.h>
#include <Fonts/FreeMonoBold24pt7b.h>

#include <GxIO/GxIO_SPI/GxIO_SPI.h>
#include <GxIO/GxIO.h>

//Imagens a apresentar
#include "wi_fi.h"
#include "no_wi_fi.h"

#define SEALEVELPRESSURE_HPA (1013.25)

//EEPROM
#include <EEPROM.h>

Adafruit_BME680 bme; // I2C
//Debugs
#define ESP8266_LED (5)
#define RELAY_SIGNAL_PIN (4)
#define SERIAL_DEBUG
#define TLS_DEBUG

/*
 * Variáveis globais
 */

GxIO_Class io(SPI, /*CS=D8*/ SS, /*DC=D3*/ 0, /*RST=D4*/ 5); // arbitrary selection of D3(=0), D4(=2), selected for default of GxEPD_Class
GxEPD_Class display(io, /*RST=D4*/ 5, /*BUSY=D2*/ 4); // default selection of D4(=2), D2(=4)

//valores para retirar
const char* ssid = "MEO-37E7A0";                   // wifi ssid
const char* password =  "0b5240c704";         // wifi password

//Dados do mqtt
const char* mqttServer = "192.168.1.80";    // IP adress Raspberry Pi
const int   mqttPort = 8883;
const char* mqttUser = "username";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "12345678";  // if you don't have MQTT Password, no need input

//Define a estrutura da EEPROM - (meter o ssid e a password como String)
//Estamos a definir o offset onde é colocado cada variável
const byte CFG_ssid = 0;
const byte CFG_password = 20;
const byte CFG_NET = 40;
const byte CFG_Active = 42; //uint8_t
const byte CFG_NET_CON = 43;

/* Certificate Authority info */
/* CA Cert in PEM format */
const char caCert[] PROGMEM = R"EOF(
-----BEGIN CERTIFICATE-----
MIICIDCCAYICFClZHbZmqwJGLM6d3EonMEgsWF1oMAoGCCqGSM49BAMCME8xCzAJ
BgNVBAYTAlBUMQswCQYDVQQIDAJQVDEPMA0GA1UEBwwGQXZlaXJvMQswCQYDVQQL
DAJHNTEVMBMGA1UEAwwMMTkyLjE2OC4xLjgwMB4XDTIxMDUyNzE0MzcwOVoXDTMx
MDUyNTE0MzcwOVowTzELMAkGA1UEBhMCUFQxCzAJBgNVBAgMAlBUMQ8wDQYDVQQH
DAZBdmVpcm8xCzAJBgNVBAsMAkc1MRUwEwYDVQQDDAwxOTIuMTY4LjEuODAwgZsw
EAYHKoZIzj0CAQYFK4EEACMDgYYABAFNzbhJ7X+qVQm3hUnk2hV/+aaWTYqDyPcQ
8zJN+8V1o+1FtoDqJAFL2JTV8YPIZt4e0CeLJomlClMAOLncQFyKVQGDwRnzEBUa
XNX0El8rgQ/lVbQh7HBNIzCuqLxKfkSHYYgaIdmIdEZ6rn263Kzrm4hJ2XuNrHUN
c7+IUKHhqPnNrDAKBggqhkjOPQQDAgOBiwAwgYcCQU/7ARF3LB+L58Ntx3JC4ur4
1t0DzK5ibxKq0jhrXBETNaZFfIbs6OyG7LzAL8zmEH+j/uMbGKhDznOoiSplzHXP
AkIBQOeRN4FrWmh37OkxAjBeDk2KVSw0HvDBqCc16LdYjg1nx+22p2kCIqckg7nu
mWEp0xVajm/aled9gBaOEXjZVo4=
-----END CERTIFICATE-----
)EOF";

/* MQTT broker cert SHA1 fingerprint, used to validate connection to right server */
const uint8_t mqttCertFingerprint[] = {0x13,0xC8,0xD7,0x9E,0x8A,0x3A,0xF8,0x4E,0x01,0xC0,0x66,0x05,0x2E,0xB0,0x95,0x97,0x8E,0xA8,0xC3,0x67};

/*
 * Funções
 */
 
//ler o uint8_t guardado
uint8_t getEEPROMUInt8(byte offset) {
  return EEPROM.read(offset);
}
//guardar o valor na memória 
void setEEPROMUInt8(byte offset, uint8_t v) {
  //v de 0 a 55;
  EEPROM.write(offset, v);
}
String getEEPROMString(byte offset) {
  // Le String da EEPROM
    String s = "";
   while (1) {
    //20 caracteres no máximo
    //a string acaba sempre com 0
    if (EEPROM.read(offset) == 0) {
       break;
     }
     s += char(EEPROM.read(offset));
     offset++;
    }
   return s;
}
 
void setEEPROMString(byte offset, String s) {
  // Grava String na EEPROM
    for (byte b = 0; b <= s.length(); b++) {
      EEPROM.write(offset + b, s[b]);
    }
  }
 
/* Other globals */
X509List caCertX509(caCert);        /* X.509 parsed CA Cert */
WiFiClientSecure espClient;         /* Secure client connection class, as opposed to WiFiClient */
PubSubClient client(espClient);
PubSubClient mqttClient(espClient); /* MQTT Client connection */
String clientId = "ESP8266Client-"; /* MQTT client ID (will add random hex suffix during setup) */

//Debug
#ifdef TLS_DEBUG
/* verifytls()
 *  Test WiFiClientSecure connection using supplied cert and fingerprint
 */
bool verifytls() {
  bool success = false;
    
#ifdef SERIAL_DEBUG
  Serial.print("Verifying TLS connection to ");
  Serial.println("192.168.1.80");
#endif

  success = espClient.connect("192.168.1.80", 8883);

#ifdef SERIAL_DEBUG
  if (success) {
    Serial.println("Connection complete, valid cert, valid fingerprint.");
  }
  else {
    Serial.println("Connection failed!");
  }
#endif

  return (success);
}
#endif

void reconnect() {
  /* Loop until we're reconnected */
  while (!mqttClient.connected()) {
    #ifdef SERIAL_DEBUG
        Serial.print("Attempting MQTT broker connection...");
    #endif
        /* Attempt to connect */
        if (mqttClient.connect(clientId.c_str())) {
          #ifdef SERIAL_DEBUG
            Serial.println("connected");
          #endif
          /* Once connected, resubscribe */
          mqttClient.subscribe("home/recroom/tv/powerstrip/cmd");      
        } 
        else {
          #ifdef SERIAL_DEBUG
            Serial.print("Failed, rc=");
            Serial.print(mqttClient.state());
            Serial.println(". Trying again in 5 seconds...");
          #endif
          /* Wait 5 seconds between retries */
          delay(5000);
        }
    }
}


/*
 * Setup inicial
 */

void setup() {
  // put your setup code here, to run once:
  //iniciar a Serial Monitor
  Serial.begin(115200); 
  
  //iniciar o display
  display.init(115200); 
  // Inicializa EEPROM
  EEPROM.begin(CFG_NET_CON + 1); 

  const GFXfont* f1 = &FreeMonoBold12pt7b;//Define o Tamanho da letra

  //verificação da conecção com o BME680
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME680 sensor, check wiring!");
    while (1);
  }
  
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // 320*C for 150 ms

/*
   * 
   * Segurança
   * 
   */

    /* Set board's GPIO pins as outputs */
  pinMode(RELAY_SIGNAL_PIN, OUTPUT);
  pinMode(ESP8266_LED, OUTPUT);
  Serial.setDebugOutput(true);


  //provável alteração de todos as ligações do wi-fi para o ciclo infinito
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password); //conexão Wi-fi
  
  //Só mostra no dislay caso seja a primeira vez que se conecta
  if(getEEPROMUInt8(CFG_NET) != 1){

    display.setRotation(3);
    display.fillScreen(GxEPD_WHITE);
    display.setTextColor(GxEPD_BLACK);
    display.drawBitmap(220,5,gImage_no_wi_fi, 35,29, GxEPD_BLACK);
    display.setCursor(50, 90);
    display.setFont(f1);
    display.print("CONNECTING");
    display.update();
  }
  //Verificação da ligação
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }

  if(getEEPROMUInt8(CFG_NET) != 1){
    Serial.println("Connected to the WiFi network");
    display.setRotation(3);
    display.fillScreen(GxEPD_WHITE);
    display.setTextColor(GxEPD_BLACK);
    display.drawBitmap(220,5,gImage_wi_fi, 35,25, GxEPD_BLACK);
    display.setCursor(50, 90);
    display.setFont(f1);
    display.print("CONNECTED");
    display.update();
    setEEPROMUInt8(CFG_NET, 1);
    EEPROM.commit(); // è o que guarda os valores no EEPROM
  }

/*
 * Configurar e ligar ao mqtt
 */
  
   /* Configure secure client connection */
  espClient.setTrustAnchors(&caCertX509);         /* Load CA cert into trust store */
  espClient.allowSelfSignedCerts();               /* Enable self-signed cert support */
  espClient.setFingerprint(mqttCertFingerprint);  /* Load SHA1 mqtt cert fingerprint for connection validation */
  #ifdef TLS_DEBUG
  /* Call verifytls to verify connection can be done securely and validated - this is optional but was useful during debug */
  verifytls();
  #endif

  /* Add random hex client ID suffix once during each reboot */
  clientId += String(random(0xffff), HEX); 
  
  while (!mqttClient.connected()) {
    reconnect();
  }
}
/*
 * Callback
 */
void subCallback(char *topic, byte *payload, unsigned int length)
{
  static int pinStatus = LOW;
  DynamicJsonDocument doc(256);
  deserializeJson(doc, (char*)payload);  
  JsonObject root = doc.as<JsonObject>();
  
#ifdef SERIAL_DEBUG  
  serializeJson(root, Serial);
  Serial.println();
#endif

  if(!root["set"].isNull()) {
    if(root["set"] == "toggle") {
      pinStatus = !pinStatus;
    } else if (root["set"] == "on") {
      pinStatus = HIGH;
    } else if (root["set"] == "off") {
      pinStatus = LOW;
    } else {
      return;
    }
    digitalWrite(RELAY_SIGNAL_PIN, pinStatus);
    mqttClient.publish("home/recroom/tv/powerstrip/status", pinStatus == LOW ? "off" : "on");
  } else if(!root["get"].isNull()) {
    if(root["get"] == "status") {
      mqttClient.publish("home/recroom/tv/powerstrip/status", pinStatus == LOW ? "off" : "on");
    }
  }
}


/*
 * Loop 
 * Realiza as medições
 */
 
void loop() {
  // put your main code here, to run repeatedly:
  /*
   * Variáveis
   */
  //Define o Tamanho da letra
  const GFXfont* f = &FreeMonoBold9pt7b;
  const GFXfont* f1 = &FreeMonoBold12pt7b;
  const GFXfont* f2 = &FreeMonoBold18pt7b;
  //Definido pelo utilizador
  int tamost = 1000; 
  int up = 0;

  //Ativação do sensor BME
  if(!bme.performReading()){
    Serial.println("Failed to perform reading :(");
    return;
  }
  
  //Retirar os valores do sensor BME
  float Temp = bme.temperature;
  float Press = bme.pressure / 100;
  float Humid = bme.humidity;
  float Gas = log(bme.gas_resistance) + 0.04*Humid;

  int T = Temp;
  int P = Press;
  int H = Humid;

  float Gas = log(bme.gas_resistance) + 0.04*Humid;
  if(Gas < 0) Gas = 0;
  int G = Gas;
  /*
   * Impressão dos valores
   */
  display.setRotation(3); //display.setRotation(1);
  display.setFont(f); 
  display.fillScreen(GxEPD_WHITE);
  display.setTextColor(GxEPD_BLACK);
  display.drawBitmap(220,5,gImage_wi_fi, 35,25, GxEPD_BLACK);
  display.setCursor(5, 50);
  display.setFont(f);
  display.print("Temperatura:");
  display.setFont(f2);
  display.setCursor(30, 85);
  display.print(T);
  display.setCursor(76, 70);
  display.setFont(f);
  display.print("0");
  display.setCursor(85, 80);
  display.setFont(f1);
  display.print("C");

  display.setCursor(20, 115);
  display.setFont(f);
  display.print("Pressao: ");
  display.setFont(f2);
  display.setCursor(5, 150);
  display.print(P);
  display.setFont(f1);
  display.print("hPa");

  display.setCursor(160, 115);
  display.setFont(f);
  display.print("Gases: ");
  display.setFont(f1);
  if(G <50)
  {
    display.setCursor(140, 150);
    display.print("EXCELENTE");
  }
  if((G<100) && (G >50))
  {
    display.setCursor(165, 150);
    display.print("BOM");
  }
    if((G<150) && (G >100))
  {
    display.setCursor(135, 150);
    display.print("INSUFICIENTE");
  }
  if(G >150)
  {
    display.setCursor(165, 150);
    display.print("MAU");
  }
  display.setFont(f1);
  display.print("");

  display.setCursor(150, 50);
  display.setFont(f);
  display.println("Humidade:");
  display.setFont(f2);
  display.setCursor(165, 85);
  display.print(H);
  display.setFont(f1);
  display.print("%");


  if(getEEPROMUInt8(CFG_Active) == 1){
    //Publish
    String Tp = (String)Temp;
    client.publish("BME_TEMP", Tp.c_str());
    client.subscribe("BME_TEMP");
  
    String Pr = (String)Press;
    client.publish("BME_Press", Pr.c_str());
    client.subscribe("BME_Press");
    
    String Hu = (String)Humid;
    client.publish("BME_Humid", Hu.c_str());
    client.subscribe("BME_Humid");
  
    String V = (String)Gas;
    client.publish("BME_VOC", V.c_str());
    client.subscribe("BME_VOC");
  }
    //Update apenas de alterações do displa
  display.updateWindow(0, 0, GxEPD_WIDTH, GxEPD_HEIGHT,false);
  
  //Sleep Mode
  ESP.deepSleep(tamost*1000 -100);
  delay(tamost);
  mqttClient.loop();
}
