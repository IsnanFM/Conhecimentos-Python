#============================================== VARIÁVEIS============================================

#em Python não se precisa declarar o tipo de dados, como em outras linguagens, a exemplo de C/C++

#Portanto podemos escolher o nome da nossa variável que o python irá se resposabilizar de reconhecer
#o tipo de dados inserido

minha_var = 10

#----------------------------------------------------------------------------------------#
print(type(minha_var)) #output: <class 'int'>

#A mesma variável pode ser usada para receber uma string por exemplo

minha_var = "essa é uma string"

print(type(minha_var)) #output: <class 'str'>

#----------------------------------------------------------------------------------------#
#Lista

minha_var = ['a', 'b', 'c']
minha_var = ['LUIS', 'FERNANDO', 'ISNAN']
minha_var = [23,421,415,546,123]


#----------------------------------------------------------------------------------------#
#Booleano

minha_var = True #ou minha_var = 1(ou qualquer inteiro, ele reconhece como True)c porém teremos que usar o parse "bool()"

print(minha_var) #output: True

minha_var = bool(0) #ou False

print(minha_var)
#============================================== CONSTANTES ============================================

#Diferente de outra linguagens o pyhton não tem constantes
#Porém como convenção dos programadores se a variável está toda em UPPER_CASE(MAIUSCULO)
#ela é considerada como uma constante e não poderá ser mudada

CONSTANTE = 1000
STATES = [
    'SP',
    'RJ',
    'BA'
]

#essas são consideradas variáveis e por convenção NÃO são mutáveis

#============================================== BOAS PRÁTICAS ============================================

#Em python por convenção também devemos usar o padrão SNAKE_CASE , que por sua ver é 'desse_tipo'

saldo_em_conta = 1000
estados_brasil = ['BA', 'SP']
