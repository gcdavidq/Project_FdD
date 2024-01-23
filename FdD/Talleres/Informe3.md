# Laboratorio N° 03

## Fundamentos de Electrónica I

En el presente informe, se dará a conocer acerca de lo que se desarrolló en la sesión N° 3 del día 22/01/2024, en donde nos introducimos al conocimiento del manejo de protoboar y el circuito divisor de tensión con los cuales se realizaron ciertas actividades que nos permitieron completar los objetivos propuestos para la presente sección que a continuación pasan a ser más detallados.



### 1. Manejo de protoboar 

**1.1 Ejercicio nivel pollito:**

Representación gráfica del circuito real y el circuito reescrito



***Figura 1:*** Ejercicio de Circuito N°1.  Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)

***Figura 2:*** Esquema del circuito de resistencia. Elaboración propia.

**Valores de cada resistencia:**

$R_{\text{1}}$: 10 000 Ω


$R_{\text{2}}$: 10 000 Ω


$R_{\text{3}}$: 220 Ω

***Evidencia del trabajo realizado:***
















***Figura 3:*** Circuito de resistencias en protoboard. Elaboración propia.

En primer lugar, se identificó que las resistencias R1 y R2 están en serie por lo tanto la sumatoria es directa.

$R_{\text{eq}}$ = $R_{\text{1}}$ + $R_{\text{2}}$


$R_{\text{eq}}$ = 10000Ω + 10000Ω


$R_{\text{eq}}$ = 20000Ω


Para la segunda parte, tenemos una suma inversa dado que el circuito es paralelo, a ello se adiciona el resultado de la $R_{\text{eq}}$  para calcular la $R_{\text{T}}$ de la siguiente manera:


$\frac{1}{R_{\text{T}}}$= $\frac{1}{R_{\text{eq}}}$ + $\frac{1}{R_{\text{3}}}$


$\frac{1}{R_{\text{T}}}$= $\frac{1}{20000Ω}$ + $\frac{1}{220Ω}$

$\frac{1}{R_{\text{T}}}$ = 0.00459Ω

$\frac{1}{R_{\text{0.00459Ω}}}$= $R_{\text{T}}$

$R_{\text{T}}$ = 217.9Ω

***Evidencias del resultado obtenido:***


***Figura 4:*** Medición de resistencias con multimetro. Elaboración propia.


**1.2 Ejercicio nivel gato:**



***Figura 5:*** Ejercicio de Circuito N°2. Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)



***Evidencia del trabajo realizado:***


***Figura 6:*** Circuito de resistencias en protoboard. Elaboración propia.

**Valores de cada resistencia:**

$R_{\text{1}}$:10 000Ω

$R_{\text{2}}$:10 000Ω 

$R_{\text{3}}$:10 000Ω 

$R_{\text{4}}$:10 000Ω 

$R_{\text{5}}$:10 000Ω 

Representación gráfica del circuito:

***Figura 7:*** Esquema de circuito de resistencias Parte 1. Elaboración propia.

Primero, sumamos $R_{\text{1}}$ y $R_{\text{2}}$, ambos están en serie.


***Figura 8:*** Esquema de circuito de resistencias Parte 2. Elaboración propia.

$R_{\text{1}}$ + $R_{\text{2}}$ = 10000Ω + 10000Ω

$R_{\text{1}}$+ $R_{\text{2}}$=20000Ω

Luego, sumamos de manera paralela $\frac{1}{R_{\text{3}}}$ + el resultado de ($R_{\text{1}}$ +$R_{\text{2}}$). Recordemos que la suma se hace de manera inversa cuando el circuito es paralelo.

***Figura 9:*** Esquema de circuito de resistencias Parte 3.. Elaboración propia.

$\frac{1}{R_{\text{T}}}$= $\frac{1}{R_{\text{4}}}$ + $\frac{1}{R_{\text{3}}}$ + $\frac{1}{R_{\text{3}}}$ + $\frac{1}{R_{1}+R_{2}}$

1RT= 110000 +110000 +120000 

1RT= 14000  

RT=4000 

Como se podrá apreciar en el circuito resumido de la imagen, por la forma en como la resistencia 5 (R5) está conectada se producirá un cortocircuito, generando así que su valor sea lo suficientemente bajo (casi nulo) para no ser considerado en el circuito.
Evidencias del resultado obtenido: 

