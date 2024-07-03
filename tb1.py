print("Bem-vindo ao E-commerce SyncEletrônicos! \n");

valorDoPedido = float(input("Informe o valor do pedido: "));
quantidadeParcelas = int(input("Informe também o número de parcelas: "));

if quantidadeParcelas < 4:
  juros = 0
elif 4 <= quantidadeParcelas < 6:
  juros = 0.04
elif 6 <= quantidadeParcelas < 9:
  juros = 0.08
elif 9 <= quantidadeParcelas < 13:
  juros = 0.16
else:
  juros = 0.32

valorDaParcela = valorDoPedido * (1 + juros) / quantidadeParcelas;
valorTotalParcelado = valorDaParcela * quantidadeParcelas;

print("\n ----------------- Resumo do Pedido --------------------- \n");
print(f"O valor de cada parcela é de: R$ {valorDaParcela:.2f}");
print(f"O valor total parcelado é de: R$ {valorTotalParcelado:.2f} \n");
print("Obrigado por comprar conosco! Volte sempre!");