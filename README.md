# Sistema de Desconto Progressivo

Aplicativo Python que calcula automaticamente descontos progressivos baseados no valor total da compra para loja online.

## Descrição

O Sistema de Desconto Progressivo visa recompensar clientes que realizam compras de maior valor. O sistema utiliza estruturas de decisão (if/elif/else) para determinar automaticamente a melhor porcentagem de desconto a ser aplicada.

## Estrutura do Código

O programa segue a estrutura clássica de programação com três etapas:

### 1. Entrada (Input)

- Entrada de dados interativa: Solicita o valor da compra ao usuário
- Coleta o valor da compra do usuário através de `input()`
- Converte a entrada em tipo `float` para operações numéricas

### 2. Processamento

- Avalia a faixa de valor da compra usando estruturas condicionais
- Define a porcentagem de desconto apropriada
- Calcula o valor absoluto do desconto em reais
- Cálculo automático de descontos: Aplica descontos progressivos conforme faixas de valor
- Processamento de dados: Converte entrada do valor em número decimal
- Calcula o valor final a pagar

### 3. Saída

- Mostra todos os detalhes da transação ao usuário de forma organizada e formatada
- Utiliza formatação com f-strings para melhor legibilidade
- Apresentação monetária: Valores exibidos com duas casas decimais para precisão

## Tabela de Descontos Aplicados

O sistema aplica descontos progressivos conforme o valor da compra. Para compras com valor menor que R$ 200,00, é concedido um desconto de 5%. Para compras a partir de R$ 200,00 até R$ 299,99, o cliente recebe um desconto de 10%. Por fim, para compras com valor igual ou superior a R$ 300,00, é aplicado o desconto máximo de 15%.

## Detalhes da Lógica de Desconto

```python
if valor\_compra < 200:
    # Desconto pequeno para compras menores
    porcentagem\_desconto = 0.05  # 5%
    
elif valor\_compra < 300:
    # Desconto médio para compras moderadas
    porcentagem\_desconto = 0.10  # 10%
    
else:
    # Desconto máximo para compras maiores
    porcentagem\_desconto = 0.15  # 15%







