#===================================OPERADORES LOGICOS==========================
#São usados com operadores de comparação e retornará um valor booleano
#Alguns dos operadores são: "and" ou "&", "or" ou "|", "not"(negação) e "()" parênteses 

#-------------------------------------operador E ---------------------------------------
#O operador "E", é usado pra comparar dois termos lógicos. Esse operador só retorna True
#se as duas operações forem True
#Ex:

saldo = 1000
limite = 10000
saque = 800

booleano = saque <= saldo and limite >= saldo # (True) and (True) = True
print(booleano) #True

saldo = 1000
limite = 10000
saque = 1001

booleano = saque <= saldo and limite >= saldo# (False) and (True) = False
print(booleano) #False

#output
#True
#False

#-------------------------------------operador OU ---------------------------------------
#O operador "OU", é usado pra comparar dois termos lógicos. Esse operador retorna True
#se uma das duas operações forem True e retorna False se as duas operações forem False
#Ex:

saldo = 1000
limite = 10000
saque = 800

booleano = saque <= saldo or limite >= saldo# (False) and (True) = True

print(booleano)
#output
#True

limite = 100
saque = 1001

booleano = saque <= saldo or limite >= saldo # (False) and (False) = False

print(booleano)
#output
#False

#-------------------------------------operador negação(not) ---------------------------------------
#esse operador inverte os valores de um termo booleano
#Por exemplo:
#booleano = saque <= saldo and limite >= saldo # (False) and (False) = False
#Aqui deu False considerando os valores das variáveis:
#saldo = 1000
#limite = 100
#saque = 1001
#Porém se usarmos o "not"

booleano = not saque <= saldo or limite >= saldo # (True) and (False) = True
booleano = saque <= saldo or not limite >= saldo # (False) and (True) = True
booleano = not saque <= saldo or not limite >= saldo # (False) and (False) = False

#output:
#True
#True
#False

#-------------------------------------PARÊNTESES "()" ---------------------------------------
#Os parênteses indicam precedência e são prioridade na operação
#Ex:

saldo = 1000
limite = 10000
saque = 800

booleano = (saque <= saldo) and (limite <= saldo) or (saque!=800) #(True) and (False) or (False) = False
booleano = not ((saque <= saldo) and (limite <= saldo) or (saque!=800))# not((True) and (False) or (False)) = True
#Aqui devemos usar o parênteses na expressão toda pra aplicá-lo no resultado final
print(booleano)

#O parênteses também é usado em expressões matemáticas, também define precedência

ex = 2 * 3 + 4 // 2  #nesse exemplo o resultado é igual a 8
ex = 2 * (3 + 4) // 2 #nesse o resultado é 7
print(ex)