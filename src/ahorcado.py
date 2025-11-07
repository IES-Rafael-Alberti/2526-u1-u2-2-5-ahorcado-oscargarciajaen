"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: [Nombre del alumno]
Fecha: [Fecha]
"""

import random

def solicitar_palabra() -> str:  # [x]
    palabras = [
    "arbol", "camino", "viento", "bosque", "lluvia", "piedra", "sombra", "arena", "campo", "monte",
    "rioja", "tierra", "valle", "flores", "luces", "noche", "sonido", "fuerte", "suave", "brisa",
    "carro", "fuente", "sendero", "nubea", "rocio", "fuego", "hojas", "ramas", "tronco", "montes",
    "cielo", "claro", "oscuro", "polvo", "bruma", "espiga", "trigo", "sabio", "letra", "cuento",
    "tiempo", "reloj", "minuto", "sueño", "tarde", "mañana", "planta", "fruta", "sabor", "dulce",
    "amargo", "verde", "marron", "azul", "blanco", "negro", "rojo", "naranja", "violeta", "gris",
    "hierro", "cobre", "plata", "oro", "torre", "puente", "casa", "silla", "mesa", "cuadro",
    "suelo", "techo", "pared", "puerta", "ventana", "cortina", "huerto", "pradera", "playa",
    "rastro", "huella", "paso", "viaje", "destino", "rumbo", "sendero", "tramo", "borde", "curva",
    "reinos", "valles", "cantos", "nubes", "mares", "rios", "piedras", "campos", "flores", "llamas"
]

    indice = random.randint(0, 99)
    palabra = palabras[indice]
    return(palabra.upper())

def limpiar_pantalla(): # [x]
    """
    Imprime varias líneas en blanco para 'limpiar' la consola 
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)

def solicitar_letra(letras_usadas):  # [x]
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """

    letra = None
    while letra == None:
        letra = input("Introduce una letra: ")
        if len(letra) == 1:
            if letra.isalpha():
                letra = letra.upper()
                if letra not in letras_usadas:
                    return(letra)
                else:
                    letra = None
            else:
                letra = None
        else:
            letra = None

    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida # [x]
    # - Verificar que sea solo un carácter (len() == 1) # [x]
    # - Verificar que sea una letra (isalpha()) # [x]
    # - Verificar que no esté en letras_usadas (operador 'in') # [x]
    # - Convertir a mayúsculas (upper()) # [x]
    pass


def mostrar_estado(palabra_oculta, intentos, letras_usadas): # [x]
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    print(f"Le quedan {intentos} intentos ")
    print(" ".join(palabra_oculta))
    print("Letras usadas - > " + " ".join(letras_usadas))

    # TODO: Implementar la unción
    # - Imprimir intentos restantes # [x]
    # - Imprimir la palabra con espacios entre caracteres # [x]
    # - Imprimir las letras usadas # [x]
    pass


def actualizar_palabra_oculta(palabra, palabra_oculta, letra): # [x]
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar 
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
        
    Returns:
        str: La palabra oculta actualizada # [x]
    """ 
    acertado = None
    for i in range(len(palabra)):
            if letra == palabra[i]:
                palabra_oculta[i] = letra 
                acertado = True

    return(palabra_oculta)




    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for # [x]
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta # [x]
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string
    pass


def jugar(palabra:str):
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    intentos_restantes = INTENTOS_MAXIMOS
    letras_usadas = []
    palabra_oculta = []
    juego_terminado = False

    palabra_oculta = ["_"] * len(palabra)


    # TODO: Solicitar la palabra al jugador 1  # [x]
    # palabra = solicitar_palabra() # [x]
    
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    # limpiar_pantalla() # [x]
    
    # TODO: Inicializar variables del juego 
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _") # [x]
    # - intentos: número de intentos restantes # [x]
    # - letras_usadas: lista vacía # [x]
    # - juego_terminado: False # [x]
    
    print("Jugador 2: ¡Adivina la palabra!\n")
    
    while juego_terminado == False:
        mostrar_estado(palabra_oculta, intentos_restantes, letras_usadas)
        letra = solicitar_letra(letras_usadas)
        letras_usadas.append(letra)
        palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
        if "_" not in palabra_oculta:
            juego_terminado = True
            print("Has ganado")
            print(f"La palabra era {palabra}")
        elif letra not in palabra:
            intentos_restantes -= 1
            print("Has fallado \n")
            if intentos_restantes == 0:
                print(f"La palabra era {palabra}")
                juego_terminado = True

    

        
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual # [x]
    #   2. Solicitar una letra # [x]
    #   3. Añadir la letra a letras_usadas # [x]
    #   4. Si la letra está en la palabra: # [x]
    #      - Actualizar palabra_oculta # [x]
    #      - Mostrar mensaje de acierto # [x]
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado # [x]
    #   5. Si la letra NO está en la palabra:# [x]
    #      - Restar un intento# [x]
    #      - Mostrar mensaje de fallo# [x]
    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra # [x]
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta # [x]
    pass


def main():
    """
    Punto de entrada del programa
    """
    palabra = solicitar_palabra()
    jugar(palabra)

    jugar_otra_vez = input("\n¿Quieres volver a jugar? S/N): ")
    if jugar_otra_vez.lower() == 's':
        main()
    else:
        print("Cerrando...")


if __name__ == "__main__":
    main()
