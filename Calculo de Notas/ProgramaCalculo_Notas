import time

def calcular_promedio_ponderado():
    while True:
        try:
            cantidad_notas_str = input("¿Cuántas notas vas a ingresar?: ").strip()
            cantidad_notas = int(cantidad_notas_str)

            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return

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
                    return

                porcentajes.append(porcentaje)
                porcentaje_acumulado += porcentaje
                
            except:
                print("Error: Ingresa un número válido para el porcentaje.")
                return

        print("\n-----------------------------------------")
        print(f"Suma total de porcentajes ingresados: {round(porcentaje_acumulado)}%")

        if round(porcentaje_acumulado) != 100.0:
            print("¡ERROR! Los porcentajes no suman 100%.")
            print("Por favor, vuelve a ejecutar el programa con los porcentajes correctos.")
            return 

        print("¡Configuración correcta! Los porcentajes suman 100%.")
        print("-----------------------------------------")

        print("\n--- 2. Ingreso de Notas ---")
        nota_final_ponderada = 0.0

        for i in range(cantidad_notas):
            try:
                porcentaje_de_esta_nota = porcentajes[i]

                nota_str = input(f" Ingresa la Nota {i + 1} (que vale un {porcentaje_de_esta_nota}%): ").strip().replace(',', '.')
                nota = float(nota_str)

                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return

                peso_decimal = porcentaje_de_esta_nota / 100.0
                contribucion = nota * peso_decimal

                nota_final_ponderada += contribucion

                print(f" -> Esta nota aporta {contribucion:.2f} puntos a tu promedio.")

            except:
                print("Error: Ingresa un número válido para la nota.")
                return

        print("\n--- Cálculo Finalizado ---")
        print(f"Tu Nota Final Ponderada es: {round(nota_final_ponderada,1)}")
        break;


def promedio_notas():
    while True:
        try:
            cantidad_notas = int(input("¿Cuántas notas vas a ingresar?: "))

            if cantidad_notas <= 0:
                print("Error: Debes ingresar al menos una nota.")
                return
        except:
            print("Error: Ingresa un número entero válido (ej: 4).")
            return
        
        ListaNotas = []
        print("\n--- 2. Ingreso de Notas ---")

        for i in range(cantidad_notas):
            try:

                nota = float(input(f" Ingresa la Nota {i + 1}: "))

                if (nota < 1 or nota > 7.0):
                    print("Error: La nota debe ser entre 1.0 y 7.0")
                    return

                ListaNotas.append(nota)

            except:
                print("Error: Ingresa un número válido para la nota.")
                return

        print("\n--- Cálculo Finalizado ---")
        resultadoPromedio = sum(ListaNotas)/ cantidad_notas
        print(f"Tu Nota Final Promediada es: {round(resultadoPromedio,1)}")
        break;
        

def main ():
    try:
        while True:
            print ("-"*142)
            print ("="*55,'Bienvenido al calculo de notas',"="*55)
            print ("-"*142)

            print ("="*68, 'MENÚ', "="*68)
            print ("-"*142)
            print ("-"*12,"Opcion 1. Ingreso de notas Ponderadas   |    Opcion 2. Ingreso de notas Promedio   |    Opcion 3. Salir del Programa","-"*12)
            print ("-"*142)

            print("")
            r = int(input("Ingrese una opcion (1,2 o 3): "))
            print("")
            
            if r==1:
                print ("*"*61,"!Notas Ponderadas¡","*"*61)
                calcular_promedio_ponderado()

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

            elif r==2:
                print ("*"*61,"!Notas Promediadas¡","*"*60)

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

            elif r == 3:
                print ("Saliendo del programa...")
                time.sleep(1.5)
                break;
            
            else:
                print("!Ingresa una opcion¡");
    
    except:
        print("Error: !Ingresa una opcion valida¡")
        return

main()
