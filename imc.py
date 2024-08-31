peso = float(input("peso: "))
altura = float(input("altura: "))

imc = peso / (altura ** 2)

print(f"seu imc é: {imc:.2f}")

def classificar_imc(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc < 25:
        return "no peso normal"
    elif imc < 30:
        return "acima do peso"
    else:
        return "obeso"

print(f"Você está {classificar_imc(imc)}.")


#    def medidor1():
#        frase1 = "abaixo do peso" if imc < 18.5 else "no peso normal"
#        print("você está", frase1)
#
#   def medidor2():
#       frase2 = "acima do peso" if imc < 30 else "obeso"
#       print("você esta", frase2)
#
#   if (imc < 25):
#       medidor1()
#   else:
#       medidor2()
