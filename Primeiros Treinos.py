#contagem de quantas PALAVRAS existe na string
palavra = 'Banana Naninca'
contagem = 0 
for letter in palavra:
  if letter == 'a':
    contagem = contagem + 1
    print (contagem)   
#para imprimir uma sentença inteira ou parte dela
word= 'Calma'
print (word) 

fruta = 'Morango'
print (fruta[:3])

# 2 formas de se imprimir setenças na vertical
indice = 0
while indice < len(fruta):
  letra = fruta [indice]
  print(letra)
  indice = indice + 1

for char in fruta:
  print (char)
  
#se eu quiser imprimir coisas expecíficas da string
l = 'Santos Futebol'
print (l[0:6])
print (l[7:14])


#se eu quiser imprimir uma string com um conjunto de coisas
amigos= ('Vinicius', 'Joice', 'Nicole')
for amigo in amigos:
  print('Feliz Natal', amigo)
  print ('Felicidade')

#quando quiser saber se existe ou não alguma palavra dentro da sring
Sabado = 'Não tem aula'
res= 'aula'in Sabado
print(res)
res= 'tem' not in Sabado
print(res)

#se quiser imprimir número e texto juntos 2 formas
cidade= 'São Paulo'
dia= 22
mes = 'Outubro'
ano = 2022 
pessoa= 'Carlos Eduardo Pereira da Silva'
carta= '{}, {} de {} de {} \n{}'
print (cidade +',' + str(dia)+' de '+ mes +' de '+ str(ano)) 
print(carta.format(cidade, dia, mes, ano, pessoa)) 

anime = 'Neo Genesis Evangelion'
print(anime)

aula=10<15
print(aula)

curso='Terça'
print(bool(curso))

semana=''
print(bool(semana))

#LISTAS

carros=['Fusion', '328i', 'M4', 'Mustang']
carros[3]='Argo'
#adicionar coisas na lista
carros.append('Fit')
carros.append('Golf')
carros.append('M5')
carros.append('Carrera')
#deletar algo específico da lista
del carros[3]
#contar quantos itens tem na lista
print(str(len(carros)) + "carros na lista")
print(carros)

#FOR

motos=["XRE", "XJ6", "Fat Bob"]
for x in motos:
  print(x)
  if(x== 'Fat Bob'):
    print(' Harley Davidson') 

#input
manga = input("Seu anime preferido ")
print ('Otakinho safadin: ' + manga )