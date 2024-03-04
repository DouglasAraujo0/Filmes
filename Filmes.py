# Importação de módulos
import pwinput
import oracledb

def obter_duracao():
    while True:
        try:
            duracao = int(input("Duração: (em minutos) "))
            if 0 < duracao <= 250:
                return duracao
            else:
                print("Por favor, insira um valor válido para a duração (entre 1 e 250 minutos).")
        except ValueError:
            print("Por favor, insira um valor inteiro válido.")
def cadastrar():

    try:
        print("-----------------Cadastrar Filme-----------------")

        # Recebe valores para o cadastro
        genero = input("Gênero: ")
        nome = input("Nome: ")
        duracao = obter_duracao()
        sinopse = input("Sinopse: ")

        # Monta a instrução SQL de cadastro em uma string
        cadastro = f"""INSERT INTO FILMES (GENERO_FILME, NOME_FILME, DURACAO, SINOPSE) VALUES ('{genero}', '{nome}', '{duracao}', '{sinopse}')"""

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


def listar():

    try:
        print("-----------------Listar Filme-----------------")

        # Lista para captura de dados do Banco 
        lista_dados = []

        # Monta a instrução SQL de consulta 
        consulta = f"""SELECT * FROM FILMES"""

        # Captura os registros da tabela
        cursor.execute(consulta)
        data = cursor.fetchall()

        # Adiciona os registros na lista
        for dt in data:
            lista_dados.append(dt)

        # Ordena a lista
        lista_dados = sorted(lista_dados)

        #Verifica se há filmes cadastrados
        if len(lista_dados) == 0:
            print("Nenhum filme cadastrado.")
        else:
            # Exibe os registros
            for item in lista_dados:
                print(item)
    except:
        print("Erro ao listar filmes.")
    else:
        input("Pressione Enter para continuar...")


def atualizar():

    try:
        print("-----------------Atualizar Filme-----------------")

        # Lista para captura de dados da tabela
        lista_dados = []

        # Permite o usuário escolher o filme a ser atualizado pelo id
        id_filme = int(input("Informe o ID do Filme: "))

        # Constroi a instrução de consulta para verificar se o filme existe
        consulta = f"""SELECT * FROM FILMES WHERE ID = {id_filme}"""

        # Captura os registros da tabela
        cursor.execute(consulta)
        data = cursor.fetchall()

        # Preenche a lista com os registros
        for dt in data:
            lista_dados.append(dt)

        # Verifica se o filme existe
            if len(lista_dados) == 0:
                print(f"Filme com o id {id_filme} não encontrado.")
            else:
                # Captura os novos valores para atualização
                genero_novo = input("Digite um novo gênero: ")
                nome_novo = input("Digite um novo nome: ")
                duracao_novo = int(input("Digite uma nova duração: "))
                sinopse_nova = input("Digite uma nova sinopse: ")

                # Constroi a instrução de atualização
                atualizacao = f"""UPDATE FILMES SET 
                GENERO_FILME = '{genero_novo}',
                NOME_FILME = '{nome_novo}',
                DURACAO = {duracao_novo},
                SINOPSE = '{sinopse_nova}' WHERE ID = {id_filme}"""

                # Executa a atualização
                cursor.execute(atualizacao)
                conn.commit()

                print("Filme atualizado com sucesso.")
    except ValueError:
        print("Valor inválido.")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        input("Pressione Enter para continuar...")


def excluir():
    try:
        print("-----------------Excluir Filme-----------------")

        # Lista para captura de dados da tabela
        lista_dados = []

        # Permite o usuário escolher o filme a ser excluído pelo id
        id_filme = int(input("Informe o ID do Filme: "))

        # Constroi a instrução de exclusão
        exclusao = f"""DELETE FROM FILMES WHERE ID = {id_filme}"""

        # Executa a exclusão
        cursor.execute(exclusao)
        conn.commit()
    except ValueError:
        print("Valor inválido.")
    except Exception as erro:
        print(f"Erro: {erro}")
    else:
        print("Filme excluído com sucesso.")
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
        case 2:
            listar()
        case 3:
            atualizar()
        case 4:
            excluir()
        case 5:
            print("Saindo...")
            break
        case _:
            print("Opção Inválida.")
    

            