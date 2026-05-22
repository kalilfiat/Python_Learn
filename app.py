"""
Python Basics Quest — Mini juego educativo para aprender Python desde cero.

Ejecutar con: python -m streamlit run app.py
"""

import random
import re
from pathlib import Path

import streamlit as st

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

APP_TITLE = "Python Basics Quest"
APP_SUBTITLE = "Aprende las bases de Python escribiendo código misión a misión."
DEFAULT_POINTS = 10
FINAL_BONUS_POINTS = 20
DEMO_NOT_STARTED = -1

# =============================================================================
# DATOS DE MISIONES
# Edita o agrega misiones copiando la estructura de un diccionario existente.
# El ejemplo enseña con unos datos; el ejercicio pide aplicar lo mismo con otros.
# =============================================================================

MISSIONS = [
    {
        "id": 1,
        "title": "Tu primer código",
        "learning_goal": "Escribir tu primera línea de Python.",
        "analogy": "Un programa puede empezar con una sola instrucción, como print().",
        "explanation": (
            "Python es un lenguaje de programación que lee instrucciones línea a línea. "
            "Tu primer paso práctico es mostrar un mensaje en pantalla con print()."
        ),
        "code_example": 'print("¡Hola, Python!")',
        "code_demo": [
            {
                "line": 'print("¡Hola, Python!")',
                "output": "¡Hola, Python!",
                "note": "Python ejecuta print y muestra el texto entre comillas.",
            }
        ],
        "question": (
            'Escribe una línea que muestre exactamente este texto: '
            "Estoy aprendiendo Python"
        ),
        "answers": [
            'print("Estoy aprendiendo Python")',
            "print('Estoy aprendiendo Python')",
        ],
        "answer_type": "code",
        "multiline": False,
        "solution": 'print("Estoy aprendiendo Python")',
        "feedback_correct": "¡Tu primera línea de Python! Así se muestra texto en pantalla.",
        "common_mistakes": "El texto debe ir entre comillas y dentro de print().",
        "hint": "Usa print() con comillas alrededor del mensaje. No copies el ejemplo: cambia el texto.",
        "hint_skeleton": 'print("____")',
        "points": DEFAULT_POINTS,
    },
    {
        "id": 2,
        "title": "print()",
        "recap": "Ya escribiste tu primer print; ahora cambia el mensaje.",
        "learning_goal": "Mostrar un mensaje distinto al del ejemplo.",
        "analogy": "print() es como decirle a Python: 'muestra esto en pantalla'.",
        "explanation": (
            "La función print() muestra texto o valores en la pantalla. "
            "Puedes cambiar el mensaje entre comillas."
        ),
        "code_example": 'print("Hola, mundo")',
        "code_demo": [
            {
                "line": 'print("Hola, mundo")',
                "output": "Hola, mundo",
                "note": "Las comillas indican que el contenido es texto (string).",
            }
        ],
        "question": (
            'El ejemplo usa "Hola, mundo". Escribe un print que muestre exactamente: '
            "Bienvenido al quest"
        ),
        "answers": [
            'print("Bienvenido al quest")',
            "print('Bienvenido al quest')",
        ],
        "answer_type": "code",
        "multiline": False,
        "solution": 'print("Bienvenido al quest")',
        "feedback_correct": "Exacto. Cambiaste el mensaje pero usaste la misma idea del ejemplo.",
        "common_mistakes": "Sin comillas, Python interpreta las palabras como variables.",
        "hint": "Misma estructura que el ejemplo, pero con el texto Bienvenido al quest.",
        "hint_skeleton": 'print("____")',
        "points": DEFAULT_POINTS,
    },
    {
        "id": 3,
        "title": "Variables",
        "recap": "print() muestra en pantalla; las variables guardan valores con un nombre.",
        "learning_goal": "Crear una variable con un nombre y valor nuevos.",
        "analogy": "Una variable es una caja con etiqueta donde guardas un valor.",
        "explanation": (
            "Una variable guarda un valor con un nombre. "
            "Se crea con el signo = (asignación)."
        ),
        "code_example": 'nombre = "Ana"\nedad = 25',
        "code_demo": [
            {
                "line": 'nombre = "Ana"',
                "output": "",
                "note": "Variable de texto (str).",
            },
            {
                "line": "edad = 25",
                "output": "",
                "note": "Variable numérica entera (int).",
            },
        ],
        "question": (
            "El ejemplo usa nombre y edad. Crea una variable llamada edad con el valor 21 "
            "(número entero, sin comillas)."
        ),
        "answers": ["edad = 21", "edad=21"],
        "answer_type": "code",
        "multiline": False,
        "solution": "edad = 21",
        "feedback_correct": "Perfecto. nombre = texto; edad = número. Aplicaste el patrón con otro valor.",
        "common_mistakes": "21 no lleva comillas. Un solo = asigna, no compara.",
        "hint": "Formato: nombre_variable = valor. El valor es un número entero.",
        "hint_skeleton": "edad = __",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 4,
        "title": "Tipos de datos",
        "recap": "Las variables guardan valores; cada valor tiene un tipo (str, int, float, bool).",
        "learning_goal": "Crear un float aplicando lo visto sobre tipos.",
        "analogy": "Los tipos son categorías: texto, entero, decimal o verdadero/falso.",
        "explanation": (
            "Python tiene tipos básicos: str (texto), int (entero), float (decimal) y bool (True/False). "
            "El tipo depende de cómo escribes el valor."
        ),
        "code_example": (
            'texto = "hola"    # str\n'
            "numero = 42       # int\n"
            "precio = 9.99     # float\n"
            "activo = True     # bool"
        ),
        "code_demo": [
            {
                "line": "precio = 9.99",
                "output": "",
                "note": "Un número con punto decimal es float.",
            }
        ],
        "question": (
            "El ejemplo usa precio = 9.99. Crea una variable precio con el valor decimal 12.50"
        ),
        "answers": ["precio = 12.50", "precio=12.50", "precio = 12.5"],
        "answer_type": "code",
        "multiline": False,
        "solution": "precio = 12.50",
        "feedback_correct": "Correcto. 12.50 es un float porque tiene punto decimal.",
        "common_mistakes": "No uses comillas: '12.50' sería texto, no número decimal.",
        "hint": "Mismo patrón que el ejemplo, pero con el valor 12.50.",
        "hint_skeleton": "precio = __.__",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 5,
        "title": "Operadores matemáticos",
        "recap": "Los números pueden ser int o float; ahora calculemos con operadores.",
        "learning_goal": "Guardar el resultado de una operación en una variable.",
        "analogy": "Python calcula como una calculadora cuando usas +, -, *, /.",
        "explanation": (
            "Python puede hacer matemáticas: +, -, *, / y más. "
            "Puedes guardar el resultado en una variable."
        ),
        "code_example": "resultado = 10 + 5\nprint(resultado)  # muestra 15",
        "code_demo": [
            {
                "line": "resultado = 10 + 5",
                "output": "",
                "note": "Suma 10 + 5 y guarda 15 en resultado.",
            },
            {
                "line": "print(resultado)",
                "output": "15",
                "note": "Muestra el valor calculado.",
            },
        ],
        "question": (
            "El ejemplo suma 10 + 5. Escribe una línea que multiplique 7 * 6 "
            "y guarde el resultado en la variable resultado"
        ),
        "answers": ["resultado = 7 * 6", "resultado=7*6", "resultado = 7*6"],
        "answer_type": "code",
        "multiline": False,
        "solution": "resultado = 7 * 6",
        "feedback_correct": "¡Bien! Cambiaste la operación pero usaste el mismo patrón de asignación.",
        "common_mistakes": "No escribas solo 7 * 6; debes guardarlo en resultado = ...",
        "hint": "Usa * para multiplicar. 7 * 6 = 42.",
        "hint_skeleton": "resultado = __ * __",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 6,
        "title": "Comparaciones",
        "recap": "Los operadores matemáticos dan números; las comparaciones dan True o False.",
        "learning_goal": "Escribir una comparación que devuelva True o False.",
        "analogy": "Comparar es preguntar si algo es cierto; Python responde True o False.",
        "explanation": (
            "Los operadores ==, !=, >, <, >=, <= devuelven True o False. "
            "Puedes mostrar el resultado con print()."
        ),
        "code_example": "print(5 > 3)   # True\nprint(5 == 3)  # False",
        "code_demo": [
            {
                "line": "print(5 > 3)",
                "output": "True",
                "note": "5 es mayor que 3 → True.",
            },
            {
                "line": "print(5 == 3)",
                "output": "False",
                "note": "5 no es igual a 3 → False.",
            },
        ],
        "question": (
            "El ejemplo compara 5 y 3. Escribe una línea que imprima el resultado de "
            "comparar si 10 es menor que 3 (debería dar False)"
        ),
        "answers": ["print(10 < 3)", "print(10<3)"],
        "answer_type": "code",
        "multiline": False,
        "solution": "print(10 < 3)",
        "feedback_correct": "Correcto. 10 < 3 es False porque 10 no es menor que 3.",
        "common_mistakes": "No confundir < (menor que) con > (mayor que) ni con = (asignación).",
        "hint": "Operador < dentro de print(). Piensa: ¿10 es menor que 3?",
        "hint_skeleton": "print(__ __ __)",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 7,
        "title": "Condicionales if / elif / else",
        "recap": "True y False controlan el flujo; if ejecuta código solo si la condición es verdadera.",
        "learning_goal": "Escribir un bloque if con condición y print indentado.",
        "analogy": "if es: si se cumple esto, entonces haz aquello.",
        "explanation": (
            "Con if ejecutas código solo si una condición es verdadera. "
            "La línea del if termina en : y el bloque va indentado."
        ),
        "code_example": (
            "edad = 18\n"
            "if edad >= 18:\n"
            '    print("Mayor de edad")\n'
            "else:\n"
            '    print("Menor de edad")'
        ),
        "code_demo": [
            {
                "line": "if edad >= 18:",
                "output": "",
                "note": "Si la condición es True, entra al bloque. No olvides los dos puntos.",
            },
            {
                "line": '    print("Mayor de edad")',
                "output": "Mayor de edad",
                "note": "El bloque if va indentado con 4 espacios.",
            },
        ],
        "question": (
            "Ya existe puntos = 55 (contexto abajo). Escribe un if que compruebe si puntos >= 50 "
            'y, si es así, imprima "Aprueba". Solo el if y su bloque (2 líneas).'
        ),
        "question_context": "puntos = 55",
        "answers": [
            'if puntos >= 50:\n    print("Aprueba")',
            "if puntos >= 50:\n    print('Aprueba')",
            "if puntos>=50:\n    print(\"Aprueba\")",
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": 'if puntos >= 50:\n    print("Aprueba")',
        "feedback_correct": "Excelente. Aplicaste if con otra variable y otro umbral que en el ejemplo.",
        "common_mistakes": "Falta : al final del if, o el print no está indentado.",
        "hint": "Cambia edad >= 18 por puntos >= 50 y el mensaje por Aprueba.",
        "hint_skeleton": "if puntos >= __:\n    print(\"____\")",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 8,
        "title": "Listas",
        "recap": "Con if decides qué hacer; las listas guardan varios valores en orden.",
        "learning_goal": "Crear una lista con otros elementos que los del ejemplo.",
        "analogy": "Una lista es una fila ordenada de valores entre corchetes.",
        "explanation": (
            "Una lista guarda varios valores en orden, entre corchetes [ ]. "
            "Los elementos se separan con comas."
        ),
        "code_example": 'frutas = ["manzana", "pera", "uva"]\nprint(frutas)',
        "code_demo": [
            {
                "line": 'frutas = ["manzana", "pera", "uva"]',
                "output": "",
                "note": "Lista de tres strings.",
            },
            {
                "line": "print(frutas)",
                "output": "['manzana', 'pera', 'uva']",
                "note": "print muestra la lista completa.",
            },
        ],
        "question": (
            'El ejemplo usa frutas. Crea una lista llamada animales con exactamente '
            'estos tres valores: "gato", "perro", "pez"'
        ),
        "answers": [
            'animales = ["gato", "perro", "pez"]',
            "animales = ['gato', 'perro', 'pez']",
            'animales=["gato","perro","pez"]',
        ],
        "answer_type": "code",
        "multiline": False,
        "solution": 'animales = ["gato", "perro", "pez"]',
        "feedback_correct": "Correcto. Misma estructura que frutas, con otro nombre y otros datos.",
        "common_mistakes": "Usa corchetes [ ], no paréntesis. Separa con comas.",
        "hint": "Sustituye frutas por animales y pon los tres animales entre comillas.",
        "hint_skeleton": 'animales = ["____", "____", "____"]',
        "points": DEFAULT_POINTS,
    },
    {
        "id": 9,
        "title": "Índices de listas",
        "recap": "Las listas tienen elementos; cada uno se accede con un índice empezando en 0.",
        "learning_goal": "Acceder al elemento correcto por índice (el primero es 0).",
        "analogy": "El índice es la posición: 0 = primero, 1 = segundo, 2 = tercero.",
        "explanation": (
            "Cada elemento de una lista tiene un índice empezando en 0. "
            "Usas lista[indice] para acceder."
        ),
        "code_example": (
            'colores = ["rojo", "verde", "azul"]\n'
            "print(colores[0])  # rojo\n"
            "print(colores[1])  # verde"
        ),
        "code_demo": [
            {
                "line": "print(colores[0])",
                "output": "rojo",
                "note": "Índice 0 = primer elemento.",
            },
            {
                "line": "print(colores[1])",
                "output": "verde",
                "note": "Índice 1 = segundo elemento.",
            },
        ],
        "question": (
            "Con la lista dias del contexto, escribe una línea print que muestre "
            "el tercer día (recuerda: el índice del tercero no es 3)"
        ),
        "question_context": 'dias = ["Lun", "Mar", "Mie"]',
        "answers": ["print(dias[2])", "print(dias [2])", "print(dias[2] )"],
        "answer_type": "code",
        "multiline": False,
        "solution": "print(dias[2])",
        "feedback_correct": "Exacto. El tercer elemento tiene índice 2 porque empezamos en 0.",
        "common_mistakes": "dias[3] daría error; dias[1] es el segundo día, no el tercero.",
        "hint": "Primer elemento = 0, segundo = 1, tercero = ?",
        "hint_skeleton": "print(dias[__])",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 10,
        "title": "Diccionarios",
        "recap": "Las listas usan índices numéricos; los diccionarios usan claves con nombre.",
        "learning_goal": "Crear un diccionario con claves y valores distintos al ejemplo.",
        "analogy": "Un diccionario asocia claves con valores, como nombre → dato.",
        "explanation": (
            "Un diccionario guarda pares clave: valor entre llaves { }. "
            "Cada par usa dos puntos entre clave y valor."
        ),
        "code_example": (
            'persona = {"nombre": "Luis", "edad": 30}\n'
            'print(persona["nombre"])  # Luis'
        ),
        "code_demo": [
            {
                "line": 'persona = {"nombre": "Luis", "edad": 30}',
                "output": "",
                "note": "Dos pares clave: valor.",
            },
            {
                "line": 'print(persona["nombre"])',
                "output": "Luis",
                "note": "Accedemos con la clave entre corchetes.",
            },
        ],
        "question": (
            "El ejemplo usa persona. Crea un diccionario libro con claves "
            '"titulo" (valor "1984") y "paginas" (valor 328)'
        ),
        "answers": [
            'libro = {"titulo": "1984", "paginas": 328}',
            'libro = {"paginas": 328, "titulo": "1984"}',
            "libro = {'titulo': '1984', 'paginas': 328}",
        ],
        "answer_type": "code",
        "multiline": False,
        "solution": 'libro = {"titulo": "1984", "paginas": 328}',
        "feedback_correct": "Perfecto. Aplicaste el formato clave: valor con otros datos.",
        "common_mistakes": "328 es número sin comillas; '1984' sí lleva comillas por ser texto.",
        "hint": 'Formato: libro = {"clave": valor, "clave2": valor2}',
        "hint_skeleton": 'libro = {"titulo": "____", "paginas": __}',
        "points": DEFAULT_POINTS,
    },
    {
        "id": 11,
        "title": "Bucles for",
        "recap": "Los diccionarios asocian claves; for recorre secuencias elemento a elemento.",
        "learning_goal": "Escribir un for que recorra un string carácter a carácter.",
        "analogy": "for toma cada elemento de una secuencia y ejecuta un bloque.",
        "explanation": (
            "El bucle for recorre cada elemento de una secuencia. "
            "La línea for termina en : y el cuerpo va indentado."
        ),
        "code_example": (
            'frutas = ["manzana", "pera"]\n'
            "for fruta in frutas:\n"
            "    print(fruta)"
        ),
        "code_demo": [
            {
                "line": "for fruta in frutas:",
                "output": "",
                "note": "Cada vuelta, fruta toma un valor de la lista.",
            },
            {
                "line": "    print(fruta)",
                "output": "manzana\npera",
                "note": "Se imprime un elemento por vuelta.",
            },
        ],
        "question": (
            "El ejemplo recorre una lista. Escribe un for que recorra el string "
            '"abc" con la variable letra e imprima cada letra (2 líneas)'
        ),
        "answers": [
            'for letra in "abc":\n    print(letra)',
            "for letra in 'abc':\n    print(letra)",
            'for letra in "abc":\n    print(letra )',
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": 'for letra in "abc":\n    print(letra)',
        "feedback_correct": "Correcto. for también recorre strings, no solo listas.",
        "common_mistakes": "Olvidar : en el for o no indentar el print.",
        "hint": "Cambia fruta in frutas por letra in \"abc\".",
        "hint_skeleton": 'for letra in "____":\n    print(letra)',
        "points": DEFAULT_POINTS,
    },
    {
        "id": 12,
        "title": "Bucles while",
        "recap": "for recorre elementos; while repite mientras una condición sea True.",
        "learning_goal": "Escribir un while con condición y cuerpo indentado.",
        "analogy": "while repite mientras la condición sea True.",
        "explanation": (
            "El bucle while repite un bloque mientras una condición sea True. "
            "Termina en : y el cuerpo va indentado."
        ),
        "code_example": (
            "contador = 0\n"
            "while contador < 3:\n"
            "    print(contador)\n"
            "    contador += 1"
        ),
        "code_demo": [
            {
                "line": "while contador < 3:",
                "output": "",
                "note": "Mientras contador < 3, repite el bloque.",
            },
            {
                "line": "    print(contador)",
                "output": "0\n1\n2",
                "note": "Imprime el valor actual en cada vuelta.",
            },
        ],
        "question": (
            "Con n = 0 del contexto, escribe un while que se repita mientras n < 4 "
            "e imprima n en cada vuelta (2 líneas: while + print)"
        ),
        "question_context": "n = 0",
        "answers": [
            "while n < 4:\n    print(n)",
            "while n<4:\n    print(n)",
            "while n < 4:\n    print(n )",
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": "while n < 4:\n    print(n)",
        "feedback_correct": "Bien. Cambiaste contador < 3 por n < 4 y aplicaste el mismo patrón.",
        "common_mistakes": "Confundir while con for, o usar = en lugar de <.",
        "hint": "while variable < numero: y debajo print(variable) indentado.",
        "hint_skeleton": "while n < __:\n    print(n)",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 13,
        "title": "Funciones",
        "recap": "Los bucles repiten; las funciones agrupan código reutilizable con un nombre.",
        "learning_goal": "Definir una función con def y parámetros opcionales.",
        "analogy": "Una función es una receta con nombre que puedes reutilizar.",
        "explanation": (
            "Una función se define con def, nombre, paréntesis y dos puntos. "
            "Puede recibir parámetros dentro de los paréntesis. El cuerpo va indentado."
        ),
        "code_example": (
            "def saludar(nombre):\n"
            '    print("Hola,", nombre)\n\n'
            'saludar("Ana")  # llama con argumento'
        ),
        "code_demo": [
            {
                "line": "def saludar(nombre):",
                "output": "",
                "note": "def + nombre + parámetro entre paréntesis + :",
            },
            {
                "line": '    print("Hola,", nombre)',
                "output": "",
                "note": "El parámetro nombre se usa dentro de la función.",
            },
            {
                "line": 'saludar("Ana")',
                "output": "Hola, Ana",
                "note": "Al llamar, pasas el valor del argumento.",
            },
        ],
        "question": (
            'El ejemplo usa saludar(nombre). Escribe una función despedir() vacía '
            'y su print("Chau") indentado (2 líneas)'
        ),
        "question_context": "def saludar(nombre):\n    print(\"Hola,\", nombre)",
        "answers": [
            'def despedir():\n    print("Chau")',
            "def despedir():\n    print('Chau')",
            "def despedir() :\n    print(\"Chau\")",
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": 'def despedir():\n    print("Chau")',
        "feedback_correct": (
            "Perfecto. Las funciones encapsulan código; luego puedes añadir parámetros como en saludar(nombre)."
        ),
        "common_mistakes": "Falta () después del nombre o el print no está indentado.",
        "hint": "def despedir(): en una línea y print(\"Chau\") indentado abajo.",
        "hint_skeleton": "def despedir():\n    print(\"____\")",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 14,
        "title": "Imports",
        "recap": "Las funciones organizan tu código; import trae módulos listos de Python.",
        "learning_goal": "Importar un módulo escribiendo la línea import.",
        "analogy": "import trae herramientas que Python ya tiene en otras cajas (módulos).",
        "explanation": (
            "Con import traes un módulo completo. "
            "Luego puedes usar sus funciones, por ejemplo math.sqrt()."
        ),
        "code_example": "import math\nprint(math.sqrt(16))  # 4.0",
        "code_demo": [
            {
                "line": "import math",
                "output": "",
                "note": "Carga el módulo math.",
            },
            {
                "line": "print(math.sqrt(16))",
                "output": "4.0",
                "note": "Usamos una función del módulo importado.",
            },
        ],
        "question": (
            "El ejemplo importa math. Escribe la línea para importar el módulo random "
            "(misma sintaxis, otro nombre de módulo)"
        ),
        "answers": ["import random", "import random;"],
        "answer_type": "code",
        "multiline": False,
        "solution": "import random",
        "feedback_correct": "Exacto. import nombre_modulo funciona con cualquier módulo estándar.",
        "common_mistakes": "No uses comillas: import \"random\" no es válido.",
        "hint": "Solo cambia math por random.",
        "hint_skeleton": "import ____",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 15,
        "title": "Errores comunes",
        "recap": "import amplía tus herramientas; los errores te guían cuando algo falta en la sintaxis.",
        "learning_goal": "Corregir sintaxis: dos puntos e indentación en un if.",
        "analogy": "Corregir errores es parte de programar; Python te dice qué falta.",
        "explanation": (
            "SyntaxError suele indicar : o comillas faltantes. "
            "IndentationError indica que el bloque no está bien indentado."
        ),
        "code_example": (
            "# Incorrecto:\n"
            "if True\n"
            'print("ok")\n\n'
            "# Correcto:\n"
            "if True:\n"
            '    print("ok")'
        ),
        "code_demo": [
            {
                "line": "if True:",
                "output": "",
                "note": "El if necesita : al final.",
            },
            {
                "line": '    print("ok")',
                "output": "ok",
                "note": "El bloque del if debe ir indentado.",
            },
        ],
        "question": (
            "Corrige este código roto (faltan : e indentación). "
            "Escribe la versión correcta en 2 líneas:"
        ),
        "question_context": "if True\nprint(\"ok\")",
        "answers": [
            'if True:\n    print("ok")',
            "if True:\n    print('ok')",
            "if True :\n    print(\"ok\")",
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": 'if True:\n    print("ok")',
        "feedback_correct": "¡Bien! Agregaste : al if e indentaste el print.",
        "common_mistakes": "Sin : → SyntaxError. Sin indentar → IndentationError.",
        "hint": "Añade : después de if True y mueve print 4 espacios a la derecha.",
        "hint_skeleton": "if True:\n    print(\"____\")",
        "points": DEFAULT_POINTS,
    },
    {
        "id": 16,
        "title": "Mini desafío final",
        "recap": "Juntas funciones, bucles y print: el patrón base de muchos scripts reales.",
        "learning_goal": "Combinar def, for y print en una función.",
        "analogy": "Juntas piezas aprendidas: función + bucle + salida.",
        "explanation": (
            "¡Última misión! Define una función que reciba una lista "
            "y use for para imprimir cada elemento."
        ),
        "code_example": (
            "def mostrar_lista(items):\n"
            "    for item in items:\n"
            "        print(item)\n\n"
            'mostrar_lista(["a", "b", "c"])'
        ),
        "code_demo": [
            {
                "line": "def mostrar_lista(items):",
                "output": "",
                "note": "Función con un parámetro items.",
            },
            {
                "line": "    for item in items:",
                "output": "",
                "note": "Bucle for dentro de la función.",
            },
            {
                "line": "        print(item)",
                "output": "a\nb\nc",
                "note": "Imprime cada elemento al llamar la función.",
            },
        ],
        "question": (
            "Escribe una función mostrar(items) con un for que recorra items "
            "e imprima cada item (3 líneas: def, for, print)"
        ),
        "answers": [
            "def mostrar(items):\n    for item in items:\n        print(item)",
            "def mostrar(items):\n    for item in items:\n        print(item )",
        ],
        "answer_type": "code",
        "multiline": True,
        "solution": "def mostrar(items):\n    for item in items:\n        print(item)",
        "feedback_correct": "¡Excelente! Completaste el quest escribiendo código real.",
        "common_mistakes": "Cada nivel anidado necesita más indentación (4 espacios por nivel).",
        "hint": "Copia la estructura del ejemplo pero la función se llama mostrar, no mostrar_lista.",
        "hint_skeleton": "def mostrar(items):\n    for item in items:\n        print(item)",
        "points": FINAL_BONUS_POINTS,
    },
]

TOTAL_MISSIONS = len(MISSIONS)
MAX_SCORE = sum(m["points"] for m in MISSIONS)

VIEW_QUEST = "Python Basics Quest"
VIEW_MAYA = "Ejemplos Maya"
VIEW_COMBAT = "Arena de código"

COMBAT_PLAYER_MAX_HP = 100
COMBAT_MONSTER_MAX_HP = 40
COMBAT_DAMAGE_CORRECT = 20
COMBAT_DAMAGE_WRONG = 15
COMBAT_RECENT_QUEUE_SIZE = 6

ATTACK_WORDS = [
    "Rayo de fuego",
    "Golpe de hielo",
    "Tormenta arcana",
    "Corte veloz",
    "Explosion critica",
    "Pulso electrico",
]
VAR_NAMES = ["nivel", "puntos", "vida", "energia", "score", "power"]
LIST_WORDS = ["sol", "luna", "mar", "rio", "viento", "roca", "nube"]

# =============================================================================
# EJEMPLOS DE SCRIPTS MAYA
# Scripts sencillos con explicación línea a línea (se ejecutan en Maya).
# =============================================================================

MAYA_EXAMPLES = [
    {
        "id": 1,
        "title": "Tu primer script en Maya",
        "summary": "Importar maya.cmds y mostrar un mensaje en la Script Editor.",
        "python_concepts": ["import", "print", "alias (as)"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            'print("Hola desde Maya")'
        ),
        "lines": [
            {
                "line": "import maya.cmds as cmds",
                "explanation": (
                    "Importa el módulo de comandos de Maya. "
                    "El alias `as cmds` permite escribir cmds en lugar de maya.cmds."
                ),
            },
            {
                "line": 'print("Hola desde Maya")',
                "explanation": (
                    "Muestra texto en la Script Editor (parte inferior de Maya). "
                    "Útil para comprobar que el script se ejecutó."
                ),
            },
        ],
    },
    {
        "id": 2,
        "title": "Crear un cubo",
        "summary": "Crear geometry con cmds.polyCube y guardar el nombre en una variable.",
        "python_concepts": ["variables", "funciones", "diccionarios (resultado)"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "resultado = cmds.polyCube(name='miCubo', width=2, height=2, depth=2)\n"
            "nombre = resultado[0]\n"
            "print('Cubo creado:', nombre)"
        ),
        "lines": [
            {
                "line": "import maya.cmds as cmds",
                "explanation": "Acceso a los comandos de Maya.",
            },
            {
                "line": "resultado = cmds.polyCube(name='miCubo', width=2, height=2, depth=2)",
                "explanation": (
                    "Crea un cubo en la escena. `name` pone el nombre del objeto; "
                    "width/height/depth definen el tamaño. Devuelve una tupla con el nombre y el nodo de forma."
                ),
            },
            {
                "line": "nombre = resultado[0]",
                "explanation": (
                    "Guarda el nombre del transform en una variable. "
                    "resultado[0] es el primer elemento de la tupla devuelta."
                ),
            },
            {
                "line": "print('Cubo creado:', nombre)",
                "explanation": "Confirma en consola qué objeto se creó. print puede recibir varios valores.",
            },
        ],
    },
    {
        "id": 3,
        "title": "Renombrar un objeto",
        "summary": "Usar una variable con el nombre del objeto y cmds.rename.",
        "python_concepts": ["variables", "strings", "asignación"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "objeto = 'miCubo'\n"
            "nuevo_nombre = cmds.rename(objeto, 'cuboRenombrado')\n"
            "print('Ahora se llama:', nuevo_nombre)"
        ),
        "lines": [
            {
                "line": "objeto = 'miCubo'",
                "explanation": (
                    "Variable con el nombre del objeto en la escena (string). "
                    "Debe existir un objeto llamado miCubo o dará error."
                ),
            },
            {
                "line": "nuevo_nombre = cmds.rename(objeto, 'cuboRenombrado')",
                "explanation": (
                    "cmds.rename cambia el nombre del objeto. "
                    "Devuelve el nombre final (por si Maya añade sufijos como cuboRenombrado1)."
                ),
            },
            {
                "line": "print('Ahora se llama:', nuevo_nombre)",
                "explanation": "Muestra el nuevo nombre para verificar el cambio.",
            },
        ],
    },
    {
        "id": 4,
        "title": "Recorrer la selección con for",
        "summary": "Obtener objetos seleccionados y aplicar una acción a cada uno.",
        "python_concepts": ["listas", "for", "funciones"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "seleccion = cmds.ls(selection=True)\n"
            "\n"
            "for obj in seleccion:\n"
            "    cmds.move(0, 2, 0, obj, relative=True)\n"
            "    print('Movido:', obj)"
        ),
        "lines": [
            {
                "line": "seleccion = cmds.ls(selection=True)",
                "explanation": (
                    "cmds.ls lista objetos. selection=True devuelve solo los seleccionados. "
                    "El resultado es una lista (puede estar vacía)."
                ),
            },
            {
                "line": "for obj in seleccion:",
                "explanation": (
                    "Bucle for: en cada vuelta, obj toma el nombre de un objeto seleccionado. "
                    "Termina en dos puntos; el bloque siguiente va indentado."
                ),
            },
            {
                "line": "    cmds.move(0, 2, 0, obj, relative=True)",
                "explanation": (
                    "Mueve el objeto 2 unidades en Y (arriba). relative=True suma al valor actual. "
                    "Los cuatro primeros números son X, Y, Z."
                ),
            },
            {
                "line": "    print('Movido:', obj)",
                "explanation": "Imprime qué objeto se movió en esta vuelta del bucle.",
            },
        ],
    },
    {
        "id": 5,
        "title": "Comprobar si hay selección (if)",
        "summary": "Evitar errores comprobando la selección antes de actuar.",
        "python_concepts": ["if", "else", "len", "listas vacías"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "seleccion = cmds.ls(selection=True)\n"
            "\n"
            "if len(seleccion) == 0:\n"
            '    print("No hay nada seleccionado")\n'
            "else:\n"
            "    print('Objetos seleccionados:', seleccion)"
        ),
        "lines": [
            {
                "line": "seleccion = cmds.ls(selection=True)",
                "explanation": "Lista de objetos seleccionados en Maya.",
            },
            {
                "line": "if len(seleccion) == 0:",
                "explanation": (
                    "len() devuelve cuántos elementos tiene la lista. "
                    "Si es 0, no hay selección. == compara igualdad."
                ),
            },
            {
                "line": '    print("No hay nada seleccionado")',
                "explanation": "Rama if: mensaje cuando la lista está vacía.",
            },
            {
                "line": "else:",
                "explanation": "Si la condición del if es falsa, entra en else.",
            },
            {
                "line": "    print('Objetos seleccionados:', seleccion)",
                "explanation": "Muestra la lista completa de nombres seleccionados.",
            },
        ],
    },
    {
        "id": 6,
        "title": "Función reutilizable: crear esfera",
        "summary": "Definir una función con parámetros para automatizar tareas repetidas.",
        "python_concepts": ["def", "parámetros", "return implícito"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "\n"
            "def crear_esfera(nombre, radio):\n"
            "    resultado = cmds.polySphere(name=nombre, radius=radio)\n"
            "    return resultado[0]\n"
            "\n"
            "\n"
            "esfera = crear_esfera('miEsfera', 1.5)\n"
            "print('Esfera creada:', esfera)"
        ),
        "lines": [
            {
                "line": "def crear_esfera(nombre, radio):",
                "explanation": (
                    "Define una función llamada crear_esfera con dos parámetros: "
                    "nombre (string) y radio (número). Termina en dos puntos."
                ),
            },
            {
                "line": "    resultado = cmds.polySphere(name=nombre, radius=radio)",
                "explanation": (
                    "Crea una esfera usando los parámetros recibidos. "
                    "name y radius son argumentos del comando de Maya."
                ),
            },
            {
                "line": "    return resultado[0]",
                "explanation": (
                    "Devuelve el nombre del objeto creado a quien llamó la función. "
                    "return termina la función y entrega ese valor."
                ),
            },
            {
                "line": "esfera = crear_esfera('miEsfera', 1.5)",
                "explanation": (
                    "Llama a la función con argumentos concretos. "
                    "El valor devuelto se guarda en la variable esfera."
                ),
            },
            {
                "line": "print('Esfera creada:', esfera)",
                "explanation": "Confirma en consola el nombre de la esfera creada.",
            },
        ],
    },
    {
        "id": 7,
        "title": "Función con parámetros: mover objeto",
        "summary": "Definir una función que reciba un objeto y cuánto moverlo en Y.",
        "python_concepts": ["def", "parámetros", "variables"],
        "code": (
            "import maya.cmds as cmds\n"
            "\n"
            "\n"
            "def mover_arriba(objeto, unidades):\n"
            "    cmds.move(0, unidades, 0, objeto, relative=True)\n"
            "    print('Movido:', objeto, 'en Y:', unidades)\n"
            "\n"
            "\n"
            "mover_arriba('miCubo', 3)"
        ),
        "lines": [
            {
                "line": "def mover_arriba(objeto, unidades):",
                "explanation": (
                    "Función con dos parámetros: objeto (nombre en escena) y unidades (número). "
                    "Los parámetros actúan como variables locales dentro de la función."
                ),
            },
            {
                "line": "    cmds.move(0, unidades, 0, objeto, relative=True)",
                "explanation": (
                    "Mueve el objeto en Y usando el valor del parámetro unidades. "
                    "relative=True suma al valor actual."
                ),
            },
            {
                "line": "    print('Movido:', objeto, 'en Y:', unidades)",
                "explanation": "Confirma qué objeto se movió y cuánto.",
            },
            {
                "line": "mover_arriba('miCubo', 3)",
                "explanation": (
                    "Llama a la función pasando argumentos concretos. "
                    "objeto recibe 'miCubo' y unidades recibe 3."
                ),
            },
        ],
    },
]


# =============================================================================
# ARENA DE CÓDIGO — combate aleatorio contra monstruos
# =============================================================================

COMBAT_MONSTERS = [
    {"name": "BugSyntax", "emoji": "🐛", "flavor": "Confunde tus comillas y olvida los dos puntos."},
    {"name": "IndentationSlime", "emoji": "🟢", "flavor": "Devora la indentación de tus bloques if y for."},
    {"name": "LoopGoblin", "emoji": "🔄", "flavor": "Enreda tus bucles for y while."},
    {"name": "VariableBat", "emoji": "🦇", "flavor": "Roba nombres de variables y las mezcla."},
    {"name": "ImportPhantom", "emoji": "👻", "flavor": "Hace que olvides cómo importar módulos."},
    {"name": "ListSerpent", "emoji": "🐍", "flavor": "Enrosca tus listas e índices."},
    {"name": "FunctionGolem", "emoji": "🗿", "flavor": "Bloquea el camino hasta que definas una función."},
    {"name": "CompareTroll", "emoji": "👹", "flavor": "Distorsiona True y False en tus comparaciones."},
]


def gen_print_challenge() -> dict:
    text = random.choice(ATTACK_WORDS)
    return {
        "topic": "print",
        "question": f'Ataca al monstruo: escribe un print que muestre exactamente "{text}"',
        "answers": [f'print("{text}")', f"print('{text}')"],
        "hint": "Usa print() con comillas alrededor del texto.",
        "hint_skeleton": 'print("____")',
        "solution": f'print("{text}")',
        "multiline": False,
        "answer_type": "code",
    }


def gen_variable_str_challenge() -> dict:
    var = random.choice(VAR_NAMES)
    text = random.choice(ATTACK_WORDS)
    return {
        "topic": "variables",
        "question": f'Crea una variable {var} con el texto "{text}"',
        "answers": [f'{var} = "{text}"', f"{var} = '{text}'"],
        "hint": "Formato: nombre = valor entre comillas.",
        "hint_skeleton": f'{var} = "____"',
        "solution": f'{var} = "{text}"',
        "multiline": False,
        "answer_type": "code",
    }


def gen_variable_int_challenge() -> dict:
    var = random.choice(VAR_NAMES)
    num = random.randint(1, 20)
    return {
        "topic": "variables",
        "question": f"Crea una variable {var} con el número entero {num} (sin comillas)",
        "answers": [f"{var} = {num}", f"{var}={num}"],
        "hint": "Los enteros no llevan comillas.",
        "hint_skeleton": f"{var} = __",
        "solution": f"{var} = {num}",
        "multiline": False,
        "answer_type": "code",
    }


def gen_math_challenge() -> dict:
    a, b = random.randint(2, 9), random.randint(2, 9)
    op = random.choice(["+", "*"])
    expr = f"{a} {op} {b}"
    return {
        "topic": "operadores",
        "question": f"Calcula y guarda en resultado la operación: {expr}",
        "answers": [f"resultado = {expr}", f"resultado={a}{op}{b}"],
        "hint": "Usa resultado = y la operación matemática.",
        "hint_skeleton": "resultado = __ __ __",
        "solution": f"resultado = {expr}",
        "multiline": False,
        "answer_type": "code",
    }


def gen_compare_challenge() -> dict:
    a, b = random.randint(1, 15), random.randint(1, 15)
    op = random.choice([">", "<", "=="])
    return {
        "topic": "comparaciones",
        "question": f"Escribe print({a} {op} {b}) para mostrar el resultado de la comparación",
        "answers": [f"print({a}{op}{b})", f"print({a} {op} {b})"],
        "hint": "print() puede mostrar True o False de una comparación.",
        "hint_skeleton": f"print({a} __ {b})",
        "solution": f"print({a} {op} {b})",
        "multiline": False,
        "answer_type": "code",
    }


def gen_list_challenge() -> dict:
    words = random.sample(LIST_WORDS, 3)
    lista_str = ", ".join(f'"{w}"' for w in words)
    return {
        "topic": "listas",
        "question": f'Crea items = [{lista_str}]',
        "answers": [
            f"items = [{lista_str}]",
            f"items=[{lista_str}]",
        ],
        "hint": "Lista entre corchetes con comas.",
        "hint_skeleton": "items = [__, __, __]",
        "solution": f"items = [{lista_str}]",
        "multiline": False,
        "answer_type": "code",
    }


def gen_index_challenge() -> dict:
    words = random.sample(LIST_WORDS, 3)
    idx = random.randint(0, 2)
    context = f'datos = ["{words[0]}", "{words[1]}", "{words[2]}"]'
    return {
        "topic": "índices",
        "question": f"Con datos del contexto, imprime el elemento en índice {idx}",
        "question_context": context,
        "answers": [f"print(datos[{idx}])", f"print(datos [{idx}])"],
        "hint": "Recuerda: el primer índice es 0.",
        "hint_skeleton": f"print(datos[__])  # índice {idx}",
        "solution": f"print(datos[{idx}])",
        "multiline": False,
        "answer_type": "code",
    }


def gen_for_challenge() -> dict:
    var = random.choice(["x", "item", "elem"])
    seq = random.choice(["items", "lista", "datos"])
    return {
        "topic": "for",
        "question": f"Escribe la primera línea de un for que recorra {seq} usando {var}",
        "answers": [f"for {var} in {seq}:", f"for {var} in {seq} :"],
        "hint": "Formato: for variable in secuencia:",
        "hint_skeleton": f"for {var} in ____:",
        "solution": f"for {var} in {seq}:",
        "multiline": False,
        "answer_type": "code",
    }


def gen_def_challenge() -> dict:
    names = ["atacar", "defender", "curar", "golpear", "sanar"]
    name = random.choice(names)
    return {
        "topic": "funciones",
        "question": f"Define una función vacía llamada {name} (solo la primera línea)",
        "answers": [f"def {name}():", f"def {name}() :"],
        "hint": "def nombre():",
        "hint_skeleton": f"def {name}____",
        "solution": f"def {name}():",
        "multiline": False,
        "answer_type": "code",
    }


def gen_import_challenge() -> dict:
    modules = ["random", "math", "os", "json"]
    mod = random.choice(modules)
    return {
        "topic": "imports",
        "question": f"Escribe la línea para importar el módulo {mod}",
        "answers": [f"import {mod}", f"import {mod};"],
        "hint": "Formato: import nombre_modulo",
        "hint_skeleton": "import ____",
        "solution": f"import {mod}",
        "multiline": False,
        "answer_type": "code",
    }


COMBAT_TEMPLATES = [
    {"id": "print_text", "generator": gen_print_challenge},
    {"id": "variable_str", "generator": gen_variable_str_challenge},
    {"id": "variable_int", "generator": gen_variable_int_challenge},
    {"id": "math_op", "generator": gen_math_challenge},
    {"id": "compare", "generator": gen_compare_challenge},
    {"id": "list_create", "generator": gen_list_challenge},
    {"id": "index", "generator": gen_index_challenge},
    {"id": "for_line", "generator": gen_for_challenge},
    {"id": "def_line", "generator": gen_def_challenge},
    {"id": "import_line", "generator": gen_import_challenge},
]


def pick_combat_template(recent_ids: list[str]) -> dict:
    """Elige una plantilla evitando las usadas recientemente."""
    available = [t for t in COMBAT_TEMPLATES if t["id"] not in recent_ids]
    if not available:
        available = COMBAT_TEMPLATES
    return random.choice(available)


def spawn_combat_encounter(recent_ids: list[str]) -> tuple[dict, dict, str]:
    """Genera monstruo + reto aleatorio. Devuelve (monstruo, reto, template_id)."""
    template = pick_combat_template(recent_ids)
    monster = random.choice(COMBAT_MONSTERS)
    challenge = template["generator"]()
    challenge["template_id"] = template["id"]
    return monster, challenge, template["id"]


# =============================================================================
# VALIDACIÓN DE RESPUESTAS
# =============================================================================


def normalize_answer(text: str) -> str:
    """Normaliza una respuesta para comparación flexible."""
    if not text:
        return ""

    result = text.strip().lower()
    result = result.rstrip(";")
    result = result.replace("'", '"')
    result = re.sub(r"\s+", " ", result)

    result = re.sub(r"\s*=\s*", "=", result)
    result = re.sub(r"\s*>\s*", ">", result)
    result = re.sub(r"\s*<\s*", "<", result)
    result = re.sub(r"\s*:\s*", ":", result)
    result = re.sub(r"\s*,\s*", ",", result)
    result = re.sub(r"\s*\[\s*", "[", result)
    result = re.sub(r"\s*\]\s*", "]", result)
    result = re.sub(r"\s*\{\s*", "{", result)
    result = re.sub(r"\s*\}\s*", "}", result)
    result = re.sub(r"\s*\(\s*", "(", result)
    result = re.sub(r"\s*\)\s*", ")", result)

    return result


def normalize_code_line(text: str) -> str:
    """Normaliza una sola línea de código."""
    return normalize_answer(text.strip())


def normalize_code(text: str) -> str:
    """Normaliza código de una o varias líneas."""
    if not text:
        return ""

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line for line in normalized.split("\n") if line.strip()]

    if len(lines) <= 1:
        return normalize_code_line(normalized)

    return "\n".join(normalize_code_line(line) for line in lines)


def check_answer(user_input: str, mission: dict) -> bool:
    """Comprueba si el código escrito por el usuario es correcto."""
    if not user_input or not user_input.strip():
        return False

    normalized_user = normalize_code(user_input)
    for valid in mission.get("answers", []):
        if normalized_user == normalize_code(valid):
            return True

    return False


def get_alternative_valid_answers(mission: dict, matched: str | None = None) -> list[str]:
    """Lista otras respuestas válidas para mostrar tras acertar."""
    alternatives = []
    matched_normalized = normalize_code(matched) if matched else None

    for answer in mission.get("answers", []):
        if matched_normalized and normalize_code(answer) == matched_normalized:
            continue
        if answer not in alternatives:
            alternatives.append(answer)

    return alternatives


# =============================================================================
# GESTIÓN DE ESTADO (session_state)
# =============================================================================


def demo_step_key(mission_id: int) -> str:
    """Clave de session_state para el paso del demo de una misión."""
    return f"demo_step_{mission_id}"


def clear_demo_state() -> None:
    """Elimina el estado de todos los demos paso a paso."""
    keys_to_delete = [key for key in st.session_state if key.startswith("demo_step_")]
    for key in keys_to_delete:
        del st.session_state[key]


def init_session_state() -> None:
    """Inicializa las variables de sesión si no existen."""
    defaults = {
        "active_view": VIEW_QUEST,
        "selected_maya_example": 0,
        "current_mission": 0,
        "score": 0,
        "correct_answers": 0,
        "answered": False,
        "last_result": None,
        "completed_missions": [],
        "game_finished": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_game() -> None:
    """Reinicia el juego por completo."""
    st.session_state.current_mission = 0
    st.session_state.score = 0
    st.session_state.correct_answers = 0
    st.session_state.answered = False
    st.session_state.last_result = None
    st.session_state.completed_missions = []
    st.session_state.game_finished = False
    clear_demo_state()


def advance_mission() -> None:
    """Avanza a la siguiente misión."""
    clear_demo_state()
    st.session_state.current_mission += 1
    st.session_state.answered = False
    st.session_state.last_result = None

    if st.session_state.current_mission >= TOTAL_MISSIONS:
        st.session_state.game_finished = True


def mark_correct(mission: dict) -> None:
    """Registra una respuesta correcta y suma puntos (solo una vez por misión)."""
    mission_id = mission["id"]
    if mission_id not in st.session_state.completed_missions:
        st.session_state.completed_missions.append(mission_id)
        st.session_state.score += mission["points"]
        st.session_state.correct_answers += 1


def init_combat_state() -> None:
    """Inicializa el estado de la arena si no existe."""
    combat_defaults = {
        "combat_player_hp": COMBAT_PLAYER_MAX_HP,
        "combat_monster_hp": COMBAT_MONSTER_MAX_HP,
        "combat_monster": None,
        "combat_challenge": None,
        "combat_recent_templates": [],
        "combat_defeated": 0,
        "combat_streak": 0,
        "combat_game_over": False,
        "combat_answered": False,
        "combat_last_result": None,
        "combat_monster_defeated": False,
        "combat_hits": 0,
        "combat_misses": 0,
    }
    for key, value in combat_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_combat() -> None:
    """Reinicia una partida de arena."""
    st.session_state.combat_player_hp = COMBAT_PLAYER_MAX_HP
    st.session_state.combat_monster_hp = COMBAT_MONSTER_MAX_HP
    st.session_state.combat_monster = None
    st.session_state.combat_challenge = None
    st.session_state.combat_recent_templates = []
    st.session_state.combat_defeated = 0
    st.session_state.combat_streak = 0
    st.session_state.combat_game_over = False
    st.session_state.combat_answered = False
    st.session_state.combat_last_result = None
    st.session_state.combat_monster_defeated = False
    st.session_state.combat_hits = 0
    st.session_state.combat_misses = 0
    start_new_combat_encounter()


def update_recent_templates(template_id: str) -> None:
    """Actualiza la cola anti-repetición de plantillas."""
    recent = list(st.session_state.combat_recent_templates)
    recent.append(template_id)
    if len(recent) > COMBAT_RECENT_QUEUE_SIZE:
        recent = recent[-COMBAT_RECENT_QUEUE_SIZE:]
    st.session_state.combat_recent_templates = recent


def start_new_combat_encounter() -> None:
    """Genera un nuevo monstruo y reto de código."""
    recent = st.session_state.get("combat_recent_templates", [])
    monster, challenge, template_id = spawn_combat_encounter(recent)
    update_recent_templates(template_id)
    st.session_state.combat_monster = monster
    st.session_state.combat_challenge = challenge
    st.session_state.combat_monster_hp = COMBAT_MONSTER_MAX_HP
    st.session_state.combat_answered = False
    st.session_state.combat_last_result = None
    st.session_state.combat_monster_defeated = False


def ensure_combat_encounter() -> None:
    """Garantiza que hay un combate activo."""
    init_combat_state()
    if st.session_state.combat_game_over:
        return
    if st.session_state.combat_monster is None or st.session_state.combat_challenge is None:
        start_new_combat_encounter()


# =============================================================================
# UI — TEMA Y HELPERS VISUALES
# =============================================================================


def inject_custom_css() -> None:
    """Inyecta estilos gamificados desde assets/theme.css."""
    css_path = Path(__file__).parent / "assets" / "theme.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text(encoding='utf-8')}</style>", unsafe_allow_html=True)


def get_difficulty(mission_id: int) -> tuple[str, str]:
    """Devuelve (slug, etiqueta) de dificultad según el id de misión."""
    if mission_id <= 5:
        return "basico", "Básico"
    if mission_id <= 11:
        return "intermedio", "Intermedio"
    return "avanzado", "Avanzado"


def render_hero(
    subtitle: str | None = None,
    title: str | None = None,
    *,
    compact: bool = False,
    streak: int | None = None,
) -> None:
    """Banner principal con gradiente."""
    hero_title = title or APP_TITLE
    hero_sub = subtitle or APP_SUBTITLE
    compact_class = " quest-hero-compact" if compact else ""
    streak_html = ""
    if streak is not None:
        streak_html = f'<div class="hero-streak">Aciertos: {streak}</div>'
    st.markdown(
        f'<div class="quest-hero{compact_class}">'
        f"{streak_html}"
        f"<h1>{hero_title}</h1>"
        f"<p>{hero_sub}</p>"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_side_stat_list(items: list[tuple[str, str]]) -> None:
    """Lista vertical de métricas para el panel lateral."""
    rows = ['<div class="side-stats">']
    for label, value in items:
        rows.append(
            f'<div class="side-stat-row">'
            f'<span class="side-stat-label">{label}</span>'
            f'<span class="side-stat-value">{value}</span>'
            f"</div>"
        )
    rows.append("</div>")
    st.markdown("".join(rows), unsafe_allow_html=True)


def render_quest_side_panel() -> None:
    """Panel lateral: resumen, progreso y reinicio."""
    completed = len(st.session_state.completed_missions)
    progress_value = completed / TOTAL_MISSIONS if TOTAL_MISSIONS else 0
    pct = int(progress_value * 100)

    with st.container(border=True):
        st.markdown('<p class="panel-label">Resumen</p>', unsafe_allow_html=True)
        render_side_stat_list(
            [
                ("Puntos", str(st.session_state.score)),
                ("Aciertos", f"{st.session_state.correct_answers} / {TOTAL_MISSIONS}"),
                ("Progreso", f"{pct}%"),
            ]
        )
        st.progress(progress_value)
        if not st.session_state.game_finished:
            current = st.session_state.current_mission + 1
            st.caption(f"Lección {current} de {TOTAL_MISSIONS}")
        else:
            st.caption("Curso completado")

        st.divider()
        render_top_bar()


def render_combat_side_panel(*, game_over: bool = False) -> None:
    """Panel lateral de la arena: HP, racha y acciones."""
    max_player = COMBAT_PLAYER_MAX_HP
    max_monster = COMBAT_MONSTER_MAX_HP
    player_hp = st.session_state.combat_player_hp
    monster_hp = st.session_state.combat_monster_hp

    with st.container(border=True):
        st.markdown('<p class="panel-label">Estado</p>', unsafe_allow_html=True)
        render_side_stat_list(
            [
                ("Tu HP", str(player_hp)),
                ("HP reto", str(monster_hp)),
                ("Racha", str(st.session_state.combat_streak)),
                ("Superados", str(st.session_state.combat_defeated)),
            ]
        )
        st.progress(player_hp / max_player if max_player else 0, text="Tu HP")
        st.progress(monster_hp / max_monster if max_monster else 0, text="HP reto")

        if game_over:
            hits = st.session_state.combat_hits
            misses = st.session_state.combat_misses
            accuracy = int((hits / (hits + misses)) * 100) if (hits + misses) else 0
            st.caption(f"Precisión: {accuracy}%")
            if st.button("Nueva partida", key="combat_restart", type="primary", use_container_width=True):
                reset_combat()
                st.rerun()
        else:
            if st.button("Reiniciar partida", key="combat_reset", type="secondary", use_container_width=True):
                reset_combat()
                st.rerun()


def render_stat_cards(score: int, correct: int, total: int, pct: int) -> None:
    """Tres tarjetas de estadísticas."""
    st.markdown(
        f'<div class="stats-row">'
        f'<div class="stat-card stat-card-points">'
        f'<div class="stat-icon-wrap">P</div>'
        f'<div><div class="stat-value">{score}</div><div class="stat-label">Puntos</div></div>'
        f"</div>"
        f'<div class="stat-card stat-card-aciertos">'
        f'<div class="stat-icon-wrap">A</div>'
        f'<div><div class="stat-value">{correct} / {total}</div><div class="stat-label">Aciertos</div></div>'
        f"</div>"
        f'<div class="stat-card stat-card-progreso">'
        f'<div class="stat-icon-wrap">%</div>'
        f'<div><div class="stat-value">{pct}%</div><div class="stat-label">Progreso</div></div>'
        f"</div>"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_objective_box(text: str) -> None:
    """Caja destacada para el objetivo de aprendizaje."""
    st.markdown(
        f'<div class="objective-box">'
        f"<strong>Objetivo</strong>"
        f"<span>{text}</span>"
        f"</div>",
        unsafe_allow_html=True,
    )


def render_mission_header(mission_id: int, title: str) -> None:
    """Encabezado de misión con badge de dificultad."""
    slug, label = get_difficulty(mission_id)
    st.markdown(
        f'<div class="mission-header">'
        f'<h2 class="mission-title">'
        f'<span class="mission-number">{mission_id}</span> Misión {mission_id}: {title}'
        f"</h2>"
        f'<span class="badge badge-{slug}">{label}</span>'
        f"</div>",
        unsafe_allow_html=True,
    )


def render_section_label(icon: str, text: str) -> None:
    """Subtítulo de sección."""
    icon_html = f'<span class="section-title-icon">{icon}</span>' if icon else ""
    st.markdown(
        f'<div class="section-title">{icon_html} {text}</div>',
        unsafe_allow_html=True,
    )


def render_sidebar_brand() -> None:
    """Logo y nombre en sidebar."""
    st.sidebar.markdown(
        '<div class="sidebar-brand">'
        '<div class="sidebar-brand-text">Python Basics</div>'
        "</div>",
        unsafe_allow_html=True,
    )


def render_sidebar_nav() -> None:
    """Navegación principal con botones visuales."""
    st.sidebar.markdown('<div class="sidebar-nav-label">Navegación</div>', unsafe_allow_html=True)
    nav_items = [VIEW_QUEST, VIEW_MAYA, VIEW_COMBAT]
    for view_id in nav_items:
        is_active = st.session_state.active_view == view_id
        if st.sidebar.button(
            view_id,
            key=f"nav_{view_id}",
            type="primary" if is_active else "secondary",
            use_container_width=True,
        ):
            if not is_active:
                st.session_state.active_view = view_id
                st.rerun()


def render_mission_timeline() -> None:
    """Lista numerada de misiones en sidebar."""
    st.sidebar.markdown('<div class="sidebar-nav-label">Misiones</div>', unsafe_allow_html=True)
    items_html = ['<div class="mission-timeline">']
    for index, mission in enumerate(MISSIONS):
        mission_id = mission["id"]
        if mission_id in st.session_state.completed_missions:
            state = "done"
        elif index == st.session_state.current_mission and not st.session_state.game_finished:
            state = "active"
        else:
            state = "pending"
        title = mission["title"]
        if len(title) > 28:
            title = title[:26] + "…"
        step_label = str(mission_id)
        items_html.append(
            f'<div class="sidebar-mission {state}">'
            f'<div class="mission-step-num">{step_label}</div>'
            f'<div class="mission-step-title">{title}</div>'
            f"</div>"
        )
    items_html.append("</div>")
    st.sidebar.markdown("".join(items_html), unsafe_allow_html=True)


def render_maya_sidebar_list() -> None:
    """Lista clicable de ejemplos Maya en sidebar."""
    st.sidebar.markdown('<div class="sidebar-nav-label">Ejemplos</div>', unsafe_allow_html=True)
    selected = st.session_state.selected_maya_example
    for index, example in enumerate(MAYA_EXAMPLES):
        title = example["title"]
        if len(title) > 34:
            title = title[:32] + "…"
        is_active = index == selected
        label = f"{example['id']}. {title}"
        if st.sidebar.button(
            label,
            key=f"maya_sel_{index}",
            type="primary" if is_active else "secondary",
            use_container_width=True,
        ):
            if not is_active:
                st.session_state.selected_maya_example = index
                st.rerun()


def render_sidebar_cta() -> None:
    """Tarjeta motivacional al pie del sidebar."""
    st.sidebar.markdown(
        '<div class="sidebar-cta">'
        '<div class="sidebar-cta-text">Continúa con las lecciones en orden.</div>'
        '<div class="sidebar-cta-sub">Practicar escribiendo código es la forma más efectiva de aprender.</div>'
        "</div>",
        unsafe_allow_html=True,
    )


def render_top_bar(show_reset: bool = True) -> None:
    """Botón de reinicio de progreso (usar dentro de una columna o contenedor)."""
    if show_reset and st.button(
        "Reiniciar progreso",
        key="top_reset_game",
        type="secondary",
        use_container_width=True,
    ):
        reset_game()
        st.rerun()


def render_inline_button(
    label: str,
    key: str,
    *,
    primary: bool = True,
    disabled: bool = False,
    width: float = 1.0,
    standalone: bool = True,
) -> bool:
    """Botón compacto; standalone=False si ya está dentro de una columna."""
    btn_type = "primary" if primary else "secondary"
    if standalone:
        col_btn, _ = st.columns([width, 4 - width])
        with col_btn:
            return st.button(
                label,
                key=key,
                type=btn_type,
                disabled=disabled,
                use_container_width=True,
            )
    return st.button(
        label,
        key=key,
        type=btn_type,
        disabled=disabled,
        use_container_width=True,
    )


def render_demo_buttons(mission_id: int, current_step: int, total_steps: int, step_key: str) -> None:
    """Fila de botones del demo con proporciones equilibradas."""
    col_start, col_next, _ = st.columns([1.1, 1.1, 2.8])
    with col_start:
        if st.button("Ver ejecución", key=f"demo_start_{mission_id}", type="primary", use_container_width=True):
            st.session_state[step_key] = 0
            st.rerun()
    with col_next:
        next_disabled = current_step < 0 or current_step >= total_steps - 1
        if st.button(
            "Siguiente paso",
            key=f"demo_next_{mission_id}",
            disabled=next_disabled,
            type="secondary",
            use_container_width=True,
        ):
            st.session_state[step_key] = min(current_step + 1, total_steps - 1)
            st.rerun()


def open_mission_card():
    """Contenedor con borde estilizado como tarjeta de misión."""
    return st.container(border=True)


# =============================================================================
# RENDERIZADO DE LA INTERFAZ
# =============================================================================


def render_header() -> None:
    """Hero banner principal."""
    render_hero()


def render_quest_page() -> None:
    """Layout principal del curso: contenido + panel lateral."""
    col_main, col_side = st.columns([3, 1], gap="large")

    with col_side:
        render_quest_side_panel()

    with col_main:
        if st.session_state.game_finished:
            render_hero(
                subtitle="Completaste todas las lecciones del curso.",
                title="Curso completado",
                compact=True,
            )
            render_final_screen()
        else:
            render_header()
            mission_index = st.session_state.current_mission
            if 0 <= mission_index < TOTAL_MISSIONS:
                render_mission(MISSIONS[mission_index])
            else:
                st.session_state.game_finished = True
                st.rerun()


def render_sidebar() -> None:
    """Sidebar gamificado con brand, nav y contenido contextual."""
    render_sidebar_brand()
    render_sidebar_nav()

    view = st.session_state.active_view

    if view == VIEW_MAYA:
        st.sidebar.divider()
        render_maya_sidebar_list()
        render_sidebar_cta()
        return

    if view == VIEW_COMBAT:
        st.sidebar.divider()
        st.sidebar.markdown('<div class="sidebar-nav-label">Arena</div>', unsafe_allow_html=True)
        defeated = st.session_state.get("combat_defeated", 0)
        streak = st.session_state.get("combat_streak", 0)
        st.sidebar.markdown(
            f'<div class="sidebar-mini-stat">'
            f'<div class="stat-icon-wrap">D</div>'
            f'<div><div class="stat-value">{defeated}</div>'
            f'<div class="stat-label">Derrotados</div></div></div>',
            unsafe_allow_html=True,
        )
        st.sidebar.markdown(
            f'<div class="sidebar-mini-stat">'
            f'<div class="stat-icon-wrap">R</div>'
            f'<div><div class="stat-value">{streak}</div>'
            f'<div class="stat-label">Racha</div></div></div>',
            unsafe_allow_html=True,
        )
        if st.session_state.get("combat_game_over"):
            st.sidebar.warning("Fin de la partida — puedes reiniciar")
        render_sidebar_cta()
        return

    st.sidebar.divider()
    render_mission_timeline()
    render_sidebar_cta()


def render_code_demo(mission: dict) -> None:
    """Demo interactivo paso a paso del código de ejemplo."""
    code_demo = mission.get("code_demo")
    if not code_demo:
        return

    mission_id = mission["id"]
    step_key = demo_step_key(mission_id)
    if step_key not in st.session_state:
        st.session_state[step_key] = DEMO_NOT_STARTED

    current_step = st.session_state[step_key]
    total_steps = len(code_demo)

    st.markdown('<div class="demo-block">', unsafe_allow_html=True)
    render_section_label("", "Demo: ejecución paso a paso")
    st.caption("Pulsa los botones para ver qué hace cada línea de código.")
    render_demo_buttons(mission_id, current_step, total_steps, step_key)

    if current_step < 0:
        st.info("Pulsa **Ver ejecución** para empezar el demo.")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    render_section_label("", "Código ejecutado hasta ahora")
    lines_shown = []
    for step_index in range(current_step + 1):
        prefix = "→ " if step_index == current_step else "  "
        lines_shown.append(prefix + code_demo[step_index]["line"])
    st.code("\n".join(lines_shown), language="python")

    console_output = []
    for step_index in range(current_step + 1):
        output = code_demo[step_index].get("output", "")
        if output:
            console_output.append(output)
    if console_output:
        render_section_label("", "Consola")
        st.code("\n".join(console_output), language="text")

    active_note = code_demo[current_step].get("note", "")
    if active_note:
        st.info(f"Paso {current_step + 1}/{total_steps}: {active_note}")

    if current_step >= total_steps - 1:
        st.success("Demo completado. ¡Ahora escribe tu código!")

    st.markdown("</div>", unsafe_allow_html=True)


def render_mission(mission: dict) -> None:
    """Renderiza una misión con demo, consigna de código y feedback."""
    with open_mission_card():
        render_mission_header(mission["id"], mission["title"])

        if mission.get("recap"):
            st.markdown(f'<p class="recap-text">Repaso: {mission["recap"]}</p>', unsafe_allow_html=True)

        if mission.get("learning_goal"):
            render_objective_box(mission["learning_goal"])

        if mission.get("analogy"):
            st.markdown(f'<p class="analogy-text">Analogía: {mission["analogy"]}</p>', unsafe_allow_html=True)

        st.markdown(f'<p class="explanation-text">{mission["explanation"]}</p>', unsafe_allow_html=True)

        render_section_label("", "Ejemplo")
        st.code(mission["code_example"], language="python")

        render_code_demo(mission)

        st.divider()
        render_section_label("", "Tu turno — escribe código")
        st.markdown(f'<p class="question-text">{mission["question"]}</p>', unsafe_allow_html=True)

        if mission.get("question_context"):
            render_section_label("", "Contexto (ya definido)")
            st.code(mission["question_context"], language="python")

        st.markdown('<div class="code-input-block">', unsafe_allow_html=True)
        input_disabled = st.session_state.answered and st.session_state.last_result == "correct"
        answer_key = f"answer_{mission['id']}"
        placeholder = "Escribe aquí tu código Python..."

        if mission.get("multiline"):
            user_code = st.text_area(
                "Escribe tu código:",
                key=answer_key,
                disabled=input_disabled,
                placeholder=placeholder,
                height=130,
                label_visibility="collapsed",
            )
        else:
            user_code = st.text_input(
                "Escribe tu código:",
                key=answer_key,
                disabled=input_disabled,
                placeholder=placeholder,
                label_visibility="collapsed",
            )

        if render_inline_button(
            "Comprobar",
            f"check_{mission['id']}",
            disabled=st.session_state.answered,
            width=1.1,
        ):
            if check_answer(user_code, mission):
                st.session_state.last_result = "correct"
                st.session_state.answered = True
                mark_correct(mission)
            else:
                st.session_state.last_result = "incorrect"
                st.session_state.answered = True

        if st.session_state.answered:
            if st.session_state.last_result == "correct":
                st.success(f"¡Correcto! +{mission['points']} puntos")
                if mission.get("feedback_correct"):
                    st.write(mission["feedback_correct"])

                alternatives = get_alternative_valid_answers(mission, user_code)
                if alternatives:
                    render_section_label("", "También valían")
                    for alt in alternatives:
                        st.code(alt, language="python")

            else:
                st.error("Incorrecto. Revisa la explicación e inténtalo de nuevo.")
                st.warning(f"Pista: {mission['hint']}")

                if mission.get("hint_skeleton"):
                    with st.expander("Esqueleto de código"):
                        st.code(mission["hint_skeleton"], language="python")

                if mission.get("common_mistakes"):
                    with st.expander("Errores comunes"):
                        st.write(mission["common_mistakes"])

                if mission.get("solution"):
                    with st.expander("Ver solución"):
                        st.code(mission["solution"], language="python")

                if render_inline_button(
                    "Intentar de nuevo",
                    f"retry_{mission['id']}",
                    primary=False,
                    width=1.3,
                ):
                    st.session_state.answered = False
                    st.session_state.last_result = None
                    st.rerun()

        if st.session_state.answered and st.session_state.last_result == "correct":
            label = (
                "Siguiente lección"
                if st.session_state.current_mission < TOTAL_MISSIONS - 1
                else "Ver resumen final"
            )
            if render_inline_button(label, f"next_{mission['id']}", width=1.4):
                advance_mission()
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def render_maya_example(example: dict) -> None:
    """Muestra un script de Maya con explicación línea a línea."""
    with open_mission_card():
        st.markdown(
            f'<div class="mission-header">'
            f'<h2 class="mission-title">Ejemplo {example["id"]}: {example["title"]}</h2>'
            f'<span class="badge badge-referencia">Referencia</span>'
            f"</div>",
            unsafe_allow_html=True,
        )
        st.write(example["summary"])

        if example.get("python_concepts"):
            concepts = ", ".join(f"`{c}`" for c in example["python_concepts"])
            st.caption(f"Conceptos de Python que practicas: {concepts}")

        render_section_label("", "Script completo")
        st.code(example["code"], language="python")

        render_section_label("", "Explicación línea a línea")
        for index, item in enumerate(example["lines"], start=1):
            with st.expander(f"Línea {index}: `{item['line']}`", expanded=index == 1):
                st.code(item["line"], language="python")
                st.write(item["explanation"])


def render_maya_examples() -> None:
    """Sección de ejemplos didácticos de scripts para Autodesk Maya."""
    example_index = st.session_state.selected_maya_example
    example = MAYA_EXAMPLES[example_index]

    col_main, col_side = st.columns([3, 1], gap="large")

    with col_side:
        with st.container(border=True):
            st.markdown('<p class="panel-label">Ejemplo</p>', unsafe_allow_html=True)
            st.markdown(f"**{example_index + 1}** de {len(MAYA_EXAMPLES)}")
            st.caption(example["title"])
            st.divider()
            st.caption("Cambia de ejemplo con los botones del menú lateral.")

    with col_main:
        render_hero(
            subtitle="Scripts comentados línea a línea para Autodesk Maya.",
            title="Ejemplos Maya",
            compact=True,
        )
        st.info(
            "Copia el código en la **Script Editor** de Maya (pestaña Python). "
            "Los comandos `cmds.*` solo funcionan dentro de Maya."
        )
        render_maya_example(example)


def render_combat_arena() -> None:
    """Minijuego de combate: derrota monstruos escribiendo código Python."""
    ensure_combat_encounter()

    col_main, col_side = st.columns([3, 1], gap="large")
    game_over = st.session_state.combat_game_over

    with col_side:
        render_combat_side_panel(game_over=game_over)

    with col_main:
        render_hero(
            subtitle="Resuelve retos de código con dificultad variable.",
            title="Arena de código",
            compact=True,
        )

        if game_over:
            with open_mission_card():
                st.markdown(
                    '<div class="mission-header">'
                    '<h2 class="mission-title">Fin de la partida</h2>'
                    '<span class="badge badge-avanzado">Game over</span>'
                    "</div>",
                    unsafe_allow_html=True,
                )
                st.write("Has agotado tus intentos. Puedes iniciar una nueva partida desde el panel lateral.")
            return

        monster = st.session_state.combat_monster
        challenge = st.session_state.combat_challenge

        with open_mission_card():
            st.markdown(
                f'<div class="monster-card">'
                f'<p class="monster-name">{monster["emoji"]} {monster["name"]}</p>'
                f'<p class="monster-flavor">{monster["flavor"]}</p>'
                f"</div>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f'<span class="badge badge-arena">Concepto: {challenge.get("topic", "Python")}</span>',
                unsafe_allow_html=True,
            )

            render_section_label("", "Reto de código")
            st.write(challenge["question"])
            if challenge.get("question_context"):
                st.code(challenge["question_context"], language="python")

            st.markdown('<div class="code-input-block">', unsafe_allow_html=True)
            input_disabled = st.session_state.combat_answered and (
                st.session_state.combat_last_result == "correct"
                or st.session_state.combat_monster_defeated
            )

            if challenge.get("multiline"):
                user_code = st.text_area(
                    "Tu código:",
                    key="combat_answer",
                    disabled=input_disabled,
                    placeholder="Escribe aquí tu código Python...",
                    height=120,
                    label_visibility="collapsed",
                )
            else:
                user_code = st.text_input(
                    "Tu código:",
                    key="combat_answer",
                    disabled=input_disabled,
                    placeholder="Escribe aquí tu código Python...",
                    label_visibility="collapsed",
                )

            if render_inline_button(
                "Enviar respuesta",
                "combat_attack",
                disabled=st.session_state.combat_answered,
                width=1.0,
            ):
                is_correct = check_answer(user_code, challenge)
                st.session_state.combat_answered = True
                if is_correct:
                    st.session_state.combat_last_result = "correct"
                    st.session_state.combat_hits += 1
                    st.session_state.combat_monster_hp -= COMBAT_DAMAGE_CORRECT
                    if st.session_state.combat_monster_hp <= 0:
                        st.session_state.combat_monster_hp = 0
                        st.session_state.combat_monster_defeated = True
                        st.session_state.combat_defeated += 1
                        st.session_state.combat_streak += 1
                else:
                    st.session_state.combat_last_result = "incorrect"
                    st.session_state.combat_misses += 1
                    st.session_state.combat_streak = 0
                    st.session_state.combat_player_hp -= COMBAT_DAMAGE_WRONG
                    if st.session_state.combat_player_hp <= 0:
                        st.session_state.combat_player_hp = 0
                        st.session_state.combat_game_over = True

            if st.session_state.combat_answered:
                if st.session_state.combat_last_result == "correct":
                    st.success(f"¡Impacto! -{COMBAT_DAMAGE_CORRECT} HP al monstruo")
                    if st.session_state.combat_monster_defeated:
                        st.success(f"Reto superado. Racha: {st.session_state.combat_streak}")
                else:
                    st.error(f"Fallaste. El monstruo te golpea: -{COMBAT_DAMAGE_WRONG} HP")
                    st.warning(f"Pista: {challenge['hint']}")
                    if challenge.get("hint_skeleton"):
                        with st.expander("Esqueleto de código"):
                            st.code(challenge["hint_skeleton"], language="python")
                    with st.expander("Ver solución"):
                        st.code(challenge["solution"], language="python")
                    if render_inline_button(
                        "Reintentar",
                        "combat_retry",
                        primary=False,
                        width=1.3,
                    ):
                        st.session_state.combat_answered = False
                        st.session_state.combat_last_result = None
                        st.rerun()

            if st.session_state.combat_monster_defeated:
                if render_inline_button("Siguiente reto", "combat_next", width=1.4):
                    start_new_combat_encounter()
                    st.rerun()

            st.markdown("</div>", unsafe_allow_html=True)


def render_final_screen() -> None:
    """Pantalla final con resumen del progreso."""
    correct = st.session_state.correct_answers
    percentage = int((correct / TOTAL_MISSIONS) * 100) if TOTAL_MISSIONS else 0

    with open_mission_card():
        render_section_label("", "Temas que exploraste")
        badges_html = ['<div class="topic-grid">']
        for mission in MISSIONS:
            done = mission["id"] in st.session_state.completed_missions
            state = "done" if done else "pending"
            icon = "✅" if done else "⬜"
            badges_html.append(
                f'<div class="topic-badge {state}">{icon} {mission["title"]}</div>'
            )
        badges_html.append("</div>")
        st.markdown("".join(badges_html), unsafe_allow_html=True)

        if percentage == 100:
            st.success("¡Perfecto! Dominas las bases de Python. Sigue practicando con proyectos pequeños.")
        elif percentage >= 70:
            st.success("¡Muy bien! Repasa las misiones fallidas y sigue aprendiendo.")
        else:
            st.info("Buen intento. Vuelve a jugar y repasa los temas que te costaron.")

        st.markdown("---")
        st.markdown(
            "**Próximos pasos:** practica en un editor de Python, "
            "modifica los ejemplos de cada misión y experimenta cambiando valores."
        )


# =============================================================================
# PUNTO DE ENTRADA
# =============================================================================


def main() -> None:
    """Función principal que orquesta la app."""
    st.set_page_config(
        page_title=APP_TITLE,
        page_icon="🐍",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_custom_css()
    init_session_state()
    init_combat_state()
    render_sidebar()

    if st.session_state.active_view == VIEW_MAYA:
        render_maya_examples()
        return

    if st.session_state.active_view == VIEW_COMBAT:
        render_combat_arena()
        return

    render_quest_page()


if __name__ == "__main__":
    main()
