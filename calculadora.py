import msvcrt
def avance ():
    print ("")
    print ("Presione alguna tecla para continuar.")
    print ("")
    tecla = msvcrt.getch()
    print ("")


def calculo (n1, n2, op):
    print ("")
    if op == 1:
        r = n1 + n2
        s = "+"
        print (f"El resultado de la suma es : {n1} + {n2} = {r}") 
    elif op == 2:
        r = n1 - n2
        s = "-"
        print (f"El resultado de la resta es : {n1} - {n2} = {r}")
    elif op == 3:
        r = n1 * n2
        s = "*"
        print (f"El resultado de la multiplicación es : {n1} * {n2} = {r}")
    else:
        if n2 != 0:
            r = n1 / n2
            s = "/"
            print (f"El resultado de la división es : {n1} / {n2} = {r}")
        else:
            print ("No es posible dividir por cero.")
    avance()
    historial.append((n1, s, n2, "=", r))
historial = []
while True:
    print ("¿Qué quiere hacer?")
    print ("1-Suma")
    print ("2-Resta")
    print ("3-Multiplicación")
    print ("4-División")
    print ("5-Historial")
    print ("6-Salir")
    try:
        op = int(input(""))
    except ValueError:
        print("Entrada inválida.")
        continue
    if op>6 or op<1:
        print ("Opción inválida.")
        avance()
    elif op == 6:
        print ("Gracias por usar la calculadora.")
        break
    elif op == 5:
        if len(historial) == 0:
            print("No hay operaciones todavía.")
        else:
            print("\nHistorial:")
            for item in historial:
                print(item)
        avance()
    else:
        print ("Ingresa el primer número.")
        n1 = int(input(""))
        print ("Ingresa el segundo número.")
        n2 = int(input(""))
        calculo(n1, n2, op)