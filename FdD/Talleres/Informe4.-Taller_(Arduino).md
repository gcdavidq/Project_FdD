<p align="center" style="margin-top: 50px; margin-bottom: 50px; font-family: Arial, sans-serif;">
  <h1 align="center" style="margin-top: 60px; margin-bottom: 1500px; font-size: 50px;">Facultad de Ciencias e Ingeniería</h1>
  <p align="center">
    <img src="https://3.files.edl.io/fdf6/22/05/20/143302-79bed48a-5422-4ab4-81ec-98e0f944c4a0.png" width="300" alt="Facultad de Ciencias e Ingeniería logo">
  </p>  
</p>

## INFORME DE LABORATORIO N.º 04: USO DE ARDUINO NANO 33 IOT



#### **DOCENTES:**

- UMBERT LEWIS DE LA CRUZ RODRIGUEZ
- MOISES STEVEND MEZA RODRIGUEZ
- HARRY ANDERSON RIVERA TITO
- PAULO CAMILO ALBERTO VELA ANTON
- RENZO JOSE CHAN RIOS
- JUAN MANUEL ZUÑIGA MAMANI

    **LIMA - PERÚ**
        **2024**

## **1. INTRODUCCIÓN:**

En el presente informe de laboratorio, se dará a conocer acerca de lo que se desarrolló en la sesión N° 04 del día 24/01/2024, en donde nos introducimos al uso de Arduino nano 33 IoT, con ayuda de otros componentes como la Arduino MKR Wifi 1010, la cual es una placa microcontroladora con un chip que permite realizar conexiones inalámbricas a otras placas u ordenadores a través del bluetooth y wifi, la MKR IoT Carrier que es una extensión de la placa Arduino MKR Wifi 1010, esta placa no dispone de un microcontrolador, es por ello que solo funciona siempre y cuando una placa Arduino MKR esté conectada a ella, asimismo, contiene todos los circuitos y sensores ya integrados, permitiendo que nos concentremos mejor en la programación y el Cable Micro USB el cual permitirá conectar a la MKR IoT Carrier al ordenador o laptop (1).

Durante la sesión se realizaron con ayuda de los componentes antes descritos ciertas actividades que nos permitieron completar los objetivos propuestos, como por ejemplo, registrar la temperatura y la humedad localmente, mostrar la temperatura local en sus 3 escalas (Fahrenheit (°F), Celsius (°C), y Kelvin (K)), encender las luces leds de color verde cada vez que una persona se acerque, esto con ayuda de un sensor de movimiento y por último encender de color azul una de las luces leds cuando el dispositivo esté en un lugar frío y de color rojo cuando esté en un lugar caliente. A continuación, dichas actividades pasan a ser más detalladas.

<p align="center" style="margin-top: 50px; margin-bottom: 50px; font-family: Arial, sans-serif;">
<i>Figura 1.</i> Arduino MKR WiFi 1010. Elaboración propia.
</p>

<p align="center" style="margin-top: 50px; margin-bottom: 50px; font-family: Arial, sans-serif;">
_Figura 1._   Arduino MKR WiFi 1010. Elaboración propia.
</p>

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/a11.-sensores.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 2.*** MKR IoT Carrier. Elaboración propia.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/a12.-código.jpeg" alt="imagen del grupo" width="400px"/>
</p>



***Figura 3.*** Conexión de la MKR IoT Carrier a la laptop. Elaboración propia.


### 1. REGISTRO DE LA TEMPERATURA Y LA HUMEDAD LOCAL. 

Como primer ejercicio, se nos pidió seguir los pasos que se presentan en la guía del Explore IoT Kit. Para ello, a continuación enumeramos los componentes utilizados tanto en este como en los siguientes ejercicios, los cuales ya fueron descritos anteriormente, pero si quisieran conocer más información acerca de estos componentes pueden ingresar a la página citada en la referencia N° 1. 

1. Arduino MKR WiFi 1010

2. MKR IoT Carrier

3. Cable Micro USB


En cuanto al montaje de estos componentes, lo único que se necesitó fue colocar la placa Arduino MKR WiFi 1010 sobre la MKR IoT Carrier y conectarlo a nuestro ordenador para que funcione. 

Por otro lado, también se necesitó iniciar sesión en Arduino Cloud e instalar el complemento Arduino Web Editor.

Con todos estos pasos realizados, la primera actividad consistía en emplear dos sensores particulares: El de temperatura y humedad, y en base a ellos recopilar datos y mostrarlos en la pantalla.  


Para que se puedan leer los valores de los sensores mencionados, es necesario incluir en nuestras líneas de código la biblioteca llamada.

Arduino_MKRIoTCarrier

**Codigo empleado:**

