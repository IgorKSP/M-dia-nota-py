produto = float(input("valor do produto é: R$ "))

print("Formas de pagamento")
print("1. à vista dinehiro ou débito")
print("2. à vista cartão de crédito")
print("3. em duas vezes")
print("4. em duas vezes com juros")

escolha = float(input("escolha a forma de pagamento: "))


if (escolha == 1) :
    valor = produto * 0.85
    print(f"valor a pagar: R${valor:.2f} ")
elif(escolha == 2):
    valor = produto * 0.93
    print(f"valor a pagar: R${valor:.2f} ")
elif (escolha == 3):
    valor = produto/2
    print(f"valor a pagar: 2x de R${valor:.2f} ")
elif( escolha == 4):
    valor = (produto * 1.10)/2
    print(f"valor a pagar: 2x de R${valor:.2f} ")
else: 
    print("forma de opagamento invalida")
