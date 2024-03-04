# Importação de módulos
import pwinput
import oracledb

# Tentativa de Conexão com o Banco de Dados

try:
    # Credenciais de Acesso (Usuário e Senha)
    usuario = input("Usuário: ")
    senha = pwinput.pwinput("Senha: ")

    # Conexão com o Banco de Dados
    conn = oracledb.connect(user= usuario, password= senha, host= "oracle.fiap.com.br", port= 1521, service_name= "orcl")

    # Cursor para Execução de Comandos SQL
    cursor = conn.cursor()
except Exception as erro:
    print(f"Erro: {erro}")    # Informa o erro
    conexao = False    # Flag para não executar a Aplicação
else:
    conexao = True    # Flag para executar a Aplicação

    

            