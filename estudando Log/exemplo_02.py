# %%
from logging import error, critical, warning, info, debug # chamadas
from logging import basicConfig # configuração
from logging import DEBUG # level
from logging import FileHandler, StreamHandler  # Handlers

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    handlers=[FileHandler("teste.txt", "w"), StreamHandler()] #escreve no arquivo(file) e escreve no shell (stream)
)

debug("Entrei aqui.")
debug("Sai aqui.")
info("Pessoa X logou")
error("Deu erro na solicitação de uma pessoa!")
critical("A minha aplicação parou! ")
warning("Algo de errado aconteceu")

# %%
