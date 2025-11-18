import pandas as pd

dados = {
    'cargos':["assistente", "analista", "gerente", "diretor"],
    'salarios':[1000, 2000, 3000, 4000]
}

dados_bi = pd.DataFrame(dados)
print(dados_bi)
