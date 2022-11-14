#tuplas não permitem serem modificadas, listas sim
mangas=('Yowamushi Pedal', 'Hajime no Ippo', 'Jujutsu Kaisen')
print(mangas)
#listas
mangas=['Yowamushi Pedal', 'Hajime no Ippo', 'Jujutsu Kaisen']
mangas[2]='Spy Family'

for x in mangas:
  print(x)
  
#Matriz
carros= [ 
  ['Gol', 'Modelo'],
  ['Volks', 'Fabricante'],
  ['2016', 'ano']
]
for l,c in carros:
  print('Linhas' + l + '| Colunas'+ c )