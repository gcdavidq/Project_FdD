# Laboratorio N° 03

## Fundamentos de Electrónica I

En el presente informe, se dará a conocer acerca de lo que se desarrolló en la sesión N° 3 del día 22/01/2024, en donde nos introducimos al conocimiento del manejo de protoboard y el circuito divisor de tensión con los cuales se realizaron ciertas actividades que nos permitieron completar los objetivos propuestos para la presente sección que a continuación pasan a ser más detallados.



### 1. Manejo de protoboard 

**1.1 Ejercicio nivel pollito:**

Representación gráfica del circuito real y el circuito reescrito

<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/1.-Circuito%201.jpeg" width="300px"/>
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/2.-Circuito%201_2.jpeg" width="400px"/>
</div>

***Figura 1:*** Ejercicio de Circuito N°1.  Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)

***Figura 2:*** Esquema del circuito de resistencia. Elaboración propia.

**Valores de cada resistencia:**

$R_{\text{1}}$: 10 000 Ω


$R_{\text{2}}$: 10 000 Ω


$R_{\text{3}}$: 220 Ω

**Evidencia del trabajo realizado:**



<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/3.-Circuito%201_3.jpeg" alt="imagen del grupo" width="600px"/>
</p>


***Figura 3:*** Circuito de resistencias en protoboard. Elaboración propia.

En primer lugar, se identificó que las resistencias R1 y R2 están en serie por lo tanto la sumatoria es directa.

$R_{\text{eq}}$ = $R_{\text{1}}$ + $R_{\text{2}}$


$R_{\text{eq}}$ = 10000Ω + 10000Ω


$R_{\text{eq}}$ = 20000Ω


Para la segunda parte, tenemos una suma inversa dado que el circuito es paralelo, a ello se adiciona el resultado de la $R_{\text{eq}}$  para calcular la $R_{\text{T}}$ de la siguiente manera:


$\frac{1}{R_{\text{T}}}$= $\frac{1}{R_{\text{eq}}}$ + $\frac{1}{R_{\text{3}}}$


$\frac{1}{R_{\text{T}}}$= $\frac{1}{20000Ω}$ + $\frac{1}{220Ω}$

$\frac{1}{R_{\text{T}}}$ = 0.00459Ω

$\frac{1}{{\text{0.00459Ω}}}$= $R_{\text{T}}$

$R_{\text{T}}$ = 217.9Ω

**Evidencias del resultado obtenido:**

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/4.-Circuito%201_4.jpeg" alt="imagen del grupo" width="600px"/>
</p>

***Figura 4:*** Medición de resistencias con multimetro. Elaboración propia.

Después de realizar los cálculos, continuamos realizando mediciones con un multímetro para ver si el procedimiento realizado es correcto.

El resultado experimental se correlaciona con el resultado que se muestra en la figura.


**1.2 Ejercicio nivel gato:**

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/5.-Circuito.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 5:*** Ejercicio de Circuito N°2. Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)



**Evidencia del trabajo realizado:**

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/18.-Taller_pregunta_2.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 6:*** Circuito de resistencias en protoboard. Elaboración propia.

**Valores de cada resistencia:**

$R_{\text{1}}$:10 000Ω

$R_{\text{2}}$:10 000Ω 

$R_{\text{3}}$:10 000Ω 

$R_{\text{4}}$:10 000Ω 

$R_{\text{5}}$:10 000Ω 

**Representación gráfica del circuito:**

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/51.-Circuito.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 7:*** Esquema de circuito de resistencias Parte 1. Elaboración propia.

Primero, sumamos $R_{\text{1}}$ y $R_{\text{2}}$, ambos están en serie.

$R_{\text{1}}$ + $R_{\text{2}}$ = 10000Ω + 10000Ω

$R_{\text{1}}$+ $R_{\text{2}}$=20000Ω


<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/6.-Circuito%202_2.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 8:*** Esquema de circuito de resistencias Parte 2. Elaboración propia.


Luego, sumamos de manera paralela $\frac{1}{R_{\text{3}}}$ + el resultado de ($R_{\text{1}}$ + $R_{\text{2}}$). Recordemos que la suma se hace de manera inversa cuando el circuito es paralelo.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/7.-Circuito%202_3.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 9:*** Esquema de circuito de resistencias Parte 3.. Elaboración propia.

