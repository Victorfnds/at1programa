import sys
print('-' * 20)
print('MENU')
print('-' * 20)
print()
print('OPÇÕES', )
print('[1], - COMPRAS')
print('[2], - VENDAS')
print('[3], - SALDO')
print('[4], - SAIR')
# menu principal
def main():
 while True:
  resposta1 = int(input(" Selecione sua opção:" ))
  if resposta1 ==1:
   transação(compra)
  elif resposta1 ==2:
   transação(venda)
  elif resposta1 ==3:
   saldo()
  elif resposta1 ==4:
   print('saindo do programa')
   sys.exit()

#menu de transações
def transação(tipo):
 print('-' * 20)
 print('MENU')
 print('-' * 20)
 print()
 print('OPÇÕES', )
 print('[1], - NOME')
 print('[2], - QUANTIDADE')
 print('[3], - VALOR')
 print('[4], - SAIR')
resposta = input("insira  a sua opção")
if resposta ==1:
  nome = input("insira o nome")
elif resposta ==2:
  quantidade = int(input("insira a quantidade"))
else:
  print("valor incorreto")
if resposta ==3:
  preço = int(input("insira o valor"))
else:
  print("valor incorreto")
if resposta ==4:
  main()

# criando listas
lista1 = list[nome]


#saldo

def saldo():
 print("o saldo total é", total(compras) - total(vendas))