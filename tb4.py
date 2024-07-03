import copy

print("Bem vindos a empresa de Sávio Rezende de Freitas");

lista_funcionarios = [];
id_global = 4659904;

def cadastrar_funcionario(id):
    print(f"\n---------- MENU CADASTRAR FUNCIONÁRIO ------------------");
    nome = input("Por favor entre com o nome do Funcionário: ");
    setor = input("Por favor entre com o setor do Funcionário: ");
    salario = float(input("Por favor entre com o salário do Funcionário: "));
    
    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    };
    
    lista_funcionarios.append(copy.deepcopy(funcionario));
    print(f"Funcionário {nome} cadastrado com sucesso!");

def consultar_funcionarios():
    while True:
        print("\n---------- MENU CONSULTAR FUNCIONÁRIO ------------------");
        print("Escolha a opção desejada:");
        print("1 - Consultar Todos os Funcionários");
        print("2 - Consultar Funcionário por id");
        print("3 - Consultar Funcionário(s) por setor");
        print("4 - Retornar ao menu principal");
        opcao = input(">>").strip();
        
        if opcao == '1':
            print("\n----------------");
            for funcionario in lista_funcionarios:
                print(f"id: {funcionario['id']}");
                print(f"nome: {funcionario['nome']}");
                print(f"setor: {funcionario['setor']}");
                print(f"salário: {funcionario['salario']}\n");
            print("----------------");
        
        elif opcao == '2':
            id_consulta = int(input("Digite o id do funcionário: "));
            encontrado = False;
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("\n----------------");
                    print(f"id: {funcionario['id']}");
                    print(f"nome: {funcionario['nome']}");
                    print(f"setor: {funcionario['setor']}");
                    print(f"salario: {funcionario['salario']}");
                    print("----------------");
                    encontrado = True;
                    break;
            if not encontrado:
                print("Id não encontrado.");
        
        elif opcao == '3':
            setor_consulta = input("Digite o setor do(s) funcionário(s): ");
            encontrado = False;
            print("\n----------------");
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == setor_consulta:
                    print(f"id: {funcionario['id']}");
                    print(f"nome: {funcionario['nome']}");
                    print(f"setor: {funcionario['setor']}");
                    print(f"salario: {funcionario['salario']}\n");
                    encontrado = True;
            if not encontrado:
                print("Setor não encontrado.");
            print("----------------");
        
        elif opcao == '4':
            return;
        
        else:
            print("Opção inválida");

def remover_funcionario():
    while True:
        print("\n------------ MENU REMOVER FUNCIONÁRIO ------------------");
        try:
            id_remover = int(input("Digite o id do funcionario a ser removido: "));
            for i, funcionario in enumerate(lista_funcionarios):
                if funcionario['id'] == id_remover:
                    del lista_funcionarios[i]
                    print("Funcionário removido com sucesso!");
                    return;
            print("Id inválido");
        except ValueError:
            print("Entrada inválida, por favor entre com um id numérico.");

if __name__ == "__main__":
    while True:
        print("\n--------------- MENU PRINCIPAL -------------------");
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Funcionário")
        print("2 - Consultar Funcionário(s)")
        print("3 - Remover Funcionário")
        print("4 - Encerrar Programa")
        opcao = input(">>").strip()
        
        if opcao == '1':
            id_global += 1
            cadastrar_funcionario(id_global);
        
        elif opcao == '2':
            consultar_funcionarios();
        
        elif opcao == '3':
            remover_funcionario();
        
        elif opcao == '4':
            print("Encerrando o programa...");
            break
        
        else:
            print("Opção inválida");