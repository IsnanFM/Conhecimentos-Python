#=================================OPERADORE IDENTIDADE===============================
#O operador de identidade em Python é "is" e ele verifica se duas variáveis ocupam 
#o mesmo espaço na memória, vamos fazer um exemplo.

saldo = 1000 #atribuição do valor numérico 1000 a variável saldo
saldo1 = saldo # atribuição da variável saldo na variável saldo1

print(saldo1 is saldo)

#Verificamos que sim, as duas variáveis ocupam a mesma posição na memória
#output
#True

saldo = 1000
saldo1 = 1000

print(saldo1 is saldo)

#Aqui também verificamos que sim, as duas variáveis ocupam a mesma posição na memória
#output
#True

saldo = 1000
saldo1 = 1000.0

print(saldo1 is saldo)

#Aqui verificamos que apesar das duas variáveis tenham o "mesmo" valor 
#o resultado é falso pois saldo1 é do tipo float

#output
#False

#Também podemos usar o "not" em conjunto com "is"

saldo = 1000
saldo1 = saldo 

print(saldo1 is not saldo) #verificar se eles não ocupam a mesma posição na memória

#output
#False pois eles são da mesma região de memória