***Figura 10:*** Medición de resistencias con multimetro. Elaboración propia.
















1.3 Ejercicio nivel dragón: 











***Figura 11:*** Ejercicio de Circuito N°3. Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)



Evidencia del trabajo realizado:
















***Figura 12:*** Circuito de resistencias en protoboard. Elaboración propia.

Valor de cada resistencia:
R1:10000 
R2:10000 
R3:10000 
R4:10000 
R5:10000 
R6:10000 
Representación gráfica del circuito real y el circuito reescrito:













***Figura 13:*** Circuito de resistencias. Elaboración propia.


***Figura 14:*** Esquema de circuito de resistencias Parte 1. Elaboración propia.

La resistencia R5 y R6 están en serie por lo tanto la sumatoria es directas:

 Req=R5+R6=10000 +10000
Req=20000 



 











***Figura 15:***  Esquema de circuito de resistencias Parte 2. Elaboración propia.    

La resistencia R2 y R4 están en serie por lo tanto la sumatoria es directas:

 Req=R2+R4=10000 +10000
Req=20000 

La resistencia R1 y R3 también están en serie por lo tanto la sumatoria es directas:

 Req=R1+R3=10000 +10000
Req=20000 








***Figura 16:***  Esquema de circuito de resistencias Parte 3. Elaboración propia.   

Finalmente, nos quedan las tres resistencias en paralelo. Para encontrar la resistencia equivalente total, realizamos la suma inversa de todas ellas.

1RT= 1R1-3+1R5-6+1R2-4

1RT= 120000 +120000 +120000 

1RT= 1.5X10-4    

1RT=11.5X10-4   

RT=6666.666     








Una vez realizados los cálculos, pasamos a tomar las medidas con el multímetro para ver si el procedimiento realizado es correcto. 
Como podemos observar en la imagen el resultado tiene relación con lo obtenido experimentalmente.













***Figura 17:*** Medición de resistencias con multimetro. Elaboración propia.   
























 Circuitos útiles

2.1 Circuito Divisor de Tensión: Este circuito nos sirve para obtener un voltaje de salida (Vout) en menor cantidad que el voltaje de entrada (Vint) utilizando la ley de Ohm. Por ejemplo, si queremos alimentar una bombilla a 6 voltios y solo disponemos de una pila de 10 voltios, podemos utilizar un circuito divisor de tensión en donde divida los 10 voltios de la pila en 2, una de 6 voltios (Vout) y otra de 4 voltios (1). 





***Figura 18:*** Fórmula general a utilizar en un circuito divisor de tensión. Fue extraído de “Divisor de tensión”(1). 

Para el presente trabajo se recomendó que el voltaje de entrada y salida sean de 5 voltios y 1.1 voltios respectivamente. Como equipo decidimos que el valor de la resistencia 2 (R2)  sea de 10 000 ohmios (Ω) al realizar las operaciones correspondientes se obtuvo que la resistencia 1 (R1) debería tener un valor de 35 454.54 ohmios (Ω) .


Vout=  R2/(R1+R2)(Vint)=  ( Vout)/((Vint) )=  R2/(R1+R2)  =  1.1/5=  (10 000)/(R1+10 000)
= R1=35 454.5454 Ω






Para comprobar lo calculado tratamos de formar una resistencia de 35 454.55 Ω aproximadamente, es por ello que se usaron 3 resistores en serie  con valores de 20 000, 10 000 y 6 000 Ω, al medir el voltaje de salida de esta nueva conexión se obtuvo como resultado un valor de 1.067 V concluyendo así que este resultado se aproximó al valor propuesto (1.1 V), una de las razones que no permitió llegar al valor propuesto fue por la diferencia de resistencia, ya que de acuerdo a los cálculos debió ser un resistor de 35 454.55 Ω, sin embargo, se utilizó uno de 36 000 Ω. 




***Figura 19:*** Conexión en serie de los 3 resistores para formar uno de 36 000 Ω . Elaboración propia.


***Figura 20:*** Voltaje de salida (Vout) de la nueva conexión. Elaboración propia.




### **REFERENCIA BIBLIOGRÁFICA:**

1. AREATECNOLOGIA. Divisor de tensión. Disponible en: https://www.areatecnologia.com/electronica/divisor-de-tension.html

