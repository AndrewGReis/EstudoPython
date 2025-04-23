# %%

from logging import error, critical, warning, info, debug # chamadas
from logging import basicConfig # configuração
from logging import DEBUG # level
from logging import FileHandler, StreamHandler  # Handlers

basicConfig(
    level=DEBUG,
    filename='meus_logs.txt',
    filemode='a', # esse a, é como se fosse um append, vai adicionando
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    handlers=[FileHandler("meus_logs.txt", "w"), StreamHandler()]
)

debug("Entrei aqui.")
debug("Sai aqui.")

info("Pessoa X logou")

error("Deu erro na solicitação de uma pessoa!")
critical("A minha aplicação parou! ")
warning("Algo de errado aconteceu")

# %%
