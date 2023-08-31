#===============================METODOS STRING==================================

#-------------------------Maiúscula, minúscula e título-------------------------
curso = 'pYtHoN'
print(curso.upper())
#PYHTON
print(curso.lower())
#python
print(curso.title()) # Coloca a string minúscula e o primeiro caracter maiusculo
#Python     

#-----------------------------Espaços em branco----------------------------
curso = "  python    "
print(curso.strip())
#"pyhton"
print(curso.lstrip()) # Retirando espaços da esquerda
#"pyhton   "
print(curso.rstrip()) # Retirando espaços da direita
#"  python"

#-----------------------------Junções e centralização----------------------------
curso = "python"
print(curso.center(10,"*"))
#**python**
print("-".join(curso))
#p-y-t-h-o-n
curso = "Python"                                                     
print(f"Bem vindo ao curso de {curso.upper()}!")