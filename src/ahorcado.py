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


def solicitar_palabra() -> str:
    """
    Selecciona aleatoriamente una palabra de una lista predefinida.

    Returns
    -------
    str
        Palabra seleccionada en mayúsculas.
    """
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
    return palabra.upper()


def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para limpiar la consola.

    Esta función se utiliza para que el jugador 2 no vea la palabra
    introducida por el jugador 1.
    """
    print("\n" * 50)


def solicitar_letra(letras_usadas):
    """
    Solicita una letra al jugador 2 y valida la entrada.

    La letra debe ser no repetida, de un solo carácter y alfabética.

    Parameters
    ----------
    letras_usadas : list
        Lista de letras que ya han sido introducidas.

    Returns
    -------
    str
        Letra válida introducida por el jugador, en mayúsculas.
    """
    letra = None
    while letra is None:
        letra = input("Introduce una letra: ")
        if len(letra) == 1:
            if letra.isalpha():
                letra = letra.upper()
                if letra not in letras_usadas:
                    return letra
                else:
                    letra = None
            else:
                letra = None
        else:
            letra = None



def mostrar_estado(palabra_oculta, intentos, letras_usadas):
    """
    Muestra el estado actual del juego del ahorcado.

    Parameters
    ----------
    palabra_oculta : list of str
        Palabra con guiones bajos y letras adivinadas.
    intentos : int
        Número de intentos restantes.
    letras_usadas : list of str
        Letras que ya han sido introducidas.
    """
    print(f"Le quedan {intentos} intentos ")
    print(" ".join(palabra_oculta))
    print("Letras usadas -> " + " ".join(letras_usadas))
    


def actualizar_palabra_oculta(palabra, palabra_oculta, letra):
    """
    Actualiza la palabra oculta revelando las apariciones de la letra acertada.

    Parameters
    ----------
    palabra : str
        Palabra completa a adivinar.
    palabra_oculta : list of str
        Lista con la palabra oculta actual (guiones y letras descubiertas).
    letra : str
        Letra que se intenta adivinar.

    Returns
    -------
    list of str
        Palabra oculta actualizada con las letras descubiertas.
    """
    acertado = None
    for i in range(len(palabra)):
        if letra == palabra[i]:
            palabra_oculta[i] = letra
            acertado = True
    return palabra_oculta


def jugar(palabra: str):
    """
    Ejecuta la lógica principal del juego del ahorcado.

    Parameters
    ----------
    palabra : str
        Palabra que debe adivinar el jugador.
    """
    print("=== JUEGO DEL AHORCADO ===\n")

    INTENTOS_MAXIMOS = 5
    intentos_restantes = INTENTOS_MAXIMOS
    letras_usadas = []
    palabra_oculta = ["_"] * len(palabra)
    juego_terminado = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    while not juego_terminado:
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


def main():
    """
    Punto de entrada del programa.

    Ejecuta una partida del juego del ahorcado y pregunta si el jugador
    desea volver a jugar al finalizar.
    """
    palabra = solicitar_palabra()
    jugar(palabra)

    jugar_otra_vez = input("\n¿Quieres volver a jugar? (S/N): ")
    if jugar_otra_vez.lower() == 's':
        jugar(palabra)
    else:
        print("Cerrando...")


if __name__ == "__main__":
    main()
