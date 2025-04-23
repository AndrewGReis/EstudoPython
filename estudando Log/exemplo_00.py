# %%
from logging import error, critical, warning, info, debug
from logging import basicConfig
from logging import INFO


basicConfig(level=INFO)

debug("Entrei aqui.")
debug("Sai aqui.")

info("Pessoa X logou")

error("Deu erro na solicitação de uma pessoa!")
critical("A minha aplicação parou! ")
warning("Algo de errado aconteceu")
# %%
