#Importamos el módulo 'time', que nos permite usar funciones
#relacionadas con el tiempo, como 'time.sleep()' para hacer pausas.
import time

#--- Función para Promedio PONDERADO ---
#QUE DEVUELVE UN DICCIONARIO CON TODA LA INFO
def calcular_promedio_ponderado():
    
    while True:
        #Inicia un bucle 'while True' para que la función se pueda repetir
        #o reiniciar si hay un error, o terminar con 'break' o 'return'.
        try:
            cantidad_notas_str = input("¿Cuántas notas vas a ingresar?: ").strip()
            cantidad_notas = int(cantidad_notas_str) #Convertimos a número entero.
            
            #Validación: No podemos ingresar 0 o menos notas.
            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return None #RETURN sale de la función 'calcular_promedio_ponderado'.
            
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return None 

        #--- Configuración de Porcentajes ---
        porcentajes = [] #Lista donde se guardaran los porcentajes
        porcentaje_acumulado = 0.0 #Lista para sumar el 100% de los porcentajes.

        print("\n--- 1. Configuración de Porcentajes ---")
        print("Ingresa el 'peso' de cada evaluación (ej: 35 para 35%): ")

        #Bucle FOR para pedir los porcentajes de cada nota.
        for i in range(cantidad_notas):
            try:
                porcentaje_str = input(f" Porcentaje de la Evaluación {i + 1} (ej: 35): ").strip().replace(',', '.') #.replace(',', '.') permite al usuario usar comas o puntos.
                porcentaje = float(porcentaje_str) #Se cambia el valor ingresado a tipo FLOAT.

                #Si el porcentaje es menor o igual a cero arroja este mensaje.
                if porcentaje <= 0:
                    print("Error: El porcentaje debe ser un número positivo.")
                    return None #RETURN sale de la función.

                porcentajes.append(porcentaje) #Agregamos el porcentaje a la lista.
                porcentaje_acumulado += porcentaje #Sumamos al acumulado.
                
            except:
                print("Error: Ingresa un número válido para el porcentaje.")
                return None #RETURN sale de la función.

        #--- Verificación de Porcentajes ---
        print("\n-----------------------------------------")
        print(f"Suma total de porcentajes ingresados: {round(porcentaje_acumulado)}%") #Mostramos el total. round() redondea el número.

        if round(porcentaje_acumulado) != 100.0: 
            print("¡ERROR! Los porcentajes no suman 100%.")
            print("Por favor, vuelve a ejecutar el programa con los porcentajes correctos.")
            return None #Sale de la función.
 
        print("¡Configuración correcta! Los porcentajes suman 100%.")
        print("-----------------------------------------")

        #--- Ingreso de Notas (Ponderado) ---
        print("\n--- 2. Ingreso de Notas ---")
        nota_final_ponderada = 0.0
        
        #Se crea la lista donde se guardaran las notas ingresadas.
        notas_ingresadas = []

        #Bucle FOR para pedir cada nota
        for i in range(cantidad_notas): 
            try:
                porcentaje_de_esta_nota = porcentajes[i] #Obtenemos el porcentaje de la lista que llenamos antes.

                #Pedimos al usuario ingresar la nota
                nota_str = input(f" Ingresa la Nota {i + 1} (que vale un {porcentaje_de_esta_nota}%): ").strip().replace(',', '.') #.replace(',', '.') permite al usuario usar comas o puntos.
                nota = float(nota_str) #Se cambia a tipo FLOAT.

                if (nota < 1 or nota > 7.0): #Si la nota es menor a 1 y mayor a 7 arroja este mensaje.
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return None #Sale de la función.
                
                notas_ingresadas.append(nota) #Se agrega la nota

                #--- Cálculo Ponderado ---
                peso_decimal = porcentaje_de_esta_nota / 100.0
                contribucion = nota * peso_decimal
                nota_final_ponderada += contribucion

                print(f" -> Esta nota aporta {contribucion:.2f} puntos a tu promedio.")

            except:
                print("Error: Ingresa un número válido para la nota.")
                return None #Sale de la función.

        #--- Resultado Final (Ponderado) ---
        print("\n--- Cálculo Finalizado ---")
        resultado_final = round(nota_final_ponderada, 1) #Redondeamos el resultado de la nota.
        
        print(f"Tu Nota Final Ponderada es: {resultado_final}")
        
        #Devolvemos un diccionario con toda la información
        return {
            "promedio_final": resultado_final,
            "notas_ingresadas": notas_ingresadas,
            "porcentajes": porcentajes
        }


#--- Función para Promedio SIMPLE ---
def promedio_notas():
    while True:
        
        try:
            cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: ")) #Ingresa el usuario el numero de notas a ingresar.

            if cantidad_notas <= 0: #Si la cantidad de notas es menor o igual a 0, manda este mensaje.
                print("Error: Debes ingresar al menos una nota.")
                return None #Sale de la función.
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return None #Sale de la función.
        
        #--- Ingreso de Notas (Simple) ---
        notas_ingresadas = [] 
        print("\n--- 2. Ingreso de Notas ---")

        #Bucle FOR para ingresar las notas.
        for i in range(cantidad_notas):
            try:
                nota_str = input(f" Ingresa la Nota {i + 1}: ").strip().replace(',', '.') #.replace(',', '.') permite al usuario usar comas o puntos.
                nota = float(nota_str)

                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return None #Sale de la función.

                notas_ingresadas.append(nota) #Agregamos la nota a la lista.

            except:
                print("Error: Ingresa un número válido para la nota.")
                return None #Sale de la función.

        #--- Cálculo y Resultado (Simple) ---
        print("\n--- Cálculo Finalizado ---")
        resultadoPromedio = sum(notas_ingresadas) / cantidad_notas
        
        resultado_final = round(resultadoPromedio, 1) #Se redondea el resultado final.
        
        print(f"Tu Nota Final Promediada es: {resultado_final}")

        #Devolvemos un diccionario con toda la información
        return {
            "promedio_final": resultado_final,
            "notas_ingresadas": notas_ingresadas
        }
        

