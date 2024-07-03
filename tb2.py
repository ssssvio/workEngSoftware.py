print("------ Bem-vindo a Loja de Marmitas do [SEU NOME COMPLETO] -----------")
print("------------------------------Cardápio--------------------------")
print("----------------------------------------------------------------")
print("---| Tamanho  |  Bife Acebolado(BA)  |  Filé de Frango(FF)  |---")
print("---|    P     |       R$ 16.00       |       R$ 15.00       |---")
print("---|    M     |       R$ 18.00       |       R$ 17.00       |---")
print("---|    G     |       R$ 22.00       |       R$ 21.00       |---")
print("----------------------------------------------------------------")

total = 0

while True:
  sabor = input("Entre com o sabor desejado (BA/FF): ")
  
  if sabor != "BA" and sabor != "FF":
    print("Sabor inválido. Tente novamente")
    continue
  
  tamanho = input("Entre com o tamanho desejado (P/M/G): ")
  
  if tamanho != "P" and tamanho != "M" and tamanho != "G":
    print("Tamanho inválido. Tente novamente")
    continue
  
  if sabor == "BA":
    if tamanho == "P":
      total += 16
    elif tamanho == "M":
      total += 18
    else:
      total += 22
  else:
    if tamanho == "P":
      total += 15
    elif tamanho == "M":
      total += 17
    else:
      total += 21
  
  adcional = input("Deseja mais alguma coisa? (S/N): ")
  
  if adcional.upper() == "N":
    break

print("O valor total a ser pago: R$", total)