/*
Bibliotecas
*/
#include <GxEPD.h>
#include <GxGDEW027W3/GxGDEW027W3.h>

//Tamanho das letras no display
#include <Fonts/FreeMonoBold9pt7b.h>
#include <Fonts/FreeMonoBold12pt7b.h>
#include <Fonts/FreeMonoBold18pt7b.h>
#include <Fonts/FreeMonoBold24pt7b.h>

#include GxEPD_BitmapExamples

#include <GxIO/GxIO_SPI/GxIO_SPI.h>
#include <GxIO/GxIO.h>

// Include de imagens 
#include "wi_fi.h"
#include "no_wi_fi.h"


GxIO_Class io(SPI, /*CS=D8*/ SS, /*DC=D3*/ 0, /*RST=D4*/ 12); // arbitrary selection of D3(=0), D4(=2), selected for default of GxEPD_Class
GxEPD_Class display(io, /*RST=D4*/ 12, /*BUSY=D2*/ 16); // default selection of D4(=2), D2(=4)

void setup() {
  // put your setup code here, to run once:
  display.init(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  int tamost = 2000; //Definido pelo utilizador
  
  //Valor para teste do display
  int t = 10.04;
  int p = 2030.12;
  int h = 79.95;


  // Estudo da rotação do display 
  /*
  display.setRotation(2);//display.setRotation(0);
  const GFXfont* f = &FreeMonoBold9pt7b;//Define o Tamanho da letra
  const GFXfont* f1 = &FreeMonoBold12pt7b;//Define o Tamanho da letra
  const GFXfont* f2 = &FreeMonoBold18pt7b;//Define o Tamanho da letra
  display.setFont(f); 
  display.fillScreen(GxEPD_WHITE);
  display.setTextColor(GxEPD_BLACK);
  display.drawBitmap(135,5,gImage_wi_fi, 35,25, GxEPD_BLACK);
  display.setCursor(20, 50);
  display.setFont(f);
  display.print("Temperatura:");
  display.setFont(f2);
  display.setCursor(30, 85);
  display.print(t);
  display.setCursor(100, 70);
  display.setFont(f);
  display.print("0");
  display.setCursor(109, 80);
  display.setFont(f1);
  display.print("C");

  display.setCursor(45, 200);
  display.setFont(f);
  display.print("Pressao: ");
  display.setFont(f2);
  display.setCursor(20, 235);
  display.print(p / 100.0);
  display.setFont(f1);
  display.print("hPa");

  display.setCursor(40, 125);
  display.setFont(f);
  display.println("Humidade:");
  display.setFont(f2);
  display.setCursor(60, 160);
  display.print(h);
  display.setFont(f1);
  //int a = readButtons();
  //display.print(a);
  display.print("%");
  */

  //Impressão dos caracteres do display
  //Código Posicao Normal
  display.setRotation(3);//display.setRotation(1);
  const GFXfont* f = &FreeMonoBold9pt7b;//Define o Tamanho da letra
  const GFXfont* f1 = &FreeMonoBold12pt7b;//Define o Tamanho da letra
  const GFXfont* f2 = &FreeMonoBold18pt7b;//Define o Tamanho da letra
  display.setFont(f);  
  display.fillScreen(GxEPD_WHITE);      //Definir cor de fundo
  display.setTextColor(GxEPD_BLACK);    //Definir a cor das letras
  display.drawBitmap(220,5,gImage_wi_fi, 35,25, GxEPD_BLACK); //Imprimir Imagem 
  display.setCursor(5, 50);             //Selecionar o local onde imprimir a imagem 
  display.setFont(f);
  display.print("Temperatura:");
  display.setFont(f2);
  display.setCursor(40, 85);
  display.print(t);
  display.setCursor(80, 70);
  display.setFont(f);
  display.print("0");
  display.setCursor(89, 80);
  display.setFont(f1);
  display.print("C");

  display.setCursor(90, 115);
  display.setFont(f);
  display.print("Pressao: ");
  display.setFont(f2);
  display.setCursor(70, 150);
  display.print(p);
  display.setFont(f1);
  display.print("hPa");

  display.setCursor(150, 50);
  display.setFont(f);
  display.println("Humidade:");
  display.setFont(f2);
  display.setCursor(160, 85);
  display.print(h);
  display.setFont(f1);
  display.print("%");

 
  display.update(); // Atualização do display
  delay(tamost); 
  
}
