# minicursoPython-buscaCep
Programa recebe um cep do usuario e fornece o endereço equivalente buscando através de uma API

## Funcionamento

1. O sistema solicita ao usuário um cep 
2. O usuário informa o cep 
3. O sistema envia o cep informado como requisição para API [ViaCEP](https://viacep.com.br/)
3. 1. Se a API encontra as informações para o CEP, o sistema printa essas informações
3. 2. Se a API não localiza as informações para o CEP, o sistema apresenta uma mensagem de erro

## Possíveis melhorias

- Conferir erro, existirão dois tipos de erro: 1) não foi possível acessar a API; 2) não foi possível encontrar o endereço através do CEP informado. Hoje o sistema valida o primeiro caso, com mensagem errada. E o segundo caso não está sendo válidado, apresentando o json com erro enviado pela API
- Hoje o sistema apresenta as informações em formato json para o usuário, incluindo campos vazios. Alterar esse design, para que cada informação esteja em um linha e que só apresente os campos que estejam preenchidos.