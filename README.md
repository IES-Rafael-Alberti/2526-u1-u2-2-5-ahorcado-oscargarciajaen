[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/8lAzcOMh)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21506768&assignment_repo_type=AssignmentRepo)
# Práctica: El Juego del Ahorcado

## Descripción
El juego del "ahorcado" es un juego de lápiz y papel, en el que el objetivo es adivinar una palabra. Un jugador piensa una palabra y el otro jugador debe ir diciendo letras que cree que puede contener la palabra. Si acierta, se escriben todas las letras coincidentes. Si la letra no está, se resta un intento, agregando una parte al cuerpo (cabeza, brazo, etc.) hasta que queda dibujado todo el cuerpo del "ahorcado".

**Gana el juego** si se completa la palabra, y **se pierde** si se completa el número de intentos antes de completar la palabra.

En nuestra versión del ahorcado, no dibujaremos el cuerpo, sino que esta parte se simulará estableciendo un número de intentos, por ejemplo **5 intentos**.

## Objetivos de Aprendizaje
Esta práctica evalúa los siguientes conceptos:
- Variables y tipos de datos primitivos (int, float, bool) y String
- Sentencias condicionales (if, elif, else)
- Sentencias iterativas (while, for)
- Operadores lógicos y de comparación
- Manipulación básica de strings

## Requisitos del Programa

### 1. Lectura de la palabra a adivinar
- La palabra debe ser introducida por un jugador (posteriormente se ocultará para que el otro jugador no la vea)
- La palabra solo contendrá letras
- La palabra debe tener **mínimo 5 caracteres**
- Se convertirá a **mayúsculas** para evitar problemas con case sensitive

### 2. Lectura de las letras
- Solo se puede escribir **una letra** cada vez
- Solo se permiten **letras** (no números ni símbolos)
- Se convertirá a **mayúsculas** para evitar problemas con case sensitive

### 3. Lógica del juego
- Mostrar el estado de la palabra con guiones bajos (_) para las letras no adivinadas
- Mantener una **lista de letras usadas**
- Si una letra introducida:
  - **No está en la palabra** o **ya fue usada**: se resta un intento
  - **Está en la palabra** y **no fue usada**: se revelan todas las apariciones de esa letra
- El juego termina cuando:
  - Se adivina toda la palabra (GANA)
  - Se agotan los intentos (PIERDE)

## ¿Qué necesitamos?

### Estructuras de datos
- Una **lista** (o string) para guardar las letras usadas
- Una **variable string** para la palabra a adivinar
- Una **variable string** para el estado actual de la palabra (con _ y letras adivinadas)
- Una **variable int** para contar los intentos restantes

### Operaciones con Strings
Funciones útiles de Python para strings:
- `upper()` - Convertir a mayúsculas
- `lower()` - Convertir a minúsculas
- `replace()` - Reemplazar caracteres
- `in` - Verificar si un carácter está en un string
- `len()` - Obtener la longitud
- `isalpha()` - Verificar si es una letra
- `index()` o `find()` - Encontrar la posición de un carácter

### Operaciones con Listas
- `[]` - Crear lista vacía
- `append()` - Añadir elemento a la lista
- `in` - Verificar si un elemento está en la lista

### Bucles necesarios
- **While**: Para solicitar la palabra hasta que cumpla las condiciones
- **While**: Para el bucle principal del juego (mientras haya intentos y no se haya ganado)
- **For**: Para recorrer la palabra y reemplazar las letras adivinadas

## Metodología de Trabajo

1. **Dividirse en grupos** (si procede)
2. **Pensar y planificar** cómo resolver el problema
3. **Identificar herramientas** necesarias
4. **Implementar la solución** paso a paso
5. **Probar y depurar** el código

## Estructura del Proyecto

```
2526_PRO_u2_ahorcado/
│
├── README.md                 # Este archivo
├── src/
│   └── ahorcado.py          # Archivo principal del juego
├── docs/
│   └── planificacion.md     # Documento de planificación (opcional)
└── ejemplos/
    └── ejemplo_ejecucion.txt # Ejemplo de cómo debería funcionar
```

## Ejemplo de Ejecución

```
=== JUEGO DEL AHORCADO ===

Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): 
> PYTHON

[Limpiando pantalla...]

Jugador 2: ¡Adivina la palabra!

Intentos restantes: 5"""
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

Palabra: _ _ _ _ _ _
Letras usadas: []

Introduce una letra: A
¡Letra incorrecta!

Intentos restantes: 4
Palabra: _ _ _ _ _ _
Letras usadas: ['A']

Introduce una letra: P
¡Bien! La letra P está en la palabra.

Intentos restantes: 4
Palabra: P _ _ _ _ _
Letras usadas: ['A', 'P']

Introduce una letra: Y
¡Bien! La letra Y está en la palabra.

Intentos restantes: 4
Palabra: P Y _ _ _ _
Letras usadas: ['A', 'P', 'Y']

[...]

¡FELICIDADES! Has adivinado la palabra: PYTHON
```

## Evidencia de debbug

![Ejemplo debug](assets/debug.png)

En esta imagen podemos ver el estado de las variables durante el debug de mi programa.

## Evidencia de los comentarios

https://github.com/IES-Rafael-Alberti/2526-u1-u2-2-5-ahorcado-oscargarciajaen/blob/e6f9c3ddbd87863daa10adb88f0fac306cb93523/src/ahorcado.py#L56-L70

**Ejemplo para probar la comprobación de variables durante la ejecución del programa.**

## Notas Importantes

- **NO** es necesario terminar la solución completamente
- Se proporcionará una solución propuesta para discutir en clase
- El objetivo es **practicar y aprender**, no completar perfectamente
- Se valorará el **proceso de pensamiento** y la **planificación**

## Recursos de Referencia

- [Documentación oficial de Python sobre strings](https://docs.python.org/3/library/stdtypes.html#str)
- [revilofe.github.io - Recursos de programación](https://revilofe.github.io/)
- [Tutoriales de Python en W3Schools](https://www.w3schools.com/python/)

## Autor
Profesor: revilofe

## Licencia
Material educativo para uso académico
