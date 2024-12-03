"""
Estruturas condicionais 
If, else, elif

If = Se

Else = Senão (usada para confirmar que o 'If' é falso)

Elif = É uma abreviação de “else if” e permite verificar múltiplas condições em um programa

"""

idade = 20


if idade < 17:    
    print('Menor de idade')

elif idade == 18:
    print('tem 18 anos')

else:
    print('Maior de idade')


"""
Estruturas Lógicas : AND (e), or (ou)n not(não), is (é)

Operadores unarios:
    - not, is
Opreadores binários
    - and,or

# Regra para funcionamento 
Para o 'and', ambos os valores precism ser True (verdadeiro)
Para o 'or', apenas um dos valores precisa ser True (verdadeiro)
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False
se for False, vira True - Ele nega o resultado
"""
ativo = True
logado= False

if ativo and logado:
    print('Bem vindo')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Exemplo
print(not False)

"""
Exercicios
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule 
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o 
número é inválido.
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar
"""

# 1-)

num1: int = input(print("Por favor indique o primeiro número inteiro:"))
num2: int = input(print('Por favor indique o segundo número inteiro:'))

if num1 > num2:
    print(f"O {num1} é maior que o num{2}")
elif num1 == num2:
    print(f"Os números {num1} e {num2} são iguais")
else:
    print(f"O {num2} é maior que o {num1}") 

# 2-)

numero1= int(input(print('Forneça o primeiro número:')))
#numero1 = int(numero1)

if numero1 > 0:
    soma: int = (numero1 * numero1)
    print(f'A raiz quadrada é {soma}')
else:
    print("Número invalido, por favor forneça um número positivo")

# 3-)

number1 = int(input(print('Forneça um número inteiro')))

if number1 % 2 == 0:
    print(f'Número {number1} par')
else:
    print(f"O número {number1} é impar")
    

    