#--- Función Principal (MENÚ) ---
def main ():
    
    gestor_de_alumnos = []
    
    #*** CAMBIO: Se elimina 'contador_alumnos = 1' ***
    #Ya no usaremos "Alumno 1", sino el nombre real ingresado por el usuario.
    
    try:
        while True:
            #--- Impresión del Menú ---
            print ("-"*165)
            print ("="*66,'BIENVENIDO AL GESTOR DE NOTAS',"="*68)
            print ("-"*165)
            print ("="*78, 'MENÚ', "="*81)
            print ("-"*165)
            print ("-"*5,"Opcion 1. Ingreso de notas Ponderadas   |    Opcion 2. Ingreso de notas Promedio   |    Opcion 3. Ver Notas Guardadas   |    Opcion 4. Salir del Programa","-"*5)
            print ("-"*165)
            print("")
            
            r = int(input("Ingrese una opcion (1, 2, 3 o 4): "))
            print("")
            
            #--- Lógica del Menú (if/elif/else) ---
            
            #Opción 1: Llama a la función de promedio ponderado.
            if r==1:
                print ("*"*61,"!Notas Ponderadas¡","*"*61)
                
                #*** NUEVO: Pedimos el nombre del alumno ***
                nombre_alumno = ""

                #Bucle simple para asegurarnos de que el nombre no esté vacío.
                while not nombre_alumno:
                    nombre_alumno = input("\nIngrese el nombre del alumno: ").strip()
                    if not nombre_alumno:
                        print("Error: El nombre no puede estar vacío.")

                print(f"\n--- Preparando cálculo para: {nombre_alumno} ---")

                resultado_calculo = calcular_promedio_ponderado() #Ejecuta la función.

                if resultado_calculo is not None:
                    #*** CAMBIO: Guardamos el nombre ingresado ***
                    info_alumno = {
                        "nombre": nombre_alumno,
                        "tipo": "Ponderado",
                        "calculo": resultado_calculo 
                    }
                    
                    gestor_de_alumnos.append(info_alumno)
                    
                    print(f"\n>> Notas de '{info_alumno['nombre']}' guardadas correctamente. <<")
                    
                    #*** CAMBIO: Se elimina 'contador_alumnos += 1' ***
                else:
                    print("\n>> Cálculo cancelado. No se guardó ningún dato. <<")


            #Opción 2: Llama a la función de promedio simple.
            elif r==2:
                print ("*"*61,"!Notas Promediadas¡","*"*60)
                
                #*** NUEVO: Pedimos el nombre del alumno ***
                nombre_alumno = ""
                while not nombre_alumno:
                    nombre_alumno = input("\nIngrese el nombre del alumno: ").strip()
                    if not nombre_alumno:
                        print("Error: El nombre no puede estar vacío.")

                print(f"\n--- Preparando cálculo para: {nombre_alumno} ---")

                resultado_calculo = promedio_notas() #Ejecuta la función
                
                if resultado_calculo is not None:
                    #*** CAMBIO: Guardamos el nombre ingresado ***
                    info_alumno = {
                        "nombre": nombre_alumno,
                        "tipo": "Simple",
                        "calculo": resultado_calculo
                    }
                    
                    gestor_de_alumnos.append(info_alumno)
                    
                    print(f"\n>> Notas de '{info_alumno['nombre']}' guardadas correctamente. <<")

                    #*** CAMBIO: Se elimina 'contador_alumnos += 1' ***
                else:
                    print("\n>> Cálculo cancelado. No se guardó ningún dato. <<")
                    

            #Opción 3: Ver Notas Guardadas
            elif r == 3:
                
                if not gestor_de_alumnos: 
                    print("Aún no has guardado las notas de ningún alumno.")
                    print("")
                else:
                    print ("*"*61,"!Notas Guardadas¡","*"*62)
                    print("Este es tu historial de alumnos y sus notas:")

                    #Simplemente leerá el 'nombre' que guardamos (ej. "Juan Pérez") en lugar de Alumno 1 como antes.
                    for alumno in gestor_de_alumnos:
                        
                        nombre = alumno['nombre']
                        tipo = alumno['tipo']
                        calculo = alumno['calculo'] #Este es el diccionario interno

                        notas = calculo['notas_ingresadas']
                        promedio = calculo['promedio_final']
                        
                        print(f"\n----------------------------------------")
                        print(f"  Nombre:   {nombre}")
                        print(f"  Tipo:     Cálculo {tipo}")
                        print(f"  Notas:    {notas}")
                        
                        #Solo mostramos porcentajes si el cálculo fue ponderado
                        if tipo == "Ponderado":
                            porcentajes = calculo['porcentajes']
                            print(f"  Pond:     {porcentajes}%")
                        
                        print(f"  Promedio Final: {promedio}")
                        print(f"----------------------------------------")
                        print("")

                time.sleep(1.5) #Para que el usuario pueda procesar lo que pasa.


            #Opción 4: Salir del programa.
            elif r == 4:
                print ("Saliendo del programa...")
                time.sleep(1.5)
                break; 
            
            else:
                print("!Ingresa una opcion válida (1, 2, 3 o 4)¡");
    
    except:
        print("Error: !Ingresa una opcion valida¡")
        return 

#--- Ejecución del Programa ---
main()
