/*
 * Bibliotecas
 */

//Bibliotecas Conexão Wi-fi
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

//Conversão para jason
#include <ArduinoJson.h>

#define SERIAL_DEBUG
#define TLS_DEBUG

/*
 * Variáveis globais
 */

//valores para retirar
const char* ssid_default = "Raspberry-AP";  // wifi ssid Open Network
const char* password_default = "qwerty1234";  // wifi password Network
//const char* ssid = "MEO-37E7A0";                   // wifi ssid
//const char* password =  "0b5240c704";         // wifi password

//Pass e Wi-Fi do rasp
char ssid[30];          // wifi ssid
char pass[30];          // wifi password

//Dados do mqtt
const char* mqttServer_default = "10.3.141.1";    // IP adress Raspberry Pi
const int   mqttPort_defaut = 1883;
const char* mqttServer = "192.168.1.80";    // IP adress Raspberry Pi
const int   mqttPort = 8883;
const char* mqttUser = "username";      // if you don't have MQTT Username, no need input
const char* mqttPassword = "12345678";  // if you don't have MQTT Password, no need input
char payload_res[4];
int f1 = 0;
int flag = 0;
char trash;
int aux = 0;

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


/* Other globals */
X509List caCertX509(caCert);        /* X.509 parsed CA Cert */
WiFiClient espClient;
//WiFiClientSecure espClient;         /* Secure client connection class, as opposed to WiFiClient */
PubSubClient client(espClient);
PubSubClient mqttClient(espClient); /* MQTT Client connection */
String clientId = "ESP8266Client-"; /* MQTT client ID (will add random hex suffix during setup) */

/*
 * Setup inicial
 */

void setup() {
  // put your setup code here, to run once:
  //iniciar a Serial Monitor
  Serial.begin(115200);

}

/*
 * Callback
 */
 void desafio(char* topic, byte* payload, unsigned int length) {

    
  if(strcmp(topic,"Challenge") == 0){
    
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message:");
    int k = 3;
    for (int i = 0; i < length; i++) {
      //Serial.print((char)payload[i]);
      payload_res[k] = (char)payload[i];
      Serial.print(payload_res[k]);
      //Serial.print("Ola");
      k--;
    }
    k = 3;
    Serial.println();
    Serial.println("-----------------------");
    
  }
  
  if(strcmp(topic,"rede") == 0){
    Serial.print("Message arrived in topic: ");
    Serial.println(topic);
    Serial.print("Message:");
    flag = 0;
    int j = 0;
    for (int i = 0; i < length; i++) {
      //Serial.print((char)payload[i]);
      if(payload[i] == ','){
        flag = 1;
        j = 0;
        }
      if(flag == 0){
        if(payload[i] == '[' || payload[i] == ']' || payload[i] == ',' || payload[i] == '"'){
        trash = (char)payload[i]; 
        }
        else{
          ssid[j] = (char)payload[i];
          j++;
        }
        }
      if(flag == 1){
         if(payload[i] == '[' || payload[i] == ']' || payload[i] == ',' || payload[i] == '"'){
          trash = (char)payload[i];
        }
        else{
          pass[j] = (char)payload[i];
          j++;
        }
        }    
    }

    Serial.println(ssid);
    Serial.println(pass);
    Serial.println();
    Serial.println("-----------------------");
    aux = 1;
    //Serial.println(aux);
    //Serial.println("AUX");
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
  //Definido pelo utilizador
  int tamost = 1000; 
  
  /*
   * Ligar á rede da rasp
   */
  //if(getEEPROMUInt8(CFG_NET_CON) != 1){
    if(f1 == 0){
      //ligar a rede levantada pela Rasp
      //WiFi.persistent(false);
      WiFi.mode(WIFI_STA);    
      WiFi.begin(ssid_default, password_default); 
      //WiFi.begin("Raspberry-AP", "qwerty1234");
      
      //Verificação da ligação
      while(WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.println("Connecting to Open WiFi..");
      }
  
      //Serial.println("AHAHAHAHAHHA");

    
    if(WiFi.status() == WL_CONNECTED)
    {

      //Configure MQTT Broker settings 
      mqttClient.setServer("10.3.141.1",1883);
      mqttClient.setCallback(desafio);
      //mqttClient.setCallback(subCallback);
    
      //conexão ao mqtt
      while (!mqttClient.connected()) {
        Serial.println("Connecting to MQTT Open...");
        if (mqttClient.connect("ESP8266Client", mqttUser, mqttPassword )) {
          Serial.println("connected");
        } else {
          Serial.print("failed with state ");
          Serial.print(mqttClient.state());
          delay(2000);
        }
      }
      f1 = 1;  
      
  }
 }

    //Desafio
    mqttClient.setCallback(desafio);
    while(mqttClient.subscribe("Challenge") != true);
    while(mqttClient.publish("ResponseChallenge",payload_res) != true);
    //Receber o nome e a passe da net
    while(mqttClient.subscribe("rede") != true);
    mqttClient.loop();

    if(aux == 1){
      //Serial.println("1");
      mqttClient.disconnect();
      //Serial.println("1");
      WiFi.disconnect();
      //WiFi.persistent(false);
      WiFi.mode(WIFI_STA);
      //Serial.println("1");
      WiFi.begin(ssid,pass);
      //Serial.println("1");
      while(WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.println("Connecting to New WiFi..");
      }
      if(WiFi.status() == WL_CONNECTED){
        Serial.println("Connected to the WiFi network");
      }
    }

  delay(tamost);
  
}

    
