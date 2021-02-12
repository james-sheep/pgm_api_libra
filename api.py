import requests
import pandas as pd

url = "http://10.20.10.174:8080/endpoints/tarefas/proximas"
r = requests.get(url)
a = r.json()
b = r.text
df = pd.DataFrame(a, columns=["id", "tarefa_especie_id", "usuario_criacao_id","subsidio", "prazo_inicio", "prazo_fim"])
print(df)
print("")
print(b)




