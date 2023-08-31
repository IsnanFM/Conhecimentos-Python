#=============================ESTRUTURAS DE REPETIÇÃO=============================
#As estruturas de repetição servem pra iterar sobre determinado bloco
#de acordo com uma condição dada.
#As duas estruturas são: "for" e "while"

#--------------------------------- for -------------------------------------------
#Para exemplificar o uso da estrutura, vamos supor que queremos "printar" uma
#determinada sequência de 0 a 20, podemos fazer um a um ou podemos usar a estrutura
#de repetição, exemplo:

for i in range(21): # 0 a 20 são 21 elementos
    print(i , end = " ")
else:    
    print() #quebra de linha e executa no final do laço

#identificando vogais em um texto
texto = "aqui é um texto"
vogais = "aeiou"

for i, letra in enumerate(texto):#o enumerate serve para enumerar o texto, o indice é alocado em "i"
    if letra in vogais:
        print("vogal", letra, "encontrada na posição", i)

print(list(range(10))) #0 inclusivo e ultimo elemento exclusivo, o 10 não entra na lista

for par in range(0,55,2):
    print(par, end = " ")
else:
    print()

#--------------------------------- While -------------------------------------------
#O while é usado da mesma forma que o for e inclusive podem desempenhar o mesmos papéis
#Ex:
#impressão de 0 a 10

i = 0
while i <= 10:
    print(i, end = " ")
    i+=1
else:
    print()

#impressão de valores até a digitação do "0"
valor = -1
while valor != 0:
    valor = int(input("Digite um inteiro\n"))
    print("Valor digitado foi:", valor)
    print()
else:
    print("fim do laço")

#--------------------------------- Uso do BREAK -------------------------------------------

valor = -1
while True:
    valor = int(input("Digite um inteiro\n"))
    print("Valor digitado foi:", valor)
    print()
    if valor == 0: #saida do laco se o valor for igual a 0
        print("")
        break
