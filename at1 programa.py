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
   compras()
  elif resposta1 ==2:
   vendas()
  elif resposta1 ==3:
   saldo()
  elif resposta1 ==4:
   print('saindo do programa')
   quit()

#menu de compras
def compras():
 print('-' * 20)
 print('MENU')
 print('-' * 20)
 print()
 print('OPÇÕES', )
 print('[1], - NOME')
 print('[2], - QUANTIDADE')
 print('[3], - VALOR')
 print('[4], - SAIR')
resposta2 = input("insira  a sua opção")
if resposta2 ==1:
  nome_compra = input("insira o nome")
elif resposta2 ==2:
  quant_compra = int(input("insira a quantidade"))
else:
  print("valor incorreto")
if resposta2 ==3:
  preço_compra = int(input("insira o valor"))
else:
  print("valor incorreto")
if resposta2 ==4:
  quit()

#menu de vendas
def vendas():
 print('-' * 20)
 print('MENU')
 print('-' * 20)
 print()
 print('OPÇÕES', )
 print('[1], - NOME')
 print('[2], - QUANTIDADE')
 print('[3], - VALOR')
 print('[4], - SAIR')

resposta3 = int(input("escolha sua opção"))
if resposta3 ==1:
 nome_venda = input("insira o nome do produto")
elif resposta3 ==2:
   quant_venda = int(input("insira a quantidade"))
else:
 print("valor invalido")
if resposta3 ==3:
   preço_venda = int(input("insira o valor"))
else:
  print("valor incorreto")
if resposta3 ==4:
   main()

# criando listas

lista_compras = list["nomecompra", "preçocompra", "quantcompra"]
lista_vendas = list["nome_venda", "preço_venda", "quant_venda"]

#saldo
totalvendas = quant_venda * preço_venda
totalcompras = quant_compra * preço_compra
def saldo():
 print("o saldo total é", totalvendas - totalcompras)