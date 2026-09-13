# app.py - Sistema de Desconto Progressivo

# ENTRADA: COLETA DE DADOS 

compra = float(input("Digite o valor da compra: "))

# PROCESSAMENTO: CÁLCULO DO DESCONTO -- # SAÍDA: EXIBIÇÃO DOS RESULTADOS

if compra < 200:
    print("Valor da compra: R$ %.2f - Desconto de 5%%" % compra)
elif compra < 300:
    print("Valor da compra: R$ %.2f - Desconto de 10%%" % compra)
else:
    print("Valor da compra: R$ %.2f - Desconto de 15%%" % compra)


