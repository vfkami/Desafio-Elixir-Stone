# Resolução do Teste Técnico | Programa de Formação em Elixir - Stone

Explicação da resolução do teste proposto para admissão do [**Programa de Formação em Elixir**](https://gist.github.com/programa-elixir/1bd50a6d97909f2daa5809c7bb5b9a8a)!

## Informações Iniciais

- Código escrito em **Python**;
- O calculo é realizado com valores inteiros, mas podem ser inseridos valores em ponto flutuante para testes;
- As listas de email e de produtos são checadas para ver se não há nenhuma lista com valor nulo ou vazio;
- Os produtos inseridos na lista de compras, precisam ser inseridos seguindo o padrão: ```NomeProduto, Quantidade, Preco``` 

## Resolução

- O total de cada item é calculado através da ```quantidade * preço```
- Para resolver o desafio proposto no teste, foi assumido que todos os valores de entrada seriam inteiros;
- Para simplificar, se inseridos valores com pontos flutuantes, estes valores serão somados e arredondados para cima, ao final da soma. Por exemplo:


        Item: Maçã
        Quantidade: 17.31
        Preço: 130
        
        Preço total a ser pago: 2250,3
        Preço arredondado: 2251
        
- Se forem adicionados mais de um item, o arredondamento acontecerá apenas no final, ao somar o preço de todos os produtos

Para que **não faltasse nenhum centávo**, em divisões com dízima, calculamos o valor que cada um deverá pagar da seguinte forma:

1. Tendo um valor total de 100 (R$ 1,00), por exemplo, para ser dividido em 6 e-mails, cada pessoa ficará com o valor de 16, pois não utilizaremos dízimas e arrendodaremos para baixo, inicialmente;
2. Após isso, multiplicaremos 16 pela quantidade de pessoas (6) e obteremos 96;
3. Subtraímos 96 de 100 e obtemos **4** como resto;
4. Distribuímos o resto igualmente para os **4** primeiros integrantes da lista, dessa forma, quatro pessoas ficarão com o valor de 17 e duas com o valor de 16, resultando em 100.


## Para rodar e testar!

Para realizar os testes, basta inserir as seguintes informações antes de rodar o código.    

- A lista de e-mails deve ser preenchida seguindo o exemplo:
```Python
emails = ['luffy@email.com', 'zoro@email.com', 'sanji@email.com', 'nami@email.com', 'chopper@email.com', 'usopp@email.com']
```

- A lista de compras deve ser preenchida seguindo o exemplo:
```Python
shoppinglist = [['apple', 175, 220], ['tomato', 1, 1154], ['bread', 10, 55], ['sauce', 1, 307], ['beef', 1, 1501], ['cabbage', 2, 156]]
```

- Para obter o resultado que uma pessoa terá de pagar, insira o email na ultima linha seguindo o exemplo
```Python
print(dic['luffy@email.com'])
```
