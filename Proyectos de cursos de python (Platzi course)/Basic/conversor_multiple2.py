def conversor(tipo_pesos, valor_dolar):
    pesos = input("ΒΏCuantos pesos " + tipo_pesos +  " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares ")  

menu = """
Bienvenido al Conversor de monedas π±

1 - Pesos colombianos ππβ€
2 - Pesos argentinos ππ€π
3 - Pesos mexicanos ππ€β€

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombianos", 3689)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Opcion no valida, Por favor ingresa un valor entre (1-2-3)")
