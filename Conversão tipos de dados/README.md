
# Conversão de tipos

- A conversão é necessária quando, por exemplo, quisermos fazer uma operação com dois tipos de dados
totalmente diferentes.

|Tipo de dado|conversor|
|--------------|-----------|
|int|_int()_|
|float|_float()_|
|bool|_bool()_|
|string|_str()_|
|tupla|_tuple()_|
|lista|_list()_|

* Esses são os principais tipos e conversões usados no python.

Agora vamos à um exemplo de uso:

Em python quando fazemos a soma de str + int, mesmo que a string seja uma representação de um inteiro, isso retorna um erro. Ex:

```
var_string = "10"
var_int = 10

print(var_int + var_string)

#output

TypeError: unsupported operand type(s) for +: 'int' and 'str'
```
Portanto devemos fazer a conversão de "10" que é do tipo <b>string</b> para o tipo <b>inteiro</b>
```
var_string = "10"
var_int = 10
var_convertida = int(var_string) #conversão

print(var_int + var_convertida)

#output

20

```
## Ocorrência de outros tipos
- Isso se dá também em outros tipos de dados:
    * <b>int -> float (float -> int)</b>
    * <b>int -> str (str -> int)</b>
    * <b>list -> tuple (tuple -> list)</b>
Ainda existe também <b>complex()</b>

## Conversão implícita
Se temos por exemplo um <b>flutuante</b> e um <b>inteiro</b> e quisermos somar os dois não precisaríamos converter qualquer um dos, o _Pyhton_ consegue fazer essa conversão em tempo de execução.

Ex
```
var_int = 5
var_float = 6.0
print(type(var_int), type(var_float))

#output

<class 'int'> <class 'float'>

#vamos fazer a soma dos dois

soma = var_int + var_float

print(soma)

print(type(soma))

#output

11.0
<class 'float'>
```
Vimos que ele identifica e faz essa conversão de tipo automaticamente.

## 📕Documentação
- https://docs.python.org/3/
## 📚 Referências
- https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3-pt
- https://blog.grancursosonline.com.br/conversoes-e-casting-de-tipos-de-dados-em-python/
