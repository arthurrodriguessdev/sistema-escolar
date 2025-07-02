alunos = {}
def exibir_menu_principal():
    menu_principal = True
    while menu_principal:
        print("\n=== SISTEMA ESCOLAR ===\n")
        print("1 - Cadastrar alunos")
        print("2 - Cadastrar disciplinas")
        print("3 - Matricular alunos")
        print("4 - Lançar notas e frequência de alunos")
        print("5 - Listar desempenho do aluno")
        print("6 - Gerar boletim")
        print("7 - Sair\n")

        selecionar_opcao = input("\nInforme o número referente aopção desejada: ")

        try:
            selecionar_opcao = int(selecionar_opcao)
        except:
            print("\nSomente números!")

        if selecionar_opcao == 1:
            cadastrar_aluno()
        
        elif selecionar_opcao == ...:
            menu_principal = False
            print("\nMenu finalizado com sucesso!")


def cadastrar_aluno():
    codigo_registro_aluno = input("\nDigite o código de reistro do aluno: ").strip().upper()

    if codigo_registro_aluno in alunos:
        print("\nAluno já registrado!")

    else:
        nome_aluno = input("\nInforme o nome do aluno: ").title()
        alunos[codigo_registro_aluno] = {"Nome do aluno": nome_aluno}
        print("\nAluno cadastrado com sucesso!")




exibir_menu_principal()