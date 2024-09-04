print("SOMA")
while True:
    a=bool(input("Digite qualquer caractere para continuar o programa ou enter para encerrá-lo. "))
    if a==True:
        x=float(input("Insira o primeiro valor: "))
        y=float(input("Insira o segundo valor: "))
        print(f"A soma de {x} com {y} é igual a {x+y}.")
        continue
    else:
        print("Encerrando o programa...")
        break