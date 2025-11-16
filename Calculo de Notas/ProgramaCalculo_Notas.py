#Importamos el módulo 'time', que nos permite usar funciones
#relacionadas con el tiempo, como 'time.sleep()' para hacer pausas.
import time

#--- Función para Promedio PONDERADO ---
#Define la función que calculará el promedio ponderado.
def calcular_promedio_ponderado():
    
    #Inicia un bucle 'while True' para que la función se pueda repetir
    #o reiniciar si hay un error, o terminar con 'break' o 'return'.
    while True:
        
        #--- Cantidad de Notas (Ponderado) ---
        #Usamos 'try y except' para manejar entradas inválidas (ej: "dos").
        try:
            #Pedimos la cantidad de notas.
            #.strip() elimina espacios en blanco.
            cantidad_notas_str = input("¿Cuántas notas vas a ingresar?: ").strip()
            cantidad_notas = int(cantidad_notas_str) #Convertimos a número entero.

            #Validación: No podemos ingresar 0 o menos notas.
            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return #RETURN sale de la función 'calcular_promedio_ponderado'.
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return #Sale de la función si la conversión a 'int' falla.

        #--- Configuración de Porcentajes ---
        porcentajes = [] #Lista para guardar los porcentajes (ej: 30, 30, 40).
        porcentaje_acumulado = 0.0 #Variable para sumar los porcentajes.

        print("\n--- 1. Configuración de Porcentajes ---")
        print("Ingresa el 'peso' de cada evaluación (ej: 35 para 35%): ")

        #Bucle FOR para pedir cada porcentaje.
        for i in range(cantidad_notas):
            try:
                #.replace(',', '.') permite al usuario usar comas o puntos.
                porcentaje_str = input(f" Porcentaje de la Evaluación {i + 1} (ej: 35): ").strip().replace(',', '.')
                porcentaje = float(porcentaje_str) #Convertimos a número decimal (float).

                #Validación: El porcentaje no puede ser negativo o cero.
                if porcentaje <= 0:
                    print("Error: El porcentaje debe ser un número positivo.")
                    return

                porcentajes.append(porcentaje) #Agregamos el porcentaje a la lista.
                porcentaje_acumulado += porcentaje #Sumamos al acumulado.
                
            except:
                print("Error: Ingresa un número válido para el porcentaje.")
                return

        #--- Verificación de Porcentajes ---
        print("\n-----------------------------------------")
        #Mostramos el total. round() redondea el número.
        print(f"Suma total de porcentajes ingresados: {round(porcentaje_acumulado)}%")

        #Validación: Los porcentajes DEBEN sumar 100.
        if round(porcentaje_acumulado) != 100.0:
            print("¡ERROR! Los porcentajes no suman 100%.")
            print("Por favor, vuelve a ejecutar el programa con los porcentajes correctos.")
            return #Sale de la función.
 
        print("¡Configuración correcta! Los porcentajes suman 100%.")
        print("-----------------------------------------")

        #--- Ingreso de Notas (Ponderado) ---
        print("\n--- 2. Ingreso de Notas ---")
        nota_final_ponderada = 0.0 # Variable para el resultado final.

        #Bucle FOR para pedir cada nota.
        for i in range(cantidad_notas):
            try:
                #Obtenemos el porcentaje de la lista que llenamos antes.
                porcentaje_de_esta_nota = porcentajes[i]

                nota_str = input(f" Ingresa la Nota {i + 1} (que vale un {porcentaje_de_esta_nota}%): ").strip().replace(',', '.')
                nota = float(nota_str)

                #Validación: La nota debe estar entre 1.0 y 7.0.
                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return

                #--- Cálculo Ponderado ---
                #Convertimos el porcentaje (ej: 35) a peso decimal (ej: 0.35).
                peso_decimal = porcentaje_de_esta_nota / 100.0
                #Multiplicamos la nota por su peso.
                contribucion = nota * peso_decimal
                #Sumamos esa contribución al total.
                nota_final_ponderada += contribucion

                #:.2f formatea el número para mostrar solo 2 decimales.
                print(f" -> Esta nota aporta {contribucion:.2f} puntos a tu promedio.")

            except:
                print("Error: Ingresa un número válido para la nota.")
                return

        #--- Resultado Final (Ponderado) ---
        print("\n--- Cálculo Finalizado ---")
        #Mostramos el resultado final, redondeado a 1 decimal.
        print(f"Tu Nota Final Ponderada es: {round(nota_final_ponderada,1)}")
        break; #BREAK rompe el bucle 'while True' y termina la función exitosamente.


