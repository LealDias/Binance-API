from binance.client import Client
import time
from binance import ThreadedWebsocketManager

# Chaves
api_key = 'ygLyQROn7y7SdNvMoJepOdhZJV4OJUPeq1hhYe2929CopY2ZqGREhnWnVy1FQMEs'
secret_key = 'aACSH2BCvZKNwp7bbQR5vtMOJAGMvJ8SUB2Cdfw5sBF1g8sRjhRevQfu6EYpssKC'

#Cliente
client = Client(api_key, secret_key)

# Testar conexão com a função ping
print(client.ping())

# Gerando os Tickers
tickers = client.get_all_tickers()
BTCUSDT = [i.values() for i in tickers if i.get('symbol') == 'BTCUSDT']

# Verificando o Ativo 'BTCUSDT' e seu respectivo valor.
print(BTCUSDT)


## Streaming dos Dados do Ativo 'BTCUSDT'

#Executando com apenas 10 segundos
delta = 0
start = time.time()
while delta < 10:
    tickers = client.get_all_tickers()
    BTCUSDT = [i.values() for i in tickers if i.get('symbol') == 'BTCUSDT']
    print(BTCUSDT)
    time.sleep(2) # Atualização a cada 2 segundos
    end = time.time()
    delta = (end) - (start)
print("Tempo de Execução: ", delta)    
print("Finalizado") 


## Streaming dos Dados do Ativo 'BTCUSDT' sem Chave

import websocket

cc = 'btcusd'
intervalo = '1m'
socket = f'wss://stream.binance.com:9443/ws/{cc}t@kline_{intervalo}'

def on_message(ws, message):
    print(message)
    
def on_close(ws):
    print("Conexão Terminada")

ws = websocket.WebSocketApp(socket, on_message= on_message, on_close= on_close)

ws.run_forever()