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