$\frac{1}{R_{\text{T}}}$= $\frac{1}{R_{\text{4}}}$ + $\frac{1}{R_{\text{3}}}$ + $\frac{1}{R_{\text{3}}}$ + $\frac{1}{R_{1}+R_{2}}$

$\frac{1}{R_{\text{T}}}$= $\frac{1}{{\text{10000Ω}}}$ + $\frac{1}{{\text{10000Ω}}}$ + $\frac{1}{{\text{20000Ω }}}$ 

$\frac{1}{R_{\text{T}}}$= $\frac{1}{{\text{4000}}}$ 

$R_{\text{T}}$=4000Ω

Como se podrá apreciar en el circuito resumido de la imagen, por la forma en como la resistencia 5 (R5) está conectada se producirá un cortocircuito, generando así que su valor sea lo suficientemente bajo (casi nulo) para no ser considerado en el circuito.
Evidencias del resultado obtenido: 


<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/19.-Taller_pregunta_2_voltimetro.jpeg" alt="imagen del grupo" width="600px"/>
</p>

***Figura 10:*** Medición de resistencias con multimetro. Elaboración propia.

***1.3 Ejercicio nivel dragón:***


<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/9.-Circuito%203_2.jpeg" alt="imagen del grupo" width="600px"/>
</p>



***Figura 11:*** Ejercicio de Circuito N°3. Fue extraído de la Guia 3 del laboratorio (Ejercicios_Fund_Electronica_1)



**Evidencia del trabajo realizado:**



<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/8.-Circuito%203.jpeg" width="600px"/>
</p>




***Figura 12:*** Circuito de resistencias en protoboard. Elaboración propia.

Valor de cada resistencia:

$R_{\text{1}}$:10000Ω

$R_{\text{2}}$:10000Ω

$R_{\text{3}}$:10000Ω

$R_{\text{4}}$:10000Ω

$R_{\text{5}}$:10000Ω

$R_{\text{6}}$:10000Ω

**Representación gráfica del circuito real y el circuito reescrito:**





<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/91.-Circuito.jpeg" width="300px"/>
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/10.-Circuito%203_3.jpeg" width="400px"/>
</div>


***Figura 13:*** Circuito de resistencias. Elaboración propia.


***Figura 14:*** Esquema de circuito de resistencias Parte 1. Elaboración propia.

La resistencia $R_{\text{5}}$ y $R_{\text{6}}$ están en serie por lo tanto la sumatoria es directas:

$R_{\text{eq}}$= $R_{\text{5}}$ + $R_{\text{6}}$ = 10000Ω + 10000Ω

$R_{\text{eq}}$=20000Ω



<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/12.-Circuito%203_5.jpeg" alt="imagen del grupo" width="1000px"/>
</p>



***Figura 15:***  Esquema de circuito de resistencias Parte 2. Elaboración propia.

La resistencia $R_{\text{2}}$ y $R_{\text{4}}$ están en serie por lo tanto la sumatoria es directas:

$R_{\text{eq}}$ = $R_{\text{2}}$ + $R_{\text{4}}$ = 10000Ω +10000Ω

$R_{\text{eq}}$ =20000Ω 

La resistencia $R_{\text{1}}$ y $R_{\text{3}}$ también están en serie por lo tanto la sumatoria es directas:

$R_{\text{eq}}$= $R_{\text{1}}$ + $R_{\text{3}}$ =10000Ω +10000Ω

$R_{\text{eq}}$= 20000 Ω




<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/11.-Circuito%203_4.jpeg" alt="imagen del grupo" width="1000px"/>
</p>




***Figura 16:***  Esquema de circuito de resistencias Parte 3. Elaboración propia.

Finalmente, nos quedan las tres resistencias en paralelo. Para encontrar la resistencia equivalente total, realizamos la suma inversa de todas ellas.

$\frac{1}{R_{\text{T}}}$=  $\frac{1}{R_{1}--{3}}$ + $\frac{1}{R_{5}--{6}}$ + $\frac{1}{R_{2}--{4}}$

