from modulos import conversor

temperatura = float(input("Digite uma temperatura: "))
unidade = input("Qual a unidade de medida (c ou f): ")

if unidade == "c":
    resultado = conversor.celsius(temperatura)
elif unidade == "f":
    resultado = conversor.fahrenheit(temperatura)
else:
    print("Unidade inserida não identificada")

print("Temperatura convertida em", unidade, "igual a", resultado)
