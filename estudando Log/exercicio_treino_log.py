import sys
import os
import logging
from typing import Optional, List

# Configuração de logging
logging.basicConfig(
    filename='meulog.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

DATABASE = "database.txt"


def create_database():
    """Cria o arquivo de banco de dados se não existir."""
    if os.path.exists(f"./{DATABASE}"):
        logger.debug("Banco de dados já existente")
    else:
        logger.debug("Criando um novo banco de dados")
        try:
            with open(f"./{DATABASE}", "w") as f:
                pass
        except Exception as e:
            logger.error(f"Erro ao criar banco de dados: {e}")
            raise


def add_user(user_name: str, user_age: str):
    """Adiciona um novo usuário ao banco de dados."""
    logger.info(f"Usuário a ser adicionado: {user_name} - {user_age}")
    
    try:
        with open(DATABASE, "a") as f:
            f.write(f"{user_name},{user_age}\n")
        logger.info(f"Usuário adicionado com sucesso!")
        print("Usuário adicionado com sucesso!")
    except Exception as e:
        logger.error(f"Erro ao adicionar usuário: {e}")
        raise


def rm_user(user_name: str):
    """Remove um usuário do banco de dados."""
    logger.info(f"Usuário a ser removido: {user_name}")
    
    try:
        # Lê todos os usuários e filtra o que será removido
        with open(DATABASE, "r") as f:
            lines = f.readlines()
        
        with open(DATABASE, "w") as f:
            removed = False
            for line in lines:
                if not line.startswith(f"{user_name},"):
                    f.write(line)
                else:
                    removed = True
            
            if removed:
                logger.info(f"Usuário removido com sucesso!")
                print("Usuário removido com sucesso!")
            else:
                logger.warning(f"Usuário não encontrado: {user_name}")
                print("Usuário não encontrado!")
    except Exception as e:
        logger.error(f"Erro ao remover usuário: {e}")
        raise


def search_user(user_name: str) -> Optional[List[str]]:
    """Busca um usuário no banco de dados."""
    logger.info(f"Buscando usuário: {user_name}")
    
    try:
        with open(DATABASE, "r") as f:
            for line in f:
                name, age = line.strip().split(",")
                if name == user_name:
                    logger.info(f"Usuário encontrado: {name} - {age}")
                    return [name, age]
        
        logger.info(f"Usuário não encontrado: {user_name}")
        return None
    except Exception as e:
        logger.error(f"Erro ao buscar usuário: {e}")
        raise


def display_help():
    """Exibe mensagem de ajuda com os comandos disponíveis."""
    help_text = """
Comandos disponíveis:
  add <nome> <idade>  - Adiciona um novo usuário
  rm <nome>           - Remove um usuário
  search <nome>       - Busca um usuário
  help                - Mostra esta ajuda
"""
    print(help_text)


def main():
    if len(sys.argv) < 2:
        display_help()
        return

    try:
        create_database()
        op = sys.argv[1].lower()

        if op == "add":
            if len(sys.argv) != 4:
                print("Uso: python app.py add \"Nome\" idade")
                return
            user_name = sys.argv[2]
            user_age = sys.argv[3]
            add_user(user_name, user_age)

        elif op == "rm":
            if len(sys.argv) != 3:
                print("Uso: python app.py rm \"Nome\"")
                return
            user_name = sys.argv[2]
            rm_user(user_name)

        elif op == "search":
            if len(sys.argv) != 3:
                print("Uso: python app.py search \"Nome\"")
                return
            user_name = sys.argv[2]
            user = search_user(user_name)
            if user:
                print(f"Usuário:\nnome: {user[0]}\nidade: {user[1]}")
            else:
                print("Usuário não encontrado!")

        elif op == "help":
            display_help()

        else:
            logger.warning(f"Operação não reconhecida: {op}")
            print("Operação não reconhecida. Use 'help' para ver os comandos disponíveis.")

    except Exception as e:
        logger.error(f"Erro durante a execução: {e}")
        print("Ocorreu um erro durante a execução. Verifique o log para mais detalhes.")


if __name__ == "__main__":
    main()