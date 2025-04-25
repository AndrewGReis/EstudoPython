import sys
import os
import logging
from typing import Optional, Dict

# Configuração de logging
logging.basicConfig(
    filename='meulog.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(funcName)s - Linha: %(lineno)d'
)
logger = logging.getLogger()

DATABASE = "database.txt"

def load_users() -> Dict[str, str]:
    """Carrega os usuários do banco de dados (arquivo) em um dicionário."""
    users = {}
    if os.path.exists(DATABASE):
        try:
            logger.debug(f"Carregando usuários do arquivo {DATABASE}...")
            with open(DATABASE, "r") as f:
                for line in f:
                    name, age = line.strip().split(",")
                    users[name] = age
            logger.info(f"Usuários carregados com sucesso. Total de usuários: {len(users)}")
        except Exception as e:
            logger.error(f"Erro ao carregar dados do arquivo {DATABASE}: {e}")
            raise
    else:
        logger.info(f"O banco de dados {DATABASE} não foi encontrado. Criando um novo.")
    return users

def save_users(users: Dict[str, str]):
    """Salva os dados dos usuários no arquivo."""
    try:
        logger.debug(f"Salvando {len(users)} usuários no arquivo {DATABASE}.")
        with open(DATABASE, "w") as f:
            for name, age in users.items():
                f.write(f"{name},{age}\n")
        logger.info(f"Usuários salvos com sucesso. Total de usuários: {len(users)}")
    except Exception as e:
        logger.error(f"Erro ao salvar usuários no arquivo {DATABASE}: {e}")
        raise

def add_user(user_name: str, user_age: str, users: Dict[str, str]):
    """Adiciona um novo usuário ao banco de dados."""
    logger.info(f"Operação 'add': Adicionando usuário - nome={user_name}, idade={user_age}")

    if user_name in users:
        logger.warning(f"Usuário {user_name} já existe no banco de dados.")
        print(f"Usuário {user_name} já existe.")
        return

    users[user_name] = user_age
    save_users(users)
    logger.info(f"Usuário {user_name} adicionado com sucesso. Total de usuários: {len(users)}")
    print(f"Usuário {user_name} adicionado com sucesso!")

def rm_user(user_name: str, users: Dict[str, str]):
    """Remove um usuário do banco de dados."""
    logger.info(f"Operação 'remove': Removendo usuário - nome={user_name}")

    if user_name in users:
        del users[user_name]
        save_users(users)
        logger.info(f"Usuário {user_name} removido com sucesso. Total de usuários restantes: {len(users)}")
        print(f"Usuário {user_name} removido com sucesso!")
    else:
        logger.warning(f"Usuário {user_name} não encontrado no banco de dados.")
        print(f"Usuário {user_name} não encontrado.")

def search_user(user_name: str, users: Dict[str, str]) -> Optional[str]:
    """Busca um usuário no banco de dados."""
    logger.info(f"Operação 'search': Buscando usuário - nome={user_name}")

    if user_name in users:
        age = users[user_name]
        logger.info(f"Usuário encontrado: {user_name} - {age}")
        return age
    else:
        logger.info(f"Usuário {user_name} não encontrado.")
        return None

def list_users(users: Dict[str, str]):
    """Lista todos os usuários em formato de tabela."""
    logger.info("Operação 'list': Listando todos os usuários")
    
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
    users = load_users()
    
    print("\n=== Sistema de Gerenciamento de Usuários ===")
    display_help()
    
    while True:
        try:
            # Obtém entrada do usuário
            user_input = input("\nDigite um comando (ou 'sair' para encerrar): ").strip()
            
            # Ignora entradas vazias
            if not user_input:
                continue
                
            # Divide o comando em partes
            parts = user_input.split()
            command = parts[0].lower()
            
            # para sair
            if command == 'sair':
                print("Encerrando o programa...")
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
                age = search_user(name, users)
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
            logger.error(f"Erro durante a execução: {e}")
            print(f"Ocorreu um erro: {e}\nDigite 'help' para ajuda.")

if __name__ == "__main__":
    main()