# O que é
O "rastreamento_correios" é um scrypt feito em python com a intenção de rastrear um pedido qualquer utilizando técnicas de raspagem de dados aplicadas ao site dos correiros

# Como rodar?
Para executar este scrypt e obter um posicionamento sobre o seu pedido é simples, você precisa
- Ter um pedido
- - Geralmente quando você compra algo on-line este vem com um numero de rastreio ('SS123456789BR' é o exemplo de um!), ele possui 13 caracteres e podem ser encontrados no seu comprovante de postagem!
- Informar o código de rastreio do seu pedido junto a linha de execução do seu scrypt
- - ex `python rastreamento_correios SS123456789BR`

Dessa forma você executará o script em questão e ele utilizará o código que você informou como parámetro de pesquisa!
