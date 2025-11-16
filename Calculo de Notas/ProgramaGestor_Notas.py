#Importamos el módulo 'time', que nos permite usar funciones
#relacionadas con el tiempo, como 'time.sleep()' para hacer pausas.
import time

#--- Función para Promedio PONDERADO ---
#AHORA DEVUELVE UN DICCIONARIO CON TODA LA INFO
def calcular_promedio_ponderado():
    
    while True:
        
        try:
            cantidad_notas_str = input("¿Cuántas notas vas a ingresar?: ").strip()
            cantidad_notas = int(cantidad_notas_str) 

            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return None 
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return None 

        #--- Configuración de Porcentajes ---
        porcentajes = [] 
        porcentaje_acumulado = 0.0 

        print("\n--- 1. Configuración de Porcentajes ---")
        print("Ingresa el 'peso' de cada evaluación (ej: 35 para 35%): ")

        for i in range(cantidad_notas):
            try:
                porcentaje_str = input(f" Porcentaje de la Evaluación {i + 1} (ej: 35): ").strip().replace(',', '.')
                porcentaje = float(porcentaje_str) 

                if porcentaje <= 0:
                    print("Error: El porcentaje debe ser un número positivo.")
                    return None

                porcentajes.append(porcentaje) 
                porcentaje_acumulado += porcentaje 
                
            except:
                print("Error: Ingresa un número válido para el porcentaje.")
                return None

        #--- Verificación de Porcentajes ---
        print("\n-----------------------------------------")
        print(f"Suma total de porcentajes ingresados: {round(porcentaje_acumulado)}%")

        if round(porcentaje_acumulado) != 100.0:
            print("¡ERROR! Los porcentajes no suman 100%.")
            print("Por favor, vuelve a ejecutar el programa con los porcentajes correctos.")
            return None 
 
        print("¡Configuración correcta! Los porcentajes suman 100%.")
        print("-----------------------------------------")

        #--- Ingreso de Notas (Ponderado) ---
        print("\n--- 2. Ingreso de Notas ---")
        nota_final_ponderada = 0.0
        
        #*** NUEVO: Lista para guardar las notas individuales ***
        notas_ingresadas = []

        for i in range(cantidad_notas):
            try:
                porcentaje_de_esta_nota = porcentajes[i]

                nota_str = input(f" Ingresa la Nota {i + 1} (que vale un {porcentaje_de_esta_nota}%): ").strip().replace(',', '.')
                nota = float(nota_str)

                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return None
                
                #*** NUEVO: Guardamos la nota individual ***
                notas_ingresadas.append(nota)

                #--- Cálculo Ponderado ---
                peso_decimal = porcentaje_de_esta_nota / 100.0
                contribucion = nota * peso_decimal
                nota_final_ponderada += contribucion

                print(f" -> Esta nota aporta {contribucion:.2f} puntos a tu promedio.")

            except:
                print("Error: Ingresa un número válido para la nota.")
                return None

        #--- Resultado Final (Ponderado) ---
        print("\n--- Cálculo Finalizado ---")
        resultado_final = round(nota_final_ponderada, 1)
        
        print(f"Tu Nota Final Ponderada es: {resultado_final}")
        
        #*** CAMBIO IMPORTANTE ***
        #Devolvemos un diccionario con toda la información
        return {
            "promedio_final": resultado_final,
            "notas_ingresadas": notas_ingresadas,
            "porcentajes": porcentajes
        }


#--- Función para Promedio SIMPLE ---
#AHORA DEVUELVE UN DICCIONARIO CON TODA LA INFO
def promedio_notas():
    while True:
        
        try:
            cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))

            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return None
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return None
        
        #--- Ingreso de Notas (Simple) ---
        #*** CAMBIO: Renombramos 'ListaNotas' a 'notas_ingresadas' por consistencia ***
        notas_ingresadas = [] 
        print("\n--- 2. Ingreso de Notas ---")

        for i in range(cantidad_notas):
            try:
                nota_str = input(f" Ingresa la Nota {i + 1}: ").strip().replace(',', '.')
                nota = float(nota_str)

                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return None

                notas_ingresadas.append(nota) #Agregamos la nota a la lista.

            except:
                print("Error: Ingresa un número válido para la nota.")
                return None

        #--- Cálculo y Resultado (Simple) ---
        print("\n--- Cálculo Finalizado ---")
        resultadoPromedio = sum(notas_ingresadas) / cantidad_notas
        
        resultado_final = round(resultadoPromedio, 1)
        
        print(f"Tu Nota Final Promediada es: {resultado_final}")

        #*** CAMBIO IMPORTANTE ***
        #Devolvemos un diccionario con toda la información
        return {
            "promedio_final": resultado_final,
            "notas_ingresadas": notas_ingresadas
        }
        

