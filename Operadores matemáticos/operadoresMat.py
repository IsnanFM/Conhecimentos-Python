#=================================OPERADORES MATEMÁTICOS===============================

#Os operadores em python tem a função de fazer contas usuais de matemática
#Por exemplo, adição, subtração, multiplicação, divisão, potência, raiz...e assim por diante
#Irei abordar os principais operadores
#--------------------------------------ADIÇÃO e SUBTRAÇÃO------------------------------------------
#O operador de adição tem como o símbolo o "+" e é uma operação binária.
#Assim como a subtração e tem como símbolo "-"
#Alguns exemplos:

A = 1
B = 34
print(A+B)
print(B-A)
#output:
# 35
# 33

#podemos fazer a operação diretamente no print
print(34+1)
print(34-1)
#output:
# 35
# 33

#--------------------------------------MULTIPLICAÇÃO e DIVISÂO------------------------------------------
#O operador de multiplicação tem como o símbolo o "*" e é uma operação binária.
#Assim como a divisão e tem como símbolo "/" e "//" para divisões inteiras
#Segue as regras matemáticas usuais

print(A*B)
print(34*1)
print(B/A)
print(34/1)
print(34//1)
#output:
# 34
# 34
# 34
# 34.0

#Assim como na matemática podemos mesclar os operadores, e eles teram níveis de
#precedência diferentes

#a*b+c/d => mult e div => adição e sub

#--------------------------------------POTÊNCIA------------------------------------------
#O operador de potência tem como símbolo "**" e "base**expoente"

A=2
B=3
potencia = A**B
print(potencia)

#--------------------------------------RAIZ------------------------------------------

#para fazer raiz quadrada vamos ter que importar uma biblioteca chamada math

import math

#assim usando math e seu metodo sqr podemos tirar raiz

A=25
raiz_a = math.sqrt(A)
print(int(raiz_a))

#output
#5

#ESSE SÃO OS PRINCIPAIS OPERADORES MATEMÁTICOS E PODEMOS USAR COMO BEM ENTENDERMOS
#SIMULAR EXPRESSÕES MATEMÁTICAS TAMBÉM É POSSÍVEL.
#NO PYTHON TAMBÉM SE APLICA "()" PARA PRECEDÊNCIA. PORÉM, NÃO PODEMOS USAR "[]","{}"
#QUE SÃO REFERENTES A LISTAS E COLEÇÕES.