#===========================OPERADORES DE ATRIBUIÇÃO=================================

#Os operadores de atribuição são usados para inserir valores em variáveis
#São os operadores: "=", "+=", "-=", "/=", "//=", "%=", "**="

#------------------------------ATIBUIÇÃO SIMPLES (=)--------------------------------------
#É o mais simples entre os operadores e é o mais fácil de ser entendido

saldo = 1000
saldo = 900 #Aqui ele sobrepõe o valor contido na variável

#------------------------------ATIBUIÇÃO COM ADIÇÃO (+=)--------------------------------------
#Funciona como o simples porém antes de atribuir ele soma um determinado valor 

saldo += 100
print(saldo)

#output
#1000

#------------------------------ATIBUIÇÃO COM SUBTRAÇÃO (-=)-------------------------------------
#Funciona como o simples porém antes de atribuir ele subtrai um determinado valor

saldo -= 100
print(saldo)

#output
#900

#------------------------------ATIBUIÇÃO COM DIVISÃO (/=) e (//=) -------------------------------------
#Funciona como o simples porém antes de atribuir ele divide por um determinado valor

saldo = 1000

saldo /= 100
print(saldo)

saldo = 1000

saldo //= 100
print(saldo)

#output
#10.0 (flutuante)
#10   (Inteiro)

#------------------------------ATIBUIÇÃO COM RESTO (%=) -------------------------------------
#Funciona como o simples porém antes de atribuir ele divide por um determinado valor e atribui
#o resto a variável

saldo %= 2 #saldo = 10, resto da divisão por 2 é igual a 0
print(saldo)

saldo = 1000

saldo %= 3 #resto da divisão de 1000 por 3
print(saldo)

#output
#0
#1

#------------------------------ATIBUIÇÃO COM EXPONENCIAÇÃO (**=) -------------------------------------
#Funciona como o simples porém antes de atribuir ele usar o valor passado como expoente do valor
#guardado da variável

saldo = 3
saldo **= 2 #vai usar 3 como base e 2 como expoente
print(saldo)

#output
#9