$\frac{1}{R_{\text{T}}}$= $\frac{1}{{\text{20000Ω}}}$ + $\frac{1}{{\text{20000Ω}}}$  + $\frac{1}{{\text{20000Ω}}}$ 

$\frac{1}{R_{\text{T}}}$= 1.5X10-4

$\frac{1}{R_{\text{T}}}$= $\frac{1}{{\text{1.5X10-4}}}$ 

$R_{\text{T}}$= 6666.666Ω


Una vez realizados los cálculos, pasamos a tomar las medidas con el multímetro para ver si el procedimiento realizado es correcto. 
Como podemos observar en la imagen el resultado tiene relación con lo obtenido experimentalmente.


<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/13.-Circuito%203_6.jpeg" alt="imagen del grupo" width="1000px"/>
</p>



***Figura 17:*** Medición de resistencias con multimetro. Elaboración propia.   






Circuitos útiles

2.1 Circuito Divisor de Tensión: Este circuito nos sirve para obtener un voltaje de salida ($V_{\text{Out}}$) en menor cantidad que el voltaje de entrada ($V_{\text{int}}$) utilizando la ley de Ohm. Por ejemplo, si queremos alimentar una bombilla a 6 voltios y solo disponemos de una pila de 10 voltios, podemos utilizar un circuito divisor de tensión en donde divida los 10 voltios de la pila en 2, una de 6 voltios ($V_{\text{Out}}$) y otra de 4 voltios (1). 


<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/16.-Formula.jpeg" width="300px"/>
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/15.-Ejercicio_4_Significado.jpeg" width="400px"/>
</div>


***Figura 18:*** Fórmula general a utilizar en un circuito divisor de tensión. Fue extraído de “Divisor de tensión”(1). 

Para el presente trabajo se recomendó que el voltaje de entrada y salida sean de 5 voltios y 1.1 voltios respectivamente. Como equipo decidimos que el valor de la resistencia 2 ($R_{\text{2}}$)  sea de 10 000 ohmios (Ω) al realizar las operaciones correspondientes se obtuvo que la resistencia 1 ($R_{\text{1}}$) debería tener un valor de 35 454.54 ohmios (Ω) .


$V_{\text{Out}}$= $\frac{R_{\text{2}}}{R_{1}+R_{2}}$  ($V_{\text{int}}$)

$\frac{V_{\text{Out}}}{V_{\text{int}}}$ = $\frac{R_{\text{2}}}{R_{1}+R_{2}}$

$\frac{1.1}{{\text{5}}}$ = $\frac{10 000}{R_{1} + 10 000}$

$R_{\text{1}}$ = 35 454.5454 Ω






Para comprobar lo calculado tratamos de formar una resistencia de 35 454.55 Ω aproximadamente, es por ello que se usaron 3 resistores en serie  con valores de 20 000, 10 000 y 6 000 Ω, al medir el voltaje de salida de esta nueva conexión se obtuvo como resultado un valor de 1.067 V concluyendo así que este resultado se aproximó al valor propuesto (1.1 V), una de las razones que no permitió llegar al valor propuesto fue por la diferencia de resistencia, ya que de acuerdo a los cálculos debió ser un resistor de 35 454.55 Ω, sin embargo, se utilizó uno de 36 000 Ω. 

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/14.-Ejercicio%204_%20Circuito.jpeg" alt="imagen del grupo" width="1000px"/>
</p>

***Figura 19:*** Conexión en serie de los 3 resistores para formar uno de 36 000 Ω . Elaboración propia.

<p align= "center">
  <img src="https://github.com/gcdavidq/Project_FdD/blob/main/Carpetas_del_Proyecto/Imagenes/Photos_lab2/17.-Resultados_ejercicio%204.jpeg" alt="imagen del grupo" width="1000px"/>
</p>


***Figura 20:*** Voltaje de salida ($V_{\text{Out}}$) de la nueva conexión. Elaboración propia.




### **REFERENCIA BIBLIOGRÁFICA:**

1. AREATECNOLOGIA. Divisor de tensión. Disponible en: https://www.areatecnologia.com/electronica/divisor-de-tension.html

