import json

data = [
    {
        "ejercicio1": "1. Hacer un programa que calcule e imprima la suma de tres calificaciones."
    },
    {
        "ejercicio2": "2. Hacer un programa que calcule e imprima el salario semanal de un empleado a partir de sus horas semanales trabajadas y de su salario por hora."
    },
    {
        "ejercicio3": "3. Guillermo tiene N dólares. Luis tiene la mitad de lo que posee Guillermo. Juan tiene la mitad de lo que poseen Luis y Guillermo juntos. Hacer un programa que calcule e imprima la cantidad de dinero que tienen entre los tres."
    },
    {
        "ejercicio4": "4. Una compañía de venta de carros usados, paga a su personal de ventas un salario de $1000 mensuales, más una comisión de $150 por cada carro vendido, más el 5 % del valor de la venta por carro. Cada mes el capturista de la empresa ingresa en la computadora los datos pertinentes. Hacer un programa que calcule e imprima el salario mensual de un vendedor dado."
    },
    {
        "ejercicio5": "5.La calificación final de un estudiante de Informática se calcula con base a las calificaciones de tres aspectos de su rendimiento académico: participación, tareas y examen parcial. Sabiendo que las calificaciones anteriores entran a la calificación con po nderaciones del 10 %, 40% y 50 %. Hacer un programa que calcule e imprima la calificación de la Unidad obtenida por un estudiante."
    },
    {
        "ejercicio6": "6.Hacer un programa que calcule el cuadrado de una suma.\nX = a^2+ b^2 + 2ab"
    },
    {
        "ejercicio7": "7. Construir un programa que, dado un número total de horas, devuelve el número de semanas, días y horas equivalentes. Por ejemplo, dado un total de 1000 horas debe mostrar 5 semanas, 6 días y 16 horas."
    },
    {
        "ejercicio8": "8. Construir un programa que calcule y muestre por pantalla las raíces de la ecuación de segundo grado de coeficientes reales: ax^2 + bx + c = 0 \nUse la formula general."
    },
    {
        "ejercicio9": "9. Pedir dos números y decir cuál es el mayor o si son iguales."
    },
    {
        "ejercicio10": "10.Crea un programa que pedirá el ingreso de tres notas de un estudiante, luego calculará el promedio e imprimirá alguno de los siguientes mensajes:\n> 10 Aprobado \n> 7 y <= 10 Recuperación \n<= 7 Desaprobado"
    },
    {
        "ejercicio11": "11.Realiza un programa que pida una hora por teclado y que muestre luego buenos días, buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12. de 13 a 20 y de 21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por teclado."
    },
    {
        "ejercicio12": "12. Escribe un programa en que dado un número del 1 a 7 escriba el correspondiente nombre del día de la semana."
    },
    {
        "ejercicio13": "13.Hacer un programa que lea un carácter por teclado y compruebe si es una letra mayúscula."
    },
    {
        "ejercicio14": "14.En Plaza Vea se hace un 20% de descuento a los clientes cuya compra supere los S /300.00 ¿Cuál será la cantidad que pagará una persona por su compra?"
    },
    {
        "ejercicio15": "15. Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: Si trabaja 40 horas o menos se le paga S /16 por hora Si trabaja mas de 40 horas se le paga S /16 por cada una de las primeras 40 horas y S /20 por cada hora extra."
    },
    {
        "ejercicio16": "16. Construir un programa que simule el funcionamiento de una calculadora que puede realizar las cuatro operaciones aritméticas básicas(suma, resta, producto y división) con valores numéricos enteros. El usuario debe especificar la operación con el primer carácter del primer parámetro de la línea de comandos: S o s para la suma R o r para la resta P, p, M o m para el producto y D o d para la división."
    },
    {
        "ejercicio17": "17. Hacer un programa que simule un cajero automático con un saldo inicial de 1000 Dólares, con el siguiente menú de opciones: \n- Ingresar dinero a la cuenta \n- Retirar dinero de la cuenta \n- Salir"
    },
    {
        "ejercicio18": "18. Hacer un programa que pase de Kg a otra unidad de medida de masa, mostrar en pantalla un menú con las opciones posibles."
    },
    {
        "ejercicio19": "19. Realiza un programa que nos diga si hay probabilidad de que nuestra pareja nos está siendo infiel. El programa irá haciendo preguntas que el usuario contestará con verdadero o falso. Cada pregunta contestada como verdadero sumará 3 puntos. Las preguntas contestadas con falso no suman puntos. A continuación, se listan las preguntas del test.\n1) Tu pareja parece estar más inquieta de lo normal sin ningún motivo aparente.\n2) Ha aumentado sus gastos de vestuario\n3) Ha perdido el interés que mostraba anteriormente por tí\n4) Ahora se afeita y se asea con más frecuencia(si es hombre) o ahora se arregla el pelo y se asea con más frecuencia(si es mujer)\n5) No te deja que mires la agenda de su teléfono móvil\n6) A veces tiene llamadas que dice no querer contestar cuando estás tú delante\n7) Últimamente se preocupa más en cuidar la línea y/o estar bronceado/a\n8) Muchos días viene tarde después de trabajar porque dice tener mucho más trabajo\n9) Has notado que últimamente se perfuma más\n10) Se confunde y te dice que ha estado en sitios donde no ha ido contigo\n\nA continuación, se muestran los mensajes que deberá dar el programa según la puntuación obtenida.\n- Puntuación entre 0 y 10: ¡Enhorabuena! tu pareja parece ser totalmente fiel.\n- Puntuación entre 11 y 22: Quizás exista el peligro de otra persona en su vida o en su mente, aunque seguramente será algo sin importancia. No bajes la guardia.\n- Puntuación entre 22 y 30: Tu pareja tiene todos los ingredientes para estar viviendo un romance con otra persona. Te aconsejamos que indagues un poco más y averigües que es lo que está pasando por su cabeza."
    },
    {
        "ejercicio20": "20. Realiza un programa que diga si un número entero positivo introducido por teclado es capicúa. Se permiten números de hasta 5 cifras."
    }
]


