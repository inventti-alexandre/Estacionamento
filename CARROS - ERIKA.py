def menu():
  print("[1] Inserir carro")
  print("[2] Listar carros cadastrados")
  print("[3] Atualizar dados a partir de uma placa")
  print("[4] Vender carros")
  print("[5] Valor obtido pelas vendas")
  print("[6] Quantidade de carros livres, reservados e vendidos")
  print("[7] Reservar carros")
  print("[8] Quantidade de carros atualizados")
  print("[9] Quantidade de carros para venda( > R$50.000,00)")
  print("[10] Consulta para a compra")
  print("[0] Sair")

def verifica_placa(matriz, placa):
  for x in matriz:
    if x[0]== placa:
      return True
    else:
      return False

def verifica_ano(ano):
    if ano >= 1990 and ano <=2018:
      return True
    else:
      return False


def cadastrar_carro(matriz):
  linha=[]
  placa=str(input("Digite a placa: ")).upper()
  if not verifica_placa(matriz, placa):
    linha.append(placa)
    ano=int(input("Digite o ano de fabricação: "))
    linha.append(ano)
    if verifica_ano(ano):
      modelo=str(input("Digite o modelo do carro: ")).upper()
      linha.append(modelo)
      preco=float(input("Digite o valor do carro: "))
      linha.append(preco)
      status=str(input("Digite o status (LIVRE, VENDIDO, RESERVADO): ")).upper()
      linha.append(status)
      matriz.append(linha)
    else:
      print("O ano digitado não é válido. Retornaremos ao menu.")
  else:
    
    print("A placa digitada não é válida. Retornaremos ao menu. ")
      
def Atualizar_carro(matriz):
  placa1=str(input("Digite a placa do carro que deseja atualizar: ")).upper()
  print("O que deseja atualizar?\n[1] - Ano(Fabricação)\n[2] - Modelo\n[3] - Preço\n[4] - Status\n[5] - Atualizar todos os dados")
  x=str(input("Opcão ---->"))
  
  i=0
  for n in matriz:
    if n != placa1:
      i+=1
    if n[0] == placa1:
      i=0
      
  if x == "1":
    matriz[i][1]=int(input("Qual o ano de fabricação do carro? "))
  if x == "2":
    matriz[i][2]=str(input("Qual o modelo do carro? ")).upper()
  if x == "3":
    matriz[i][3]= float(input("Qual o preco do carro? "))
  if x == "4":
    matriz[i][4]=str(input("Digite o novo status do carro: ")).upper()
  if x == "5":
    matriz[i][1]=int(input("Qual o ano de fabricação do carro? "))
    matriz[i][2]=str(input("Qual o modelo do carro? ")).upper
    matriz[i][3]= float(input("Qual o preco do carro? "))
    matriz[i][4]=str(input("Digite o novo status do carro: ")).upper



def Vender_carros(matriz):
  ano_vender=int(input("Qual o ano do carro que o cliente deseja comprar? "))
  modelo_vender=str(input("Qual o modelo do carro que o cliente deseja comprar? ")).upper()
  
  for x in matriz:
    j=0
    if (x[:][1] != ano_vender) and (x[:][2] != modelo_vender):
      j+=1
      
  print(matriz[j][:])
  comprar=str(input("Esse é o carro escolhido.Para confirmar, digite SIM.Para cancelar, digite NÃO.")).upper()
  
  if comprar == "SIM":
    if matriz[j][4]=="LIVRE":
      matriz[j][4]="VENDIDO"
      print("Carro vendido com sucesso!")
    else:
      print("Desculpe este carro não está livre para a venda. ")
  else:
    print("Por favor, tente novamente.")

def Soma_vendas(matriz):
  soma_vendas=0
  for x in range (0, len(matriz)):
    if matriz[x][4] == "VENDIDO":
      soma_vendas += matriz[x][3]
  print("O valor total das vendas obtidas é: ", soma_vendas)


def Quantidade_carros(matriz):
  l=0
  r=0
  v=0
  for x in range (0, len(matriz)):
    if matriz[x][4]== "VENDIDO":
      v+=1
    elif matriz[x][4] == "LIVRE":
      l+=1
    elif matriz[x][4] == "RESERVADO":
      r+=1
  print("O total de carros vendidos é:", v, "\nO total de carros livres é:", l, "\nO total de carros reservados é:", r)
  print("-*-"*20)
    


def Reservar_carro(matriz):
  placa_reservar=str(input("Digite a placa do carro que você quer reservar: ")).upper()
  j=0
  for x in matriz:
    if x[0] == placa_reservar:
      j=0
    elif x != placa_reservar:
      j+=1
      
  if matriz[j][4]=="LIVRE":
    matriz[j][4]="RESERVADO"
    print("Carro reservado com sucesso! ")
  elif matriz[j][4]=="VENDIDO":
    print("Esse carro já está vendido. ")
  elif matriz[j][4] == "RESERVADO":
    print("Este carro já está reservado. ")
  
def Carro_livre(matriz):
  soma=0
  for x in range (0, len(matriz)):
    if matriz[x][4] == "LIVRE" and matriz[x][3] > 50000:
      soma+=1
  print("O valor total de carros livres e maior que R$ 50.000,00 é :", soma)
  
  
def Consulta_compra(matriz):
  valor=float(input("Digite o valor máximo que você deseja pagar: "))
  for x in matriz:
    if x[3] <= valor and x[4] == "LIVRE":
      print("**" * 20)
      print(x[:])
  print("Os carros que você poderá comprar estão listados acima. ")
      



def main():
  matriz=[]
  cont=0
  menu()
  opcao = True
  while opcao:
    opcao = str(input("Opção ---> "))
    if opcao == "0":
      opcao = False
    else:
      if opcao=="1":
        cadastrar_carro(matriz)
      elif opcao=="2":
        for linha in range (0, len(matriz)):
          print(matriz[linha])
      elif opcao=="3":
        cont+=1
        Atualizar_carro(matriz)
      elif opcao=="4":
        Vender_carros(matriz)
      elif opcao=="5":
        Soma_vendas(matriz)
      elif opcao=="6":
        Quantidade_carros(matriz)
      elif opcao == "7":
        Reservar_carro(matriz)
      elif opcao == "8":
        print("Foram feitas", cont, "atualizações em carros cadastrados. " )
      elif opcao == "9":
        Carro_livre(matriz)
      elif opcao == "10":
        Consulta_compra(matriz)
    menu()
  print(matriz)
main()
  
