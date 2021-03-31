import time


def checkValue(operation):                      #Verifica que el valor esté en el rango admitido en cada operación, y que no sea un string
    #Operation range.
    #0. Nivel
    #1. Stat
    #2. Hit die
    #3. Skill
    while True:
        try: 
            ingress = input()
            ingress = int(ingress)
            if operation == 0:        #Nivel
                if ingress >= 1 and ingress <= 20:
                    return ingress
                else: 
                    print("Tu nivel debe estar entre 1 y 20.")
            
            elif operation == 1:      #Stat
                if ingress >= -6 and ingress <= 10:
                    return ingress
                else:
                    print("Tu valor debe estar entre -6 y 10.")
            
            elif operation == 2:      #Hit die
                if ingress == 6 or ingress == 8 or ingress == 10 or ingress == 12:
                    return ingress
                else: 
                    print("Tu valor debe ser 6, 8, 10 ó 12.")

            elif operation == 3:      #Skill
                if ingress >= 0 and ingress <= 18:
                    return ingress
                else:
                    print("Debe ser un número entre 0 y 18.")

        except ValueError:
            print("Error. Ingrese un valor numérico.")


def waitCalculation():
    print("Calculando", end="", flush = True)
    for i in range(3):
        print(".", end="", flush = True)
        time.sleep(1)
    print("\n")