#--- Función para Promedio SIMPLE ---
#Define la función que calculará el promedio simple (todas valen lo mismo).
def promedio_notas():
    while True:
        
        #--- Cantidad de Notas (Simple) ---
        try:
            cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))

            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return
        
        #--- Ingreso de Notas (Simple) ---
        ListaNotas = [] #Lista para guardar las notas.
        print("\n--- 2. Ingreso de Notas ---")

        for i in range(cantidad_notas):
            try:
                #Aquí no se pide porcentaje, solo la nota.
                nota = float(input(f" Ingresa la Nota {i + 1}: "))

                #Validación: La nota debe estar entre 1.0 y 7.0.
                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return

                ListaNotas.append(nota) #Agregamos la nota a la lista.

            except:
                print("Error: Ingresa un número válido para la nota.")
                return

        #--- Cálculo y Resultado (Simple) ---
        print("\n--- Cálculo Finalizado ---")
        #sum(ListaNotas) suma todos los números dentro de la lista.
        resultadoPromedio = sum(ListaNotas) / cantidad_notas
        
        print(f"Tu Nota Final Promediada es: {round(resultadoPromedio,1)}")
        break; #Termina la función exitosamente.
        

#--- Función Principal (MENÚ) ---
#Esta es la función que controla el flujo del programa.
def main ():
    #TRY & EXCEPT principal para atrapar errores en el menú (ej: escribir "a").
    try:
        #Bucle 'while True' para que el menú vuelva a aparecer
        #después de un cálculo (a menos que el usuario decida salir).
        while True:
            #--- Impresión del Menú ---
            #Imprimimos el menú con formato.
            print ("-"*142)
            print ("="*55,'Bienvenido al calculo de notas',"="*55)
            print ("-"*142)
            print ("="*68, 'MENÚ', "="*68)
            print ("-"*142)
            print ("-"*12,"Opcion 1. Ingreso de notas Ponderadas   |    Opcion 2. Ingreso de notas Promedio   |    Opcion 3. Salir del Programa","-"*12)
            print ("-"*142)
            print("")
            
            #Pedimos la opción al usuario.
            r = int(input("Ingrese una opcion (1,2 o 3): "))
            print("")
            
            #--- Lógica del Menú (if/elif/else) ---
            
            #Opción 1: Llama a la función de promedio ponderado.
            if r==1:
                print ("*"*61,"!Notas Ponderadas¡","*"*61)
                calcular_promedio_ponderado() #Ejecuta la función

                #Pregunta si desea salir después de terminar el cálculo.
                try:
                    #.upper() convierte la respuesta a MAYÚSCULAS (SI, S, NO, N).
                    res=input("¿Desea salir del programa? (SI/S | NO/N):").upper()
                    if (res=="SI" or res=="S"):
                        print ("Saliendo...")
                        break; #BREAK rompe el bucle 'while True' del MENÚ y termina el programa.
                    elif (res=="NO" or res=="N"):
                        print ("") #No hace nada y el 'while True' del menú se repite.
                    else:
                        print("!Ingrese una respuesta correcta¡") #Respuesta inválida.
                except:
                    print ("ERROR: !Ingrese una respuesta correcta¡")

            #Opción 2: Llama a la función de promedio simple.
            elif r==2:
                print ("*"*61,"!Notas Promediadas¡","*"*60)
                promedio_notas() #Ejecuta la función
                
                #Pregunta si desea salir (igual que en la opción 1).
                try:
                    res=input("¿Desea salir del programa? (SI/S | NO/N):").upper()
                    if (res=="SI" or res=="S"):
                        print ("Saliendo...")
                        break;
                    elif (res=="NO" or res=="N"):
                        print ("")
                    else:
                        print("!Ingrese una respuesta correcta¡")
                except:
                    print ("ERROR: !Ingrese una respuesta correcta¡")

            #Opción 3: Salir del programa.
            elif r == 3:
                print ("Saliendo del programa...")
                #Usamos la función importada. Pausa el programa por 1.5 segundos.
                time.sleep(1.5)
                break; #Rompe el bucle 'while True' del MENÚ y termina.
            
            #Opción Inválida: Si ingresa un número que no es 1, 2 o 3.
            else:
                print("!Ingresa una opcion¡");
    
    #Manejo de error del menú (si 'int(input...)' falla).
    except:
        print("Error: !Ingresa una opcion valida¡")
        return #Termina el programa.

#--- Ejecución del Programa ---
#Esta es la línea que inicia todo. Llama a la función 'main'.
main()
