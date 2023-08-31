#=============================INTERPOLAÇÃO DE VARIÁVEIS==========================

#--------------------------------Velha forma (%)---------------------------------
nome= "Isnan"
idade = 23
curso = "python"
print("Olá eu sou %s tenho %d anos e estou aprendendo %s" % (nome,idade,curso))
#Olá eu sou Isnan tenho 23 anos e estou aprendendo python

#-----------------------------------Format---------------------------------------
nome= "Isnan"
idade = 23
curso = "python"

print("Olá eu sou {} tenho {} anos e estou aprendendo {}".format(nome,idade,curso))
#Olá eu sou Isnan tenho 23 anos e estou aprendendo python

print("Olá eu sou {1} tenho {0} anos e estou aprendendo {2}".format(nome,idade,curso))
#Olá eu sou 23 tenho Isnan e estou aprendendo python

print("Olá eu sou {nome} tenho {idade} anos e estou aprendendo {curso}".format(nome= nome, idade= idade, curso = curso))
#Olá eu sou Isnan tenho 23 anos e estou aprendendo python

#-----------------------------------f-string---------------------------------------
nome= "Isnan"
idade = 23
curso = "python"

print(f"Olá eu sou {nome} tenho {idade} anos e estou aprendendo {curso}")
#Olá eu sou Isnan tenho 23 anos e estou aprendendo python

#----------------------------formatando com f-string------------------------------
PI = 3.14159

print(f"Valor de PI: {PI:.3f}")
#Valor de PI: 3.142
print(f"Valor de PI: {PI:6.3f}") #adiciona 6 espacos em branco
#Valor de PI:  3.142