// Se inicia con la agregación de biblioteca Arduino_MKRIoTCarrier.h, que proporciona las funciones necesarias para interactuar con el módulo IoT Carrier y otros periféricos:
```cpp
#include <Arduino_MKRIoTCarrier.h>
```
// Se declara un objeto carrier de la clase MKRIoTCarrier, que se utilizará para interactuar con el módulo IoT Carrier. También se declaran variables globales para almacenar los valores de temperatura (temperature) y humedad (humidity). Dichos valores serán del tipo float

```cpp
MKRIoTCarrier carrier;
float temperature = 0;
float humidity = 0;
```
 // En la funcion setup, se inicia la comunicación con una velocidad de 9600, se configura la variable CARRIER_CASE (que hace referencia a si está colocada la carcasa de plastico del carrier) por lo que colocamos que sí (True)
```cpp
void setup() {
  Serial.begin(9600);
  CARRIER_CASE = true;
  carrier.begin();
}
```
// En la función Loop, se empieza leyendo los valores de temperatura y humedad del sensor mediante los metodos de readTemperature(). Luego, se actualizan los botones tactiles mediante el metodo de update. Continuando con el codigo, los valores de la temperatura y humedad se imprimen en el monitor de manera serial, cada uno acompañado de caracteres tipo string. Por ultimo, si se detecta el boton TOUCH0 o TOUCH1, se llaman a las funciones de Temperatura y Humedad respectivamente. 

```cpp
void loop() {
  temperature = carrier.Env.readTemperature();
  humidity = carrier.Env.readHumidity();
 
  carrier.Buttons.update();
 
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println("  °C");
 
  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");
 
  if (carrier.Buttons.onTouchDown(TOUCH0)) {
    printTemperature();
  }
 
  if (carrier.Buttons.onTouchDown(TOUCH1)) {
    printHumidity();
  }
}
```

// Estas dos ultimas funciones están diseñadas para configurar la pantalla conectada al modulo Carrier y mostrar los valores de temperatura o humedad (de acuerdo a como se seleccione con los TOUCH´s ya mencionados), variando en el texto así como en el tamaño y color de este.

```cpp
void printTemperature() {


  carrier.display.fillScreen(ST77XX_RED); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(6); //large sized text
 
  carrier.display.setCursor(30, 50); //sets position for printing (x and y)
  carrier.display.print("Temp: ");
  carrier.display.setTextSize(4); //decreasing text size
  carrier.display.setCursor(40, 120); //sets new position for printing (x and y)
  carrier.display.print(temperature);
  carrier.display.print(" C");
}
 
void printHumidity() {


  carrier.display.fillScreen(ST77XX_BLUE); //red background
  carrier.display.setTextColor(ST77XX_WHITE); //white text
  carrier.display.setTextSize(2); //medium sized text
 
  carrier.display.setCursor(20, 110); //sets position for printing (x and y)
  carrier.display.print("Humi: ");
  carrier.display.print(humidity);
  carrier.display.println(" %");
}
```


Evidencia del resultado:

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/b2.-humedad.jpeg" width="300px"/>
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/b21.-temperatura.jpeg" width="300px"/>
</div>

***Figura 4:*** Visualización de la humedad del ambiente en el display. Elaboración propia. | ***Figura 5:*** Visualización de la temperatura del ambiente en el display. Elaboración propia.

###  2. TEMPERATURA LOCAL EN SUS 3 ESCALAS (CELSIUS (°C) FAHRENHEIT (°F) Y KELVIN (K)).

Como segundo ejercicio, se nos encargó el desafío de escribir líneas de código de tal manera que al presionar el TOUCH (Boton que mostraba en la pantalla la temperatura) se muestre la temperatura en grados Celsius, pero si se lo volvía a tocar una vez más, esta cambiaba a escala Fahrenheit, y si se lo tocaba por tercera vez se cambia a escala Kelvin. Esto quiere decir que solo se cambiaron porciones de código, que se explicarán más adelante junto con este a manera de comentarios.

Codigo usado:

```cpp
// Bibliotecas importadas y empleadas:
#include <Adafruit_EEPROM_I2C.h>
#include <Adafruit_FRAM_I2C.h>
#include <Adafruit_GFX.h>
#include <Adafruit_GrayOLED.h>
#include <Adafruit_SPITFT.h>
#include <Adafruit_SPITFT_Macros.h>
#include <gfxfont.h>
#include <AirQualityClass.h>
#include <Arduino_MKRIoTCarrier.h>
#include <Arduino_MKRIoTCarrier_Buzzer.h>
#include <Arduino_MKRIoTCarrier_Qtouch.h>
#include <Arduino_MKRIoTCarrier_Relay.h>
#include <EnvClass.h>
#include <IMUClass.h>
#include <MKRIoTCarrierDefines.h>
#include <PressureClass.h>
```

