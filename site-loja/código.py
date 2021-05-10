import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb3dc4e2de07148bdbf9181c40adc2a1f"
# Your Auth Token from twilio.com/console
auth_token  = "f71a1d1d084c1898c6d8d878b0b6f76c"
client = Client(account_sid, auth_token)

# Vendas acima de R$ 55.000 ganha viagem
# Passo a passo da solução
# Abrir os 6 arquivos do Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes de {mes} o Vendedor {vendedor} bateu a meta com {vendas} de Vendas')
        print(f'PARABÉNS {vendedor}, você acaba de ganhar uma viagem com tudo pago!!')
        message = client.messages.create(
            to="+5544xxxxxxxx",
            from_="+18142773347",
            body=f'PARABÉNS, por ter batido a meta de 55000, você  ganhou a viagem com tudo pago!!')
        print(message.sid)

# Para cada arquivo:

# Verificar se algum valor na coluna da Vendas  daquele arquivo é maior que R$ 55.000

# Se for maior que R$ 55.000 -> envia um SMS -> para o vendedor que ultrapassou a meta