# Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.

# Escreva um código que imprima todos os números exceto o número 13.
# Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.

# Como desafio, imprima eles em ordem decrescente (20, 19, 18...)




# numero = 20
for i in range(20):
    numero = numero -1
    if (numero == 13):
        continue
    if (numero ==0):
        break
    print(numero)


#Usando o metodo while



i = 0
while (i < 20):
    i = i + 1
    if (i == 13):
        continue
    if (i == 20):
        break
    print(i)