//Declaracion de variables globales para almacenar los valores de temperatura y humedad, ademas, se han agregado variables booleanas que permitiran gestionar la unidad de temperatura actual.

```cpp
MKRIoTCarrier carrier;

float temperature = 0;
float humidity = 0;
bool celsius = true;  // Variable para almacenar la unidad actual de temperatura
bool kelvin = false;  // Variable para almacenar si se muestra la temperatura en Kelvin
```

//Aparte de lo explicado en el primer ejercicio, se ha agregado un delay para abrir el setup y ver detalles de errores si existieran:

```cpp
void setup() {
  Serial.begin(9600);
  delay(1500);  
  CARRIER_CASE = true;
  carrier.begin();
}

void loop() {
  temperature = carrier.Env.readTemperature();
  humidity = carrier.Env.readHumidity();
  carrier.Buttons.update();
 
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println("  °C");
 
  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");

  if (carrier.Button0.onTouchDown()) {
    toggleTemperatureUnit(); // Cambia la unidad de temperatura al tocar el botón 0
    printTemperature();
  }

  if (carrier.Button1.onTouchDown()) {
    printHumidity();
  }
}
```

//Se implementó una nueva función que permitirá cambiar entre las unidades de temperatura ya mencionadas. Si estaba en Celsius, cambia a Fahrenheit y activa Kelvin; si estaba en Fahrenheit o Kelvin, cambia a Celsius y desactiva Kelvin.

```cpp
void toggleTemperatureUnit() {
  // Cambia entre Celsius, Fahrenheit y Kelvin
  if (celsius) {
    celsius = false;  // Cambia a Fahrenheit
    kelvin = true;    // Activa Kelvin
  } else {
    celsius = true;   // Cambia a Celsius
    kelvin = false;   // Desactiva Kelvin
  }
}

void printTemperature() {
  carrier.display.fillScreen(ST77XX_RED); // Fondo rojo
  carrier.display.setTextColor(ST77XX_WHITE); // Texto blanco
  carrier.display.setTextSize(6); // Tamaño de texto grande
 
  carrier.display.setCursor(30, 50);
  carrier.display.print("Temp: ");
```

 // En la variable printTemperature se han agregado nuevas condicionales, las cuales dependiendo de la temperatura seleccionada se imprimirán en la pantalla, en este punto se realizan las respectivas conversiones de unidades:
 
 ```cpp
  if (celsius) {
    carrier.display.setTextSize(4);
    carrier.display.setCursor(40, 120);
    carrier.display.print(temperature);
    carrier.display.print(" C");
  } else if (kelvin) {
    carrier.display.setTextSize(4);
    carrier.display.setCursor(40, 120);
    carrier.display.print(temperature + 273.15);  // Convierte a Kelvin
    carrier.display.print(" K");
  } else {
    float tempConverted = (celsius) ? temperature : temperature * 9 / 5 + 32;
    carrier.display.setTextSize(4);
    carrier.display.setCursor(40, 120);
    carrier.display.print(tempConverted);
    carrier.display.print(" F");
  }
}

void printHumidity() {
  carrier.display.fillScreen(ST77XX_BLUE); // Fondo azul
  carrier.display.setTextColor(ST77XX_WHITE); // Texto blanco
  carrier.display.setTextSize(2); // Tamaño de texto mediano
 
  carrier.display.setCursor(20, 110);
  carrier.display.print("Humidity: ");
  carrier.display.print(humidity);
  carrier.display.print(" %");
}
```
 

Evidencias del resultado:

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/c3.-temperatura_F.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 6:***  Temperatura del ambiente en grados Fahrenheit. Elaboración propia.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/c31.-temperatura_celsius.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 7:***  Temperatura del ambiente en grados Celsius. Elaboración propia.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/c32.-temperatura_kelvin.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 8:***  Temperatura del ambiente en grados Kelvin. Elaboración propia.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/c33.-código.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 9:***  Imagen de la ejecución del código en el editor online de arduino. Elaboración propia. 


### 3.  ENCENDIDO DE LAS LEDS DEL OPLA iOT, POR DETECCIÓN DE MOVIMIENTO MEDIANTE EL SENSOR PIR

Lamentablemente este ejercicio no pudimos ejecutar, el ejercicio se tenía que realizar con la Opla Iot junto con el sensor pir(sensor de movimiento), la Opla contiene  5 leds alrededor de la pantalla LCD, los cuales tenían que encenderse al momento de que el sensor pir captará movimiento, todos los 5 leds debían encenderse de verde y apagarse cuando no detectaron nada en su rango de alcance de 3 a 7 metros.  

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab3/d.-4_luces_led.jpeg" alt="imagen del grupo" width="400px"/>
</p>

