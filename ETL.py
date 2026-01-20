import pandas as pd
df = pd.read_csv("clientes.csv", sep=";")

# TRANSFORM
def gerar_mensagem(nome, conta, cartao):
    return (
        f"Olá, {nome}! Vimos sua conta {conta} e o final do cartão {cartao}. "
        f"Uma dica: separe um valor fixo por semana para construir uma reserva e acompanhar sua evolução."
    )

df["mensagem"] = df.apply(
    lambda x: gerar_mensagem(x["nome"], x["conta"], str(x["cartao"])),
    axis=1
)

# LOAD
df.to_csv("clientes_enriquecidos.csv", index=False, encoding="latin1", sep=";")

print(df.head())
print("Arquivo gerado: clientes_enriquecidos.csv")