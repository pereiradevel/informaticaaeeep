
def menu():
    while True:
        print("Bem vindo a lista 3")
        print("Escolha uma das opções.")
        print("[1] Cálculo do IMC")
        print("[2] Números Pares e Ímpares até N:")
        print("[3] Tabuada Personalizada:")
        print("[4] Verificação de Número Primo:")
        print("[5] Soma de Notas e Média:")
        print("[6] Jogo do Número Secreto:")
        
        
        op = input("Escolha uma opção:")


        if op == 1:
            print("Cálculo do IMC")
            peso = float(input("Digite seu peso:"))
            altura = float(input("Digite sua altura:"))
            imc = (peso) / (altura) * altura
            if imc < 18.5:
                print("Abaixo do peso")
        for imc in range(18.5,24.9):
            print( "Peso normal")
        for imc in range(25,29.9):
            print("Sobrepeso")
        if imc > 30:
            print("Obesidade")
            
menu()