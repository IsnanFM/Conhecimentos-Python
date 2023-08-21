#================================FUNÇÕES ENTRADA E SAÍDA======================================

#--------------------------------------ENTRADA---------------------------------------

# Exisem duas funções principais pra entrada e sáida
# Primeiro a "input()" e podemos exibir uma mensagem passada por parâmetro
var1 = input("digite um valor \n")
var = int(input("digite um valor \n")) + 10

#output: "digite um valor"
#o valor digitado no input foi "4" nas duas ocasiões, portanto o valor gravado em "var"

#------------------------------------SÁIDA---------------------------------------------

#A segunda função (saída) é a função "print()" , podemos passar basicamente qualquer coisa como parâmetro
#será exibido no terminal 
#Por exemplo

print(var)
print(var1)

#output:
#4
#14

#podemos tambem

print(type(var))
print("mensagem qualquer") #quebra de linha por padrão
print("mensagem qualquer", end= ".\n" )
print("mensagem","qualquer", sep="-")
print(34 + 25)
print(var1,var)

#output:
#<class 'int'>
#mensagem qualquer
#mensagem qualquer.
#mensagem-qualquer
#59
#4 14