***Figura 10:*** Representación de los 5 leds alrededor de la pantalla LCD . Elaboración propia.



### 4. CAMBIO DE COLOR DE ACUERDO A  LA TEMPERATURA REGISTRADA

En este ejercicio lo que se pedía era tomar una temperatura inicial y de acuerdo a eso establecer un código que nos permita comparar las temperaturas con umbrales predefinidos, es decir, si se detecta una temperatura mayor a 28 °C se prenderá la luz de color rojo que hace referencia al exceso de calor de lo contrario si es una temperatura menor a 28 °C se prenderá la luz de color azul que hace referencia al frío.

**CÓDIGO REALIZADO:**

```cpp
include <Arduino_MKRIoTCarrier.h>
MKRIoTCarrier carrier;


float temperature = 0;
float humidity = 0;


void setup() {
  Serial.begin(9600);
  delay(1500);
  CARRIER_CASE = true;
  carrier.begin();
}


void loop() {
  // leer los valores del sensor
  temperature = carrier.Env.readTemperature();
  humidity = carrier.Env.readHumidity();


  // actualizar los botones táctiles
  carrier.Buttons.update();


  // imprimir cada uno de los valores del sensor
  Serial.print("Temperature = ");
  Serial.print(temperature);
  Serial.println(" °C");


  Serial.print("Humidity = ");
  Serial.print(humidity);
  Serial.println(" %");


  // función para imprimir los valores
  if (carrier.Button0.onTouchDown()) {
    printTemperature();
  }


  if (carrier.Button1.onTouchDown()) {
    printHumidity();
  }


  // Cambiar el color del display basado en la temperatura
  if (temperature > 28.0) {
    carrier.display.fillScreen(ST77XX_RED); // fondo rojo
    carrier.display.setTextColor(ST77XX_WHITE);
  } else {
    carrier.display.fillScreen(ST77XX_BLUE); // fondo azul
    carrier.display.setTextColor(ST77XX_WHITE);
  }
}


void printTemperature() {
  // configurar el display, tamaño de texto y posición
  carrier.display.setTextSize(6);
  carrier.display.setCursor(30, 50);
  carrier.display.print("Temp: ");
 
  carrier.display.setTextSize(4);
  carrier.display.setCursor(40, 120);
  carrier.display.print(temperature);
  carrier.display.print(" C");
}


void printHumidity() {
  // configurar el display, tamaño de texto y posición
  carrier.display.setTextSize(2);
  carrier.display.setCursor(20, 110);
  carrier.display.print("Humi: ");
  carrier.display.print(humidity);
  carrier.display.println(" %");
}
```

Este código debe  activar una serie de efectos visuales y sonoros en respuesta a una temperatura inferior a 28 grados Celsius. Configura ciertos píxeles de una tira de LEDs en rojo, emite un tono y muestra la temperatura en una pantalla junto con un mensaje indicando que hace calor.

***Nota:*** No tenemos las evidencias correspondientes a este ejercicio porque tuvimos un error en el código y no pudimos llegar a la salida deseada.



### 5. COMENTARIOS

En la actividad, hemos explorado los dos elementos centrales de nuestro conjunto: la placa Arduino MKR WiFi 1010 y la MKR IoT Carrier. Además, hemos realizado pruebas para familiarizarnos con algunas de sus funciones, como la lectura de temperatura y humedad, la utilización de la pantalla de la portadora, y finalmente, hemos adquirido conocimientos sobre cómo emplear los botones capacitivos de la MKR IoT Carrier.

1. Integración de sensores: Al combinar sensores como el HTS221 con actuadores como luces LED en Arduino, se logra la creación de sistemas simples pero eficaces para responder a condiciones ambientales específicas.
 
2. Programación Lógica: La programación lógica basada en umbrales facilita la toma de decisiones para activar o desactivar dispositivos en respuesta a cambios en las variables medidas, como la temperatura y la humedad, en este caso.

3. Adaptabilidad y Personalización: La modularidad y flexibilidad de Arduino permiten ajustar fácilmente el código a diferentes situaciones, posibilitando la personalización del sistema según los requisitos específicos del usuario.


### REFERENCIAS BIBLIOGRÁFICAS:

1. Explore IoT Kit. [citado 24 de enero de 2024]. Disponible en: https://explore-iot.arduino.cc/iotsk/module/iot-starter-kit/lesson/internet-of-things

2.	Sensor de Movimiento PIR HC-SR501. Edu.co. [citado el 25 de enero de 2024]. Disponible en: https://www.unipamplona.edu.co/unipamplona/portalIG/home_74/recursos/visual-basic-para-excel/17052017/u5_movimiento.jsp
