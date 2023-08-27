#===========================OPERADORES DE ASSOCIAÇÃO=================================
#Os operadores de associação são usados para verificar se um elemento está
#em uma determinada sequência
#Exemplo:

string = "Python é uma linguagem"

print("Python" in string) #verificando se a substring está dentro da string principal

#output:
#True

frutas = ["uva","maça","pera","ameixa"]

print("Ameixa" in frutas)
#output:
#False

print("ameixa" in frutas)
#output:
#True

print("ameixa" not in frutas)
#output:
#False
