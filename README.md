# Desafio de Código PwC

Um provedor de endereços retorna endereços apenas com ruas concatenadas, nomes e números em uma única string. Nosso próprio sistema, por outro lado, tem campos específicos para armazenar o nome da rua e o número da rua.

Portanto, se faz necessário escrever um código simples que processe a entrada e retorne esses campos na saída.

Entrada: string de endereço com os dados concatenados.
Saída: string da rua e string do número da rua.

### Casos Simples:
a. “Miritiba 339” -> {“Miritiba”, “339”}

b. “Babaçu 500” -> { “Babaçu”, “500”}

c. “Cambuí 804B” -> {“Cambuí”, “123B”}

### Considere os casos mais complicados:
a. “Rio Branco 23” -> {“Rio Branco”, “23”}

b. “Quirino dos Santos 23 b” -> {“Quirino dos Santos”, ”23 b”}

### Considere endereços de outros países (casos complexos)
a. “4, Rue de la République” -> {"Rue de la République", "4"}

b. “100 Broadway Av” -> {"Broadway Av", "100"}

c. “Calle Sagasta, 26” -> {“Calle Sagasta”, “26”}

d. “Calle 44 No 1991” -> {“Calle 44”, “No 1991”}

## Resolução

Foi utilizado o notebook Jupyter para confecção e testes desse desafio. 

Primeiro, foi importado a biblioteca Pandas para transformar o arquivo Excel em dataframe. Preferi trabalhar com input em excel pelo entrada.xlsx, pois é um software presente em todo lugar e facilita a extração e a saida.

Segundo, foi criada uma função chamada armazenar_endereco que verificará o endereço e retornará o valor em dicionário separado do logradouro e do número, de acordo com a exigência do desafio. 

Por fim, essa função é aplicada linha a linha d datraframe e retornada em excel como saida.xlsx em poucos segundos.

## Executável

O arquivo em python foi criado para ser encapsulado em executável por meio do pyinstaller. Fiz os testes e o desafio.exe está funcionando normalmente.

## Utilização do GitHub

Primeiro, eu criei e sincronizei meu repositório git com o github remoto. Depois, acabei não salvando e enviei apenas o arquivo criado por equívoco. Por isso, enviei o notebook base salvo para correção. Então,  primeiro eu resolvi os casos mais simples por facilidade de execução. Depois, resolvi os casos em que aparecia um número no endereço, seja no início, meio ou fim. 

Então, resolvi o caso em que aparece mais de uma vez os números no endereço e criei um markdown para exemplificar o desafio para posteridade. Como eu não tinha percebido que era para ser um executável, eu adaptei o código para trabalhar com pandas e facilitar a entrada e saida de informações, criei o .py e o .exe também. Por fim, atualizei novamente o markdown.
