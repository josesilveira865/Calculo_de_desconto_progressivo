# app.py - Sistema de Desconto Progressivo
# ENTRADA: COLETA DE DADOS DO USUÁRIO
# Solicita ao usuário que insira o valor total da compra
# A função float() converte o valor inserido em número decimal
valor_compra = float(input("Digite o valor total da compra: R$ "))


# PROCESSAMENTO: CÁLCULO DO DESCONTO

# Verifica em qual faixa de desconto o valor da compra se encaixa
# Utiliza estruturas de decisão para determinar a porcentagem

if valor_compra < 200:
    # Se a compra for menor que R$ 200, aplica desconto de 5%
    porcentagem_desconto = 0.05
    
elif valor_compra < 300:
    # Se a compra for entre R$ 200 e R$ 299.99, aplica desconto de 10%
    porcentagem_desconto = 0.10
    
else:
    # Se a compra for R$ 300 ou mais, aplica desconto de 15%
    porcentagem_desconto = 0.15

# Calcula o valor do desconto em reais multiplicando o valor da compra
# pela porcentagem de desconto determinada acima
valor_desconto = valor_compra * porcentagem_desconto

# Calcula o valor final que o cliente deve pagar
# subtraindo o valor do desconto do valor original da compra
valor_final = valor_compra - valor_desconto

# SAÍDA: EXIBIÇÃO DOS RESULTADOS

# Exibe os resultados de forma organizada e formatada para o usuário
print("\n" + "="*50)
print("RESUMO DA COMPRA")
print("="*50)
print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: {porcentagem_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")
print("="*50 + "\n")
