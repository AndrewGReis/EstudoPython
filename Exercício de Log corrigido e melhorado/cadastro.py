import sys

import os

import logging



# Configuração de logging

logging.basicConfig(

    filename='./meulog.log',

    level=logging.INFO,

    format='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'

)

logger = logging.getLogger()



DATABASE = "./database.txt"



def load_users() -> dict[str, str]:

    """Carrega os usuários do banco de dados (arquivo) em um dicionário."""

    users = {}

    if os.path.exists(DATABASE):

        logger.debug(f"Carregando usuários de {DATABASE}")

        try:

            with open(DATABASE, "r") as f:

                for line in f:

                    name, age = line.strip().split(",")

                    users[name] = age

        except Exception as e:

            logger.error(f"Erro ao carregar usuários: {e}")

            raise

    else:

        logger.debug("Nenhum usuário pre-registrado")

    return users



def save_users(users: dict[str, str]):

    """Salva os dados dos usuários no arquivo."""

    try:

        logger.info("Atualizando os registros do banco de dados...")

        with open(DATABASE, "w+") as f:

            for name, age in users.items():

                f.write(f"{name},{age}\n")

    except Exception as e:

        logger.error(

            f"Falha ao atualizar o banco de dados. {DATABASE=} \n {users=}\n Erro: {e}"

        )

        raise



def add_user(user_name: str, user_age: str, users: dict[str, str]):

    """Adiciona um novo usuário ao banco de dados."""



    logger.info(f"Adicionando o usuário {user_name=} {user_age=}")



    if user_name in users:

        print(f"Usuário {user_name} já existe.")

        logger.warning("Usuário já existente no banco. Retorno ao laço principal...")

        return



    users[user_name] = user_age

    save_users(users)

    logger.info("Usuário adicionado com sucesso!")

    print(f"Usuário {user_name} adicionado com sucesso!")



def rm_user(user_name: str, users: dict[str, str]):

    """Remove um usuário do banco de dados."""

    logger.info(f"Removendo o usuário {user_name=}")

    if user_name in users:

        del users[user_name]

        save_users(users)

        logger.info(f"Usuário removido com sucesso!")

        print(f"Usuário {user_name} removido com sucesso!")

    else:

        logger.info(f"{user_name=} não encontrado.")

        print(f"Usuário {user_name} não encontrado.")



def search_user_age(user_name: str, users: dict[str, str]) -> str | None:

    """Busca um usuário no banco de dados."""

    logger.info(f"Buscando {user_name=}..")

    if user_name in users:

        age = users[user_name]

        logger.info(f"Encontrado! {user_name=} user_age={age}")

        return age

    else:

        logger.info(f"{user_name=} não encontrado")

        return None



def list_users(users: dict[str, str]):

    """Lista todos os usuários em formato de tabela."""

    

    if not users:

        print("\nNenhum usuário cadastrado.")

        return

    

    # Cabeçalho da tabela

    print("\n{:<30} {:<10}".format('NOME', 'IDADE'))

    print("-" * 40)

    

    # Dados dos usuários (ordenados alfabeticamente)

    for name, age in sorted(users.items()):

        print("{:<30} {:<10}".format(name, age))

    

    print(f"\nTotal de usuários: {len(users)}")



def display_help():

    """Exibe mensagem de ajuda com os comandos disponíveis."""

    logger.debug("Mostrando mensagem de help")

    help_text = """

Comandos disponíveis:

  add <nome> <idade>  - Adiciona um novo usuário

  rm <nome>           - Remove um usuário

  search <nome>       - Busca um usuário

  list                - Lista todos os usuários cadastrados

  help                - Mostra esta ajuda

  sair                - Encerra o programa



Exemplos:

  add João Silva 25     - Adiciona um novo usuário

  rm Maria Santos       - Remove um usuário

  search Pedro Almeida  - Busca um usuário

  list                  - Mostra todos os usuários

"""

    print(help_text)



def main():

    logger.info("App iniciado")

    users = load_users()

    print("\n=== Sistema de Gerenciamento de Usuários ===")

    display_help()

    

    while True:

        logger.info("Aguardando input do usuário...")

        try:

            # Obtém entrada do usuário

            user_input = input("\nDigite um comando (ou 'sair' para encerrar): ").strip()

            

            # Ignora entradas vazias

            if not user_input:

                continue



            logger.debug(f"Input do usuário: {user_input}")

                

            # Divide o comando em partes

            parts = user_input.split()

            command = parts[0].lower()

            

            # para sair

            if command == 'sair':

                print("Encerrando o programa...")

                logger.info("App encerrado")

                break

                

            # caso precise de ajuda

            elif command == 'help':

                display_help()

                

            #  para adicionar usuário

            elif command == 'add':

                if len(parts) < 3:

                    print("Formato incorreto. Uso: add <nome> <idade>")

                    continue

                name = ' '.join(parts[1:-1])  # Permite nomes com espaços

                age = parts[-1]

                if not age.isdigit():

                    print("Erro: A idade deve ser um número inteiro.")

                    logger.warning(f"Idade passada em input não é numérica: {age}")

                    continue

                add_user(name, age, users)

                

            # para remover usuário

            elif command == 'rm':

                if len(parts) < 2:

                    print("Formato incorreto. Uso: rm <nome>")

                    continue

                name = ' '.join(parts[1:])  # Permite nomes com espaços

                rm_user(name, users)

                

            #para buscar usuário

            elif command == 'search':

                if len(parts) < 2:

                    print("Formato incorreto. Uso: search <nome>")

                    continue

                name = ' '.join(parts[1:])  # Permite nomes com espaços

                age = search_user_age(name, users)

                if age:

                    print(f"\nUsuário encontrado:\nNome: {name}\nIdade: {age}")

                else:

                    print(f"\nUsuário '{name}' não encontrado.")

            

            # para listar todos os usuários

            elif command == 'list':

                list_users(users)

                    

            # não reconhecido

            else:

                print("Comando não reconhecido. Digite 'help' para ver os comandos disponíveis.")

                

        except Exception as e:

            print(f"Ocorreu um erro: {e}\nDigite 'help' para ajuda.")

    



if __name__ == "__main__":

    main()