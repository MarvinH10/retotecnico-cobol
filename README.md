# Procesador de Archivos CSV de Transacciones Bancarias

## Introducción
Este aplicativo es un reto práctico que tiene como propósito procesar un archivo CSV que contiene transacciones bancarias, para generar un reporte con información clave: balance final, la transacción de mayor monto y el conteo de transacciones por tipo (Crédito y Débito). La solución busca ser clara, concisa y fácil de ejecutar, facilitando el análisis de datos financieros a partir de un formato común.

## Instrucciones de Ejecución
1. **Clona este repositorio:**  
   ```bash
   git clone https://github.com/MarvinH10/retotecnico-cobol
   ```

2. **Navega al directorio del proyecto:**  
   ```bash
   cd retotecnico-cobol
   ```

3. **Coloca el archivo `archivo.csv` en el directorio raíz del proyecto.**

4. **Ejecutalo:**  
   ```bash
   python procesadorCSV.py archivo.csv
   ```

## Enfoque y Solución
La solución implementada se basa en dos funciones principales:

Procesamiento del CSV (procesar_csv):
Esta función abre el archivo CSV y utiliza el módulo csv.DictReader para leer las transacciones. Por cada fila del archivo:

* Se extraen y limpian los datos de cada transacción (tipo, monto e identificador).
* 
* Se actualiza el balance final aplicando sumas o restas según se trate de un crédito o un débito.
* 
* Se lleva un conteo de las transacciones de cada tipo.
* 
* Se evalúa si el monto de la transacción actual es mayor que el de la transacción previamente almacenada como la de mayor monto, actualizando esta información en caso afirmativo.

Generación del reporte (mostrar_reporte):
Una vez procesado el archivo, esta función imprime en la consola un reporte formateado que incluye:

* El balance final, mostrado con dos decimales.
* 
* La transacción con el mayor monto, indicando su identificador y valor.
* 
* El conteo total de transacciones clasificadas en crédito y débito.

## Estructura del Proyecto
El proyecto se compone de los siguientes archivos y carpetas:

1. **procesadorCSV.py:** 
Archivo principal que contiene la lógica de procesamiento del archivo CSV y la generación del reporte. Este script es el encargado de:

* Leer y procesar el archivo CSV.
* 
* Calcular el balance final a partir de las transacciones.
* 
* Identificar la transacción con el monto más alto.
* 
* Contabilizar la cantidad de transacciones de cada tipo.
* 
* Imprimir el reporte de resultados en la terminal.

2. **README.md:** 
Documento que proporciona una descripción detallada del proyecto, incluyendo su propósito, instrucciones de ejecución, el enfoque y la solución adoptada, así como la estructura del proyecto.

2. **(Opcional) Archivo CSV de ejemplo:** 
Se recomienda incluir un archivo CSV de prueba para facilitar la validación y el uso de la aplicación. Este archivo debe contener las columnas tipo, monto e id para que el script pueda procesarlo correctamente.