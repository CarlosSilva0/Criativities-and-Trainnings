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