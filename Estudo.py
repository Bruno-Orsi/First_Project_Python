"""
Tipo Float

Tipo real, decimal

Separador de casas decimais na programação é o ponto e não a virgúla.
"""

# Errado quando está buscando float
Valor = 1, 44
print(type(Valor))  # Tuple/Tupla


# Certo quando busca float
Valor = 1.44
print(type(Valor))  # Float

# É possivel fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(valor2)

# Podemos converter um float para um int
"""
Ao converter valores float para inteiros, nós perdemos a precisão( no caso era 1.44 e virou apenas 1)
"""
res = int(Valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
print(type(5j))
vars = 5j
print(type(vars))


"""
Algébra Booleana,criada por George Boole

2 constatnes, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso
"""

ativo = True

print(ativo)

"""
Negação (not)
Fazendo negação, se o valor vooleano for verdadeiro o resultado será falso.
Ou seja, sempre o contrário
"""
print(not ativo)

"""
Ou (or)
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or False -> False
"""
logado = False

print(ativo or logado)

"""
E (and) - Também é uma operação binária, ou seja, depende de dois valores. Ambos os
valores devem ser verdadeiros.

True and True -> True
False and False -> True
True and False -> False
"""

# Para deixar a palavra/frase para maiúsculo -> 'upper' - para minusculo -> 'lower'

"""
Escopo de variáveis

 Dois cassos de escopo:

 1 - Variáveis globais;
    - Variáeis globais são reconhecidas por todo o programa

 2 - Variáveis locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada   
 """
"""
Exercicios para praticar

1 - Faça um programa que leia um número inteiro e imprima-o

2 - Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles

3 -  Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos
"""
# 1-) 
numero: int = int(input("Informe um número inteiro:"))

print(numero)

# 2-)

print("Informe 3 números inteiros:")

num1: int = int(input("1 número inteiro:"))

num2: int = int(input("2 número inteiro:"))

num3: int = int(input("3 número inteiro:"))

soma = int(num1 + num2 + num3)

print(f" A soma dos números {num1}, {num2}, {num3} é de {soma}")


# 3-)

print("informe 3 números inteiros:")

numero1: int = int(input('Informe o primeiro número:'))

numero2: int = int(input('Informe o segundo número:'))

numero3: int = int(input('Informe o terceiro número:'))

soma: int = (numero1 * numero1) + (numero2 * numero2) + (numero3 * numero3)

print(f" a soma dos quadrados dos números {numero1} com {numero2} e {numero3} é {soma}") 



