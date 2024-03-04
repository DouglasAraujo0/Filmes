# Importação de módulos
import pwinput
import oracledb

def cadastrar():
    try:
        print("-----------------Cadastrar Filme-----------------")

        # Recebe valores para o cadastro
        genero = input("Gênero: ")
        nome = input("Nome: ")
        dt_lancamento = input("Data de Lançamento (dd/mm/aaaa): ") 
        duracao = int(input("Duração: "))

        # Monta a instrução SQL de cadastro em uma string
        cadastro = f"""INSERT INTO FILMES (GENERO_FILME, NOME_FILME, DT_LANCAMENTO, DURACAO) VALUES ('{genero}', '{nome}', TO_DATE('{dt_lancamento}', 'YYYY-MM-DD'), {duracao})"""

        # Executa e grava o registro na tabela
        cursor.execute(cadastro)
        conn.commit()
    except ValueError:
        print("Valor inválido.")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        print("Filme cadastrado com sucesso.")
        input("Pressione Enter para continuar...") 


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


# Enquanto a flag conexao estiver True, a aplicação será executada
while conexao:
    print("1 - Cadastrar Filme")
    print("2 - Listar Filmes")
    print("3 - Atualizar Filme")
    print("4 - Excluir Filme")
    print("5 - Sair")
    escolha = int(input("Escolha uma opção: "))

    match escolha:
        case 1:
            cadastrar()
            break
        case 2:
            listar()
            break
        case 3:
            atualizar()
            break
        case 4:
            excluir()
            break
        case 5:
            print("Saindo...")
            break
        case _:
            print("Opção Inválida.")
    

            