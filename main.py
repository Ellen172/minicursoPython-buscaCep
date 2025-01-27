import requests #aceita requisições via internet

cep = input ("Digite o CEP (sem traços): ") # input para receber o cep do usuário

resposta = requests.get("https://viacep.com.br/ws/%s/json/" %(cep))# envia o cep para a API viacep

if resposta.status_code != 200 : 
  print("Erro no acesso a API viacep!")
else : 
  dados = resposta.json()
  print ('dados: ', dados) # printa todas as informações encontradas para o cep informado