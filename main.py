import openpyxl

# PARTE 1: Crear diccionario y entrada de datos
estudiantes = {}

for i in range(3):
    nombre = input(f"Ingresa el nombre del estudiante {i+1}: ")
    nota = float(input(f"Ingresa la nota de {nombre}: "))
    estudiantes[nombre] = nota

# PARTE 2: Crear archivo Excel
libro = openpyxl.Workbook()
hoja = libro.active

# PARTE 3: Escribir encabezados
hoja["A1"] = "Estudiante"
hoja["B1"] = "Nota"

# PARTE 4: Escribir datos con ciclo
fila = 2
for nombre, nota in estudiantes.items():
    hoja[f"A{fila}"] = nombre
    hoja[f"B{fila}"] = nota
    fila += 1

# PARTE 5: Guardar archivo
libro.save("ejercicio1.xlsx")
print("¡Ejercicio 1 guardado en ejercicio1.xlsx!")
