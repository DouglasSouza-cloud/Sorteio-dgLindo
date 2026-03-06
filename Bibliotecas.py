import random
import math
import datetime
import time

nums = []

def media():  # Função para calc. média;
    b = sum(nums) / len(nums)
    print(b)

def maior():  # Função para pegar o maior valor;
    a = max(nums)
    print(a)

def menor():  # Função para pegar o menor valor;
    c = min(nums)
    print(c)






while True:
        
        print("\n=== Bem vindo ao Sorteio ====\n")
        
        try:
            qtd = int(input("Quantos números deseja sortear?: "))

            for i in range (qtd):
                while True:
                    if qtd < 0:
                        print("Número Negativo não né man...")
                    else:

                        num = random.randint(1, 100)
                        nums.append(num)


            print("\nOs números sorteados foram: ", nums)
            print("\nO maior número sorteado foi: ")
            maior()
            print("\nO menor número sorteado foi: ")
            menor()
            print("\nA média dos números sorteados é: ")
            media()

            ref = str(input("\nDeseja refazer? s/n: \n"))  # Decisão do usuário de refazer ou não.

            if ref == "s":  # Condição
                print("Reiniciando Sorteio...")
                time.sleep(2)  # Aguarda 2 segundos antes de reiniciar

            elif ref == "n":
                print("Sorteio finalizado finalizado.")
                break  # Para o programa quando a condição for correspondida.
        except ValueError:
             print("Digito inválido, digite novamente...")
              


