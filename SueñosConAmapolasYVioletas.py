# PARA VISUALIZAR EL SIGUIENTE PROGRAMA:
# NECESITA DIRIGIRSE A:
# 
# O SINO A:
# 

import tkinter as tk
from tkinter import scrolledtext
import time

texto_carta = """
Sueños De Amapolas Y Violetas

Bienvenidos!
Esto es algo que quiero ir desarrollando con el paso de los años
Me gustaría ver de que soy capaz programando 
Es un proyecto raro pero que me da mucho orgullo hacer
Es algo personal y que capaz con el tiempo vaya agregando más cosas
Pero lo esencial es esto

Empezamos hoy:
6 de Mayo de 2024

-
.

.-
-- 
---

Linda fecha
Siempre lo guardo con amor
Mi mente siempre guarda lo más lindo de todo
Aunque es complicado
Me gusta pensar que me hace feliz
Yo funciono así
El amor me mueve
Siempre hice locuras por la gente que amo
Y lo voy a hacer toda mi vida
Quiero que estén orgullosos
Me esfuerzo siempre para eso
No siempre lo consigo
Pero nunca dejo de motivarme y seguir
Siempre hay una salida
Capaz soy muy positivo
Pero es lo que me lleva a ser yo mismo
Quiero vivir mi vida
Esforzándome por la gente que amo
Siempre voy a luchar por los que amo
No todos los saben
Pero siempre voy a estar ahí
Demostrando amor
Siempre trato de no decepcionar a las personas
Realmente quiero hacer feliz a las personas
También me esfuerzo
Me esfuerzo para cumplir mis sueños
Sueños para mí, para los que confiaron en mí.
Quiero crecer, quiero aprender, quiero egresarme
Quiero ser feliz
Que la gente que amo se alegre por mi felicidad
Y disfrutar con ellos
Quiero viajar
Conocer otros lugares del mundo
Y después darle la oportunidad de viajar a los que amo
Pero para eso tengo que viajar yo primero
Después de egresarme me voy a ir
Ver cómo me va ahí y como puedo crecer
Seguramente sea Australia
Por un tiempo
Tengo miedo
De alejarme y no estar con los que amo
Ya no quiero perder a la gente que amo
A nadie más
Pero lo tengo que hacer
Tenía otros planes
Siempre los mantengo
Sigue siendo mi sueño más importante
El sueño con el que sueño y deseo siempre
Pero actualmente no se puede
Ojalá que si
Aunque sea el único que confie en eso
Soy un soñador muy feliz
Y siempre voy a confiar en ese sueño que tengo hace dos años exactos
No tengo muchos sueños en mi vida
Solo algunos
Pero estoy muy enfocado y orgulloso de mis sueños
Hacer feliz y enorgullecer a la gente que amo con mis sueños
Así que ahora quiero estudiar, viajar, jugar al tenis, y mucho más
Cumplir la fantasía que tenía desde chico
Decirle a ese pibito, que vas a poder viajar
Solo, pero sabiendo que la gente que te ama esta con vos
Siempre
Cada día de mi vida
Están conmigo
Son mi fuerza de todos los días
Nunca los olvides
Mi familia
Mis amigos
Esas personas que compartí en mis actividades diarias
Y en especial
A las personas Bobas de mi vida:

-... 
..
.- 
-. 
-.-. 
.-

´´Entre Amapolas y Violetas
Que cada 6, florecen más y más
Desde el primer día que vi aquella flor
Su aroma me pudo encantar
La flor que enamora todo mi ser
Mente, corazón y alma
Y aunque este soleado o lluvioso
Siempre admire su belleza
Mi asombro es algo maravilloso
Mi amor a la naturaleza
Una flor única y especial
Y que nunca quise arrancar
El viento sopla y sopla
No sé a dónde la llevara
Si el camino nos cruza de vuelta
Como hilos rojos, el camino se va a trazar
Ansio ese momento, algún día llegara
Y por siempre esa flor cuidar
Por el resto de mis días
Y los colores de las flores se fusionaran
Esa flor que me cautiva
Desde que la vi
Y que me hace soñar
Con poder ser feliz
Te digo gracias de todo corazón
En mi vida siempre vas a estar
Y con orgullo estarás
Porque no hay nada más sincero
Que lo que acabo de contar
La distancia nos aleja
Pero el amor nos une
Y solo las amapolas y las violetas
Pueden encontrar de vuelta su perfume
Con mucha alegría
Con mucho cariño
Con mucha fe
El destino es el destino
Y eso lo descubrí
Cada 6 de mi vida´´

-agus
"""


def agregar_texto_progresivo(texto):
    texto_carta_texto.configure(state=tk.NORMAL)  
    for i, char in enumerate(texto):
        texto_carta_texto.insert(tk.END, char)
        
        texto_carta_texto.yview(tk.END)
        ventana.update()
        time.sleep(0.03)  
    texto_carta_texto.configure(state=tk.DISABLED)  

ventana = tk.Tk()
ventana.title("Carta")
ventana.geometry("800x600")

texto_carta_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=80, height=20, font=("Helvetica", 12))
texto_carta_texto.pack(expand=True, fill="both", padx=10, pady=10)

agregar_texto_progresivo(texto_carta)

ventana.mainloop()