def execute(fileName):
    i = 1
    for d in data:
        theFinalFile = f'{i}-{fileName}.py'
        exercises = open(theFinalFile, 'w', encoding='utf-8')
        exercises.write(f'"""\n{ d[f"ejercicio{i}"] }\n"""')
        i += 1


# def validateSequence(sequence, fileName):
#     if sequence == '1':
#         exercises = f'{fileName}{i}.py', 'w', encoding = 'utf-8'
#         return exercises
# the user wanna user letters so...
# if sequence == 'a':
#     exercises = "open(f'{fileName}{chr(96 + i)}.py', 'w', encoding='utf-8')"
#     return exercises
# if sequence == 'A':
#     exercises = "open(f'{fileName}{chr(64 + i)}.py', 'w', encoding='utf-8')"
#     return exercises


# def validatePosition(fileName, position, sequence):
#     # I write a condition with the data of the user
#     if position == 1:
#         info = f'i{fileName}.py'
#         return info
#     if position == 2:
#         info = f'{fileName}i.py'
#         return info


# (fileName, sequence, position):
def writeExercises(fileName):
    # I Execute my programn
    execute(fileName)


# i ask data
fileName = input("humano dime cómo quieres que se llamen los archivos: ")

writeExercises(fileName)
# sequence = input("humano como sabes los nombres de los archivos no se pueden repetir, ¿Qué te parece si le agregamos una secuencia? xD\nEscribe '1' si quieres que sea una secuencia de números\nEscribe 'a' en minúscula si quieres que sea una secuencia de letras del abecedarios en minúscula\nEscribe 'A' en mayúscula si quieres que sea una secuencia de letras del abecedarios en mayúscula")
# if sequence == 'a':
#     position = int(input(
#         "humano ahora como último paso quiero que me digas en dónde deberia poner la secuencia:\n1) a-ejemplo.py\n2) ejemplo-a.py"))
#     writeExercises(fileName, sequence, position)
# if sequence == 'A':
#     position = int(input(
#         "humano ahora como último paso quiero que me digas en dónde deberia poner la secuencia:\n1) A-ejemplo.py\n2) ejemplo-A.py"))
#     writeExercises(fileName, sequence, position)
# if sequence == '1':
#     position = int(input(
#         "humano ahora como último paso quiero que me digas en dónde deberia poner la secuencia:\n1) 1-ejemplo.py\n2) ejemplo1.py"))
#     writeExercises(fileName, sequence, position)
