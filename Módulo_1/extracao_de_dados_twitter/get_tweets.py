import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# Cadastrar as chaves de acesso
consumer_key = 'Rez2QrEaaw4MTRfNg7RCtlQUf'
consumer_secret = 'E9P4Ig9CEJPO4xVKoV0UPNT8qiCCz1PiRdKmQlBK88m3c7mGFn'

access_token = '1329889067480322049-IaByhIBOk3XfnoUARWdG5KCjxfEI1X'
access_token_secret = 'HBfIyHvIaUdeMTkZsEkWh1iG6R3Eg0Owh8kphyiH09RUW'

# Definir um arquivo de saída para armazenar os tweets coletados
date_hoje = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
out = open(f'collected_tweets_{date_hoje}.txt',"w")

# Implementar uma classe para conexão com o twitter

class MyListener(StreamListener):

    def on_data(self, data):
        itemstring = json.dumps(data)
        out.write(itemstring + '\n')
        return True

    def on_error(self, status):
        print(status)



# implementar nossa função MAIN
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=["Trump"])

