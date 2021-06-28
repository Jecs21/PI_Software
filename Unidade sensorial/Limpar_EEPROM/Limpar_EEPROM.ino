//EEPROM
#include <EEPROM.h>

//ler o uint8_t guardado
uint8_t getEEPROMUInt8(byte offset) {
  return EEPROM.read(offset);
}
//guardar o valor na memória 
void setEEPROMUInt8(byte offset, uint8_t v) {
  //v de 0 a 55;
  EEPROM.write(offset, v);
}

// Local de armazenamento na EEPROM
const byte CFG_NET = 40;
const byte CFG_Active = 42; //uint8_t
const byte CFG_NET_CON = 43;

void setup() {
  //Inicialização da ERPROM
  EEPROM.begin(CFG_NET + 1); //incerteza se leva mais um ou não
  // put your setup code here, to run once:
  setEEPROMUInt8(CFG_Active, 0);
  setEEPROMUInt8(CFG_NET_CON, 0);
  setEEPROMUInt8(CFG_NET, 0);
  EEPROM.commit();
}

void loop() {
  // put your main code here, to run repeatedly:

}
