#=============================EESTRUTURAS CONDICIONAIS=============================
#Funcionam como estruturas de controle de fluxo, determinam um condição para
#execução de um bloco de código
#Essa estruturas são: "if", "elif" , "else"

#------------------------------------- IF ------------------------------------------
#o if("se" em português), como dito define um condição pra chamada de determinado
#bloco de código, exemplo:
saldo = 1000
saque = 300

if saque <= saldo:
    print("É possível sacar")

#percebe-se que o saque não se adequa a essa condição, portanto não irá fazer a execução do print

if saque >= saldo:
    print("Não é possível sacar")

#------------------------------------- elif ------------------------------------------
#o "elif" determina uma condição se a condição antes dela não for satisfeita
#Exemplo:
saque = 1001

if saque <= saldo: #não entra
    print("É possível sacar")
elif saque >= saldo: #entra, e so passa por ela se não entrar na primeira
    print("Não é possível sacar")

saque = 300

if saque <= saldo: #entra
    print("É possível sacar")
if saque >= saldo: #não entra
     print("Não é possível sacar")

# Nesse caso, o valor se adequa a primeira condição, porém
#ele também irá ler a segunda condição, diferente do primeiro
#exemplo que só faz a leitura se não passar pela primeira condição

#------------------------------------- else --------------------------------------------
#o "else" permite que um bloco de codigo seja executado sem a necessidade de passar uma condição
#é usado depois de uma estrutura que tenha um condição
#Exemplo:

saque = 1001

if saque <= saldo: #entra
    print("É possível sacar")
else: #qualquer valor que não seja menor igual a saldo, entra no else
    print("Não é possível sacar")

#podemos usar as 3 estruturas em conjunto como, por exemplo:

saque = 1501

if saque <= saldo: #não entra
    print("É possível sacar") 
elif saque >= saldo and saque <= 1500: #não entra
     print("Não é possível sacar")
else: #entra
    print("Erro ao tentar sacar")

#-----------------------------------------ANINHAR ESTRUTURAS-------------------------------------
#É possível aninhar as estruturas usar "if/elif/else" dentro de "if/elif/else"

tipo_conta = int(input("Qual seu tipo de conta? corrente [1] poupanca [2]\n"))

if tipo_conta == 1:
    acao = int(input("O que deseja fazer? transferir[1] sacar[2]\n"))
    if acao == 1:
        print("fazer transferencia")
    elif acao == 2:
        print("fazer saque")

elif tipo_conta == 2:
    acao = int(input("O que deseja fazer? transferir[1] depositar[2]\n"))
    if acao == 1:
        print("fazer transferencia")
    elif acao == 2:
        print("fazer deposito")

else:
    print("valor não aceito")

#-----------------------------------------IF TERNÁRIO-------------------------------------
#A condição é feita dentro de uma única linha nesse formato: retorno = (ação) if (condição) else (ação)
#Exemplo

retorno = "É maior" if 3>=2 else  "É menor"
print(retorno)
#output
#É maior

valor = 15 

par = "Par" if valor%2 == 0 else "Ímpar" 
print(par)
#output
#Ímpar
