# Generador de Archivo Excel con Notas de Estudiantes

Este proyecto en Python permite crear un archivo Excel (`ejercicio1.xlsx`) que almacena los nombres de estudiantes y sus respectivas notas. El programa solicita al usuario ingresar los nombres y notas de tres estudiantes, y luego organiza esta información en un archivo Excel.

## Requisitos

* Python 3.x instalado en tu sistema.
* La librería `openpyxl` instalada. Puedes instalarla usando pip:

    ```bash
    pip install openpyxl
    ```

## Instalación

1.  Clona este repositorio o descarga el archivo `main.py`.
2.  Asegúrate de tener Python y `openpyxl` instalados.

## Uso

1.  Ejecuta el script `main.py` desde tu terminal:

    ```bash
    python main.py
    ```

2.  El programa te pedirá que ingreses el nombre y la nota de cada estudiante. Sigue las instrucciones en la terminal.

3.  Una vez que hayas ingresado todos los datos, el programa creará un archivo Excel llamado `ejercicio1.xlsx` en el mismo directorio donde se encuentra el script.

4.  Abre el archivo `ejercicio1.xlsx` con Microsoft Excel, LibreOffice Calc o cualquier otro programa compatible para ver los datos almacenados.

## Estructura del archivo Excel



* Columna A: Nombres de los estudiantes.
* Columna B: Notas de los estudiantes.
* La primera fila contiene los encabezados "Estudiante" y "Nota".
* Las filas siguientes contienen los datos de cada estudiante.

## Ejemplo



| Estudiante | Nota |
| :--------- | :--- |
| Juan       | 85   |
| María      | 92   |
| Pedro      | 78   |

## Notas Adicionales

* El programa actualmente está configurado para ingresar datos de tres estudiantes. Puedes modificar el ciclo `for` en el código para ingresar más o menos estudiantes.
* Asegúrate de ingresar notas válidas (números).
* El archivo excel se genera en el mismo directorio donde se ejecuta el script de python.

