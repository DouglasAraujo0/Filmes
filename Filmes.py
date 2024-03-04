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
        consulta = f"""SELECT * FROM FILMES WHERE ID_FILME = {id_filme}"""

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
                dt_lancamento_novo = input("Digite uma nova data de lançamento (dd/mm/aaaa): ")
                duracao_novo = int(input("Digite uma nova duração: "))

                # Constroi a instrução de atualização
                atualizacao = f"""UPDATE FILMES SET 
                GENERO_FILME = '{genero_novo}',
                NOME_FILME = '{nome_novo}',
                DT_LANCAMENTO = TO_DATE('{dt_lancamento_novo}', 'YYYY-MM-DD'),
                DURACAO = {duracao_novo} WHERE ID_FILME = {id_filme}"""

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
    

            