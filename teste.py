import pyodbc
from datetime import date
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-0ATOPUE;" ##Nome do seu desktop
    "Database=Teste;"##Nome da sua Data Base
    "Trusted_connection = yes;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

id_venda= 0 #Id da venda = 0 para podermos adicionar conforme a operação for executada durante o looping
cursor = conexao.cursor()# adicionamos o cursor para poder mexer na nosso codigo
                                                 #e implementar a modificação no banco de dados
while True:#inicio looping
    
    opcao = input("\n\n\nDigite o que deseja fazer:\n\n 1- Adicionar algo ao banco de dados\n\n2-Listar o banco de dados\n\n3-Alterar nome do cliente no banco de dados\n\n4-Remover algo do banco de dados\n\n5-Sair\n\n")
    if opcao == "1":

        id_venda += 1
        nome = input("Digite o nome do cliente\n")
        produto = input("Digite o produto que o cliente está comprando\n")
        data = date.today()
        valor = int(input("Digite o valor do produto\n"))
        quantidade = int(input("Digite a quantidade que o cliente está compando\n"))

        comandoadd = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id_venda}, '{nome}', '{produto}', '{data}', {valor}, {quantidade})"""
        print("Adicionado")
        cursor.execute(comandoadd)
        cursor.commit()

    if opcao == "2":

        listcommand = """SELECT * FROM Vendas"""
        dados = pd.read_sql(listcommand,conexao)
        print(dados)

    if opcao == "3":

        idname = input("Digite o ID do nome a ser alterado:\n\n")
        novonome = input("Digite o novo nome:\n")
        comandoatt = f"""update Vendas set cliente='{novonome}' WHERE id_venda='{idname}'"""
        cursor.execute(comandoatt) 
        cursor.commit()
        print("Nome renomeado com sucesso!")

    if opcao == "4":

        idRem = int(input("Digite o ID a ser removido do banco de dados:\n"))
        comandorem = f"""DELETE FROM Vendas WHERE id_venda='{idRem}'"""
        cursor.execute(comandorem)
        
        cursor.commit()
        print("Removido")

    if opcao == "5":
        break