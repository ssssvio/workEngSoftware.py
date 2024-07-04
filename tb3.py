print("Bem vindos a Fábrica de Camisetas do Sávio Rezende de Freitas")

def escolha_modelo():
    while True:
        print("\n Entre com o modelo desejado")
        print("MCS - Manga Curta Simples")
        print("MLS - Manga Longa Simples")
        print("MCE - Manga Curta Com Estampa")
        print("MLE - Manga Longa Com Estampa")
        modelo = input("->").strip().upper()
        
        if modelo == 'MCS':
            return 1.80
        elif modelo == 'MLS':
            return 2.10
        elif modelo == 'MCE':
            return 2.90
        elif modelo == 'MLE':
            return 3.20
        else:
            print("Escolha inválida, entre com o modelo novamente")

def num_camisetas():
    while True:
        try:
            num = int(input("Entre com o número de camisetas: "))
            if num > 20000:
                print("Não aceitamos tantas camisetas de uma vez. Por favor, entre com o número de camisetas novamente.")
                continue
            
            if num < 20:
                desconto = 0
            elif 20 <= num < 200:
                desconto = 0.05
            elif 200 <= num < 2000:
                desconto = 0.07
            elif 2000 <= num <= 20000:
                desconto = 0.12

            num_com_desconto = num * (1 - desconto)
            return num_com_desconto
        
        except ValueError:
            print("Valor inválido, por favor, entre com um número válido de camisetas.")

def frete():
    while True:
        print("\n Escolha o tipo de frete:")
        print("1 - Frete por transportadora - R$ 100.00")
        print("2 - Frete por Sedex - R$ 200.00")
        print("0 - Retirar pedido na fábrica - R$ 0.00")
        opcao_frete = input("->").strip()
        
        if opcao_frete == '1':
            return 100
        elif opcao_frete == '2':
            return 200
        elif opcao_frete == '0':
            return 0
        else:
            print("Opção inválida, entre com o tipo de frete novamente.");

if __name__ == "__main__":
    valor_modelo = escolha_modelo()
    quantidade = num_camisetas()
    valor_frete = frete()

    total = (valor_modelo * quantidade) + valor_frete

    print("\n--------------------- Resumo do Pedido --------------------- \n")
    print(f"Total: R$ {total:.2f} (Modelo: {valor_modelo:.2f} * Quantidade(com desconto): {quantidade:.0f} + frete: {valor_frete:.2f})")
    print("\nObrigado por comprar conosco! Volte sempre!")