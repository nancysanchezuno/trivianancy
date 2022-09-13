import random  # importamos la libreria random
import time

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

# BOOLEANO O DATO LÓGICO
iniciar_trivia = True
intentos = 0
# BUCLE SOBRE INICIO DE TRIVIA
while iniciar_trivia== True:
    intentos += 1
    puntaje = random.randint(0, 10)
    print()
    print("Intento número:", intentos)
    input("Presiona Enter para continuar.")
    print()
    # BIENVENIDA A LA TRIVIA
    print(
        GREEN + "            ***¡¡Bienvenidos a mi trivia!!***\n        ¿Conoces las capitales de los países de América?" + RESET
    )
    print()
    print("Conozcamonos un poco...")
    nombre = input(BLUE + "¿Cuál es tu nombre?:" + RESET)
    print()
    print(CYAN + "Hola", nombre,
          "esperamos que la pases genial,le recomendamos seguir las siguientes instrucciones para desarrollar la trivia:" + RESET)
    print()
    print(YELLOW + "1.Las respuestas deben estar en minúscula.")
    print("2.El puntaje variará dependiendo si la respuesta es correcta o incorrecta.")
    print("3.Lee las preguntas cuantas veces consideres necesarias.")
    print("4.Presiona la tecla Enter o Return luego de escribir tu respuesta." + RESET)
    print()
    print(WHITE + "Si está de acuerdo en continuar escriba 'si', o de lo contrario escriba 'no'." + RESET)
    continuar = input(YELLOW + "Respuesta: " + RESET)
    while continuar not in ("si", "no"):
        continuar = input(YELLOW + "Debe responder si o no para poder continuar. Inténtalo nuevamente: " + RESET)
    if continuar == "si":
        time.sleep(1)
        print(BLUE + "Bien!!, Empecemos con la trivia", nombre, "!" + RESET)
        # CARGA INICIAL DE 5 SEGUNDOS ANTES DE LA PRIMERA PREGUNTA
        for tiempo in range(5, 0, -1):
            print("Iniciamos en", tiempo, "segundos")
            time.sleep(1)
        print()
        print(RED + "Comenzarás con", puntaje,"puntos de bonificación. Aprovechalos!!!"+RESET)
        # PREGUNTA NUMERO 1 USANDO EL CICLO "FOR"
        print()
        print(
            MAGENTA + "1.¿Siguiendo el orden,¿cuales son las capitales de: Uruguay, Paraguay y Venezuela?" + RESET)
        print()
        print(" a.Montevideo,Asunción y Caracas")
        print(" b.Brasilia,Lima,Caracas")
        print(" c.Lima,Montevideo,Quito")
        print(" d.Caracas,Asunción,Bogotá")
        print()
        respuesta_usuario = input(YELLOW + "Coloque la letra de la respuesta correcta:" + RESET)
        paises = ["Uruguay", "Paraguay", "Venezuela"]
        capitales = ["Montevideo", "Asunción", "Caracas"]
        respuesta_correcta = "a"
        while respuesta_usuario not in ("a", "b", "c", "d"):
            respuesta_usuario = input("Debe responder a,b,c,d según considere correcto. Inténtalo nuevamente: ")
        if respuesta_usuario == respuesta_correcta:
            puntaje += random.randint(5, 10)
            print("Excelente", nombre, ",tu respuesta es correcta.")
        elif respuesta_usuario == "b":
            puntaje -= random.randint(0, 4)
            print("Lamentablemente", nombre, "la respuesta es incorrecta.")
        else:
            puntaje -= random.randint(0, 4)
            print("Lamentablemente", nombre, "la respuesta es incorrecta.")
        for number in range(0, 3):
            print("La capital de", paises[number], "es", capitales[number])
        print()
        print(RED + nombre, "llevas", puntaje, "puntos." + RESET)
        print()
        # PREGUNTA NUMERO 2
        time.sleep(1)
        print(MAGENTA + "2.¿Cuál es la capital de Argentina?" + RESET)
        print()
        print(" a.Bogotá")
        print(" b.Lima")
        print(" c.Brasilia")
        print(" d.Buenos Aires")
        print()
        respuesta_usuario = input(YELLOW + "Coloque la letra de la respuesta correcta:" + RESET)
        respuesta_correcta = "d"
        while respuesta_usuario not in ("a", "b", "c", "d"):
            respuesta_usuario = input("Debe responder a,b,c,d según considere correcto. Inténtalo nuevamente: ")
        if respuesta_usuario == "a":
            puntaje -= random.randint(0, 4)
            print("Incorrecto", nombre, "! Bogotá es la capital de Colombia.")
        elif respuesta_usuario == "b":
            puntaje -= random.randint(0, 4)
            print("Incorrecto", nombre, "! Lima es la capital de Perú.")
        elif respuesta_usuario == "c":
            puntaje -= random.randint(0, 4)
            print("Incorrecto", nombre, "! Brasilia es la capital de Brasil.")
        else:
            puntaje += random.randint(5, 10)
            print("Correcto", nombre, "!! Buenos Aires es la gran capital cosmopolita de Argentina.")
        print()
        print(RED + nombre, "llevas", puntaje, "puntos." + RESET)
        print()
        # PREGUNTA NUMERO 3 CON RESPUESTA SECRETA
        time.sleep(1)
        print(MAGENTA + "3.¿Cuál es la capital de Canadá?" + RESET)
        print()
        print(" a.Ottawa")
        print(" b.Brasilia")
        print(" c.Seúl")
        print(" d.Paris")
        print()
        respuesta_usuario = input(YELLOW + "Coloque la letra de la respuesta correcta:" + RESET)
        respuesta_correcta = "a"
        while respuesta_usuario not in ("a", "b", "c", "d", "x"):
            respuesta_usuario = input("Debe responder a,b,c,d según considere correcto. Inténtalo nuevamente:")
        if respuesta_usuario == "x":
            puntaje += random.randint(100, 200)
            print("Este es un mensaje secreto", nombre,
                  "por lo que como premio obtuviste muchisimos puntos adicionalesl!!")
        elif respuesta_usuario == respuesta_correcta:
            puntaje += random.randint(5, 10)
            print("Correcto", nombre, "!! Ottawa es la capital de Canadá y la cuarta ciudad más grande del país.")
            print("Ottawa fue fundada en 1850.")
        elif respuesta_usuario == "b":
            puntaje -= random.randint(0, 4)
            print("Lo lamentamos", nombre,
                  " su respuesta es incorrecta. Ottawa es la capital de Canadá y la cuarta ciudad más grande del país.")
        else:
            puntaje -= random.randint(0, 4)
            print("Lo lamentamos", nombre,
                  "su respuesta es incorrecta. Ottawa es la capital de Canadá y la cuarta ciudad más grande del país.")
        print()
        print(RED + nombre, "llevas", puntaje, "puntos." + RESET)
        print()
        time.sleep(1)
        # PREGUNTA NÚMERO 4
        print(MAGENTA + "4.¿Cuál es la capital de Surinam?" + RESET)
        print()
        print(" a.Georgetown")
        print(" b.Asunción")
        print(" c.Paramaribo")
        print(" d.Quito")
        print()
        respuesta_usuario = input(YELLOW + "Coloque la letra de la respuesta correcta:" + RESET)
        respuesta_correcta = "c"
        while respuesta_usuario not in ("a", "b", "c", "d"):
            respuesta_usuario = input("Debe responder a,b,c,d según considere correcto. Inténtalo nuevamente:")
        if respuesta_usuario == respuesta_correcta:
            puntaje = puntaje * 2
            print("Correcto", nombre,
                  "!!!!! Paramaribo es la capital de Surinam y está ubicada en el distrito de Paramaribo, a orillas del río Surinam.")
            print(
                "La población de la ciudad ronda los 250 000 habitantes, pero el área metropolitana alberga a casi 400 000 habitantes.")
        elif respuesta_usuario == "a":
            puntaje = puntaje + 5
            print("Incorrecto", nombre,
                  ". Paramaribo es la capital de Surinam y está ubicada en el distrito de Paramaribo, a orillas del río Surinam.")
            print(
                "La población de la ciudad ronda los 250 000 habitantes, pero el área metropolitana alberga a casi 400 000 habitantes.")
        elif respuesta_usuario == "b":
            puntaje -= 5
            print("... Paramaribo es la capital de Surinam.")
        else:
            puntaje = puntaje / 2
            print(
                "Totalmente incorrecto!!! Paramaribo es la capital de Surinam y está ubicada en el distrito de Paramaribo, a orillas del río Surinam.")
            print(
                "La población de la ciudad ronda los 250 000 habitantes, pero el área metropolitana alberga a casi 400 000 habitantes.")
        print()
        print(RED + "Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos." + RESET)

        # COMIENZA LA RULETA
        time.sleep(2)
        print("Finalmente,puedes usar tu suerte para cambiar tu puntaje total.")
        print()
        print(RED+"Advertencia: Asi como tu puntaje puede duplicarse tambien podría dividirse."+RESET)
        print()
        suerte = input(GREEN + "Deseas probar tu suerte? Escribe si o no: " + RESET)
        while suerte not in ("si", "no"):
            suerte = input(YELLOW + "Debes responder si o no. Ingresa nuevamente tu respuesta: " + RESET)
        if suerte == "si":
            numero_azar = random.randint(0, 1)
            if numero_azar == 0:
                puntaje = puntaje / 2
                time.sleep(1)
                print()
                print("Usaste toda tu suerte, pero no fue suficiente y tu puntaje se dividió ", nombre,", tu puntaje total es:", puntaje)
            elif numero_azar == 1:
                puntaje = puntaje * 2
                time.sleep(1)
                print()
                print("Usaste toda tu suerte y lograste duplicarlo ", nombre, ", tu puntaje total es: ", puntaje)
        else:
            print("Decidiste no usar tu suerte ", nombre, ", tu puntaje total es: ", puntaje)

        # PUNTAJE DE LA RULETA DE LA SUERTE
        if puntaje <= 50:
            print(MAGENTA + "No alcanzaste un puntaje alto pero no te desanimes, inténtalo de nuevo!")
        if 50 <= puntaje <= 100:
            print("Excelente,conoces mucho de Geografia. Felicidades.")
        if 100 < puntaje:
            print("Impresionante,alcanzaste un puntaje histórico. LO LOGRASTE!!!" + RESET)

        # CICLO DE JUEGO Y FINALIZACIÓN
        print()
        time.sleep(1)
        print(YELLOW+"¿Deseas intentar nuevamente la trivia?"+RESET)
        print()
        repetir_trivia = input(BLUE+"Ingresa 'si' para repetir, o cualquier tecla para finalizar: "+RESET).lower()

        if repetir_trivia != "si":  # != significa "distinto"
            print(GREEN+"Espero", nombre, "que te hayas divertido, hasta luego!!!"+RESET)
            iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
    else:
        time.sleep(1)
        print(GREEN+nombre,
              "lamentamos que no quieras continuar, puedes volver a intentar esta trivia en otro momento."+RESET)
        print(YELLOW + "Hasta pronto", nombre,"!!")
