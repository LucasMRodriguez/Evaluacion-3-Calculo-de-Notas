# 👨‍🎓 Gestor Simple de Notas de Alumnos

Este proyecto es un script de consola desarrollado en Python que funciona como un sistema básico para calcular y gestionar las notas finales de los alumnos.

---

## 📝 Descripción

El programa presenta un menú interactivo que permite al usuario:

1.  **Calcular Promedio Ponderado:** Solicita el nombre de un alumno, la cantidad de notas, y luego el porcentaje (peso) y la nota de cada evaluación. Valida que los porcentajes sumen 100% y que las notas estén en el rango correcto (1.0 a 7.0).
2.  **Calcular Promedio Simple:** Solicita el nombre del alumno, cantidad de notas y la nota de cada evaluación, calculando un promedio donde todas tienen el mismo valor.
3.  **Ver Notas Guardadas:** Muestra un historial detallado de todos los cálculos realizados. Por cada alumno guardado, lista su nombre, el tipo de cálculo (Simple o Ponderado), las notas individuales, los porcentajes (si aplica) y el promedio final.
4.  **Salir:** Termina la ejecución del programa.

---

## 🚀 Instrucciones para Ejecutar

1.  Asegúrate de tener Python 3 instalado en tu sistema.
2.  Clona este repositorio o descarga el archivo `.py`.
3.  Abre una terminal o consola.
4.  Navega hasta la carpeta donde se encuentra el archivo.
    ```bash
    cd ruta/donde/esta/el/archivo
    ```
5.  Ejecuta el script con el siguiente comando (usa `python3` si `python` no funciona):

    ```bash
    python ProgramaGestor_Notas.py
    ```

6.  Sigue las instrucciones del menú en la consola.

---

## ⚙️ Requisitos

* **Python:** Se requiere **Python 3.6** o una versión superior (debido al uso de *f-strings* para formatear el texto).
* **Bibliotecas Adicionales:** Ninguna. El programa solo utiliza la biblioteca estándar `time`, que viene preinstalada con Python.
