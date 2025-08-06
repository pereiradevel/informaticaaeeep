#Questao 1. Escreva um programa que imprima os números de 1 a 10 usando o for.
#for numero in range(1, 11):
 #print(numero)
 
#Questao 2. Escreva um programa que imprima os números de 10 a 1 usando while.
#while numero >= 1:
  #print(numero)
  #numero -= 1
  
#Questao 3. Crie um programa que pergunte o nome do usuário e o imprima 5 vezes.
#ome = input("Qual seu nome?: ")
#for _ in range(5):
  #print(nome)
  
#Questao 4. Imprima os números pares de 0 a 20 usando for com range().
#for numero in range(0,21,2):
    #print(numero)

#Questao 5. Crie um programa que pergunte ao usuário uma senha e só saia do loop se ele digitar 1234.
#while True:
    #senha = input("Digite a senha: ")
    #if senha == "1234":
        #print("Senha correta! Acesso liberado.")
        #break
    #else:
        #print("Senha incorreta. Tente novamente.")


#Questao 6. Crie um programa que peça 5 números e imprima a soma total.
#soma = 0
#for i in range(5):
    #numero = int(input(f"Digite o {i+1}º número: "))
    #soma = soma + numero
#print(f"A soma total é: {soma}")

#Questao 7. Use o continue para pular a impressão de números ímpares entre 1 e 10.
#for numero in range(1, 11,2):
    #print(numero)
    
#Questao 8. Crie um programa que leia números do usuário até que ele digite 0. Depois mostre quantos números foram digitados.

#contador = 0
#while True:
   # numero = int(input("Digite um número (digite 0 para sair): "))
   # if numero == 0:
       # break
    #contador = contador + 1

#print(f"Você digitou {contador} números.")    

#Questao 9. Faça um programa que imprima a tabuada de um número informado pelo usuário
#numero = int(input("Digite um número para ver a tabuada: "))

#print(f"Tabuada de {numero}:")

#for i in range(1, 11):
    #resultado = numero * i
    #print(f"{numero} x {i} = {resultado}")