#--- Función Principal (MENÚ) ---
def main ():
    
    #*** CAMBIO: Ahora se implementa un gestor de alumnos/cálculos ***
    gestor_de_alumnos = []
    
    #*** NUEVO: Contador para "Alumno 1", "Alumno 2", etc. *** (Provisional)
    contador_alumnos = 1
    
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
                
                #*** NUEVO: Informamos para quién es el cálculo ***
                print(f"\n--- Preparando cálculo para: Alumno {contador_alumnos} ---")

                #*** CAMBIO: 'resultado_calculo' ahora es un diccionario ***
                resultado_calculo = calcular_promedio_ponderado() #Ejecuta la función

                if resultado_calculo is not None:
                    #*** NUEVO: Creamos el "paquete" de info para este alumno ***
                    info_alumno = {
                        "nombre": f"Alumno {contador_alumnos}",
                        "tipo": "Ponderado",
                        "calculo": resultado_calculo #Añadimos el diccionario del resultado
                    }
                    
                    #*** CAMBIO: Guardamos el paquete completo ***
                    gestor_de_alumnos.append(info_alumno)
                    
                    print(f"\n>> Notas de '{info_alumno['nombre']}' guardadas correctamente. <<")
                    
                    #*** NUEVO: Incrementamos el contador SOLO si fue exitoso ***
                    contador_alumnos += 1
                else:
                    print("\n>> Cálculo cancelado. No se guardó ningún dato. <<")


            #Opción 2: Llama a la función de promedio simple.
            elif r==2:
                print ("*"*61,"!Notas Promediadas¡","*"*60)
                
                #*** NUEVO: Informamos para quién es el cálculo ***
                print(f"\n--- Preparando cálculo para: Alumno {contador_alumnos} ---")

                #*** CAMBIO: 'resultado_calculo' ahora es un diccionario ***
                resultado_calculo = promedio_notas() #Ejecuta la función
                
                if resultado_calculo is not None:
                    #*** NUEVO: Creamos el "paquete" de info para este alumno ***
                    info_alumno = {
                        "nombre": f"Alumno {contador_alumnos}",
                        "tipo": "Simple",
                        "calculo": resultado_calculo #Añadimos el diccionario del resultado
                    }
                    
                    #*** CAMBIO: Guardamos el paquete completo ***
                    gestor_de_alumnos.append(info_alumno)
                    
                    print(f"\n>> Notas de '{info_alumno['nombre']}' guardadas correctamente. <<")

                    #*** NUEVO: Incrementamos el contador SOLO si fue exitoso ***
                    contador_alumnos += 1
                else:
                    print("\n>> Cálculo cancelado. No se guardó ningún dato. <<")
                    

            #*** CAMBIO: Opción 3 ahora lee la nueva estructura ***
            elif r == 3:
                print ("*"*61,"!Notas Guardadas¡","*"*62)
                
                if not gestor_de_alumnos: 
                    print("Aún no has guardado las notas de ningún alumno.")
                else:
                    print("Este es tu historial de alumnos y sus notas:")
                    
                    #Iteramos sobre la lista de diccionarios de alumnos
                    for alumno in gestor_de_alumnos:
                        
                        #Guardamos los datos en variables para más claridad
                        nombre = alumno['nombre']
                        tipo = alumno['tipo']
                        calculo = alumno['calculo'] #Este es el diccionario interno
                        
                        notas = calculo['notas_ingresadas']
                        promedio = calculo['promedio_final']
                        
                        #Imprimimos la info
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

                #Hacemos una pequeña pausa para que el usuario pueda leer.
                time.sleep(1)


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
