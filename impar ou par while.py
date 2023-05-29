while True:
    numero = int(input("Digite um número inteiro (ou um valor negativo para sair): "))
    
    if numero < 0:
        print("Programa encerrado.")
        break
    
    if numero % 2 == 0:
        print("O número", numero, "é par.")
    else:
        print("O número", numero, "é ímpar.")

