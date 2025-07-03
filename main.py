alunos = {}
DISCIPLINAS_PERMITIDAS = ['BIOLOGIA', 'FISICA', 'QUIMICA', 'MATEMATICA']

def exibir_menu_principal():
    menu_principal = True
    while menu_principal:
        print("\n=== SISTEMA ESCOLAR ===\n")
        print("1 - Cadastrar alunos")
        print("2 - Matricular alunos em disciplinas")
        print("3 - Lançar notas e frequência de alunos")
        print("4 - Listar desempenho do aluno")
        print("5 - Gerar boletim")
        print("6 - Listar alunos")
        print("7 - Sair\n")

        selecionar_opcao = input("\nInforme o número referente aopção desejada: ")

        try:
            selecionar_opcao = int(selecionar_opcao)
        except:
            print("\nSomente números!")

        if selecionar_opcao == 1:
            cadastrar_aluno()

        elif selecionar_opcao == 2:
            matricular_alunos_disciplinas()

        elif selecionar_opcao == 3:
            notas_frequencias()

        elif selecionar_opcao == 6:
            listar_alunos()

        elif selecionar_opcao == 7:
            menu_principal = False
            print("\nMenu finalizado com sucesso!")


def cadastrar_aluno():
    codigo_registro_aluno = input("\nDigite o código de reistro do aluno: ").strip().upper()

    if codigo_registro_aluno in alunos:
        print("\nAluno já registrado!")

    else:
        nome_aluno = input("\nInforme o nome do aluno: ").title()
        alunos[codigo_registro_aluno] = {
        "Nome do aluno": nome_aluno,
        'Disciplinas': {}}
        
        print("\nAluno cadastrado com sucesso!")


def matricular_alunos_disciplinas():
    if alunos:
        
        i = 1
        print("\n=== LISTA DE ALUNOS ===\n")

        for code, nome in alunos.items():
            print(f"{i} - Código: {code} | Nome do aluno: {nome['Nome do aluno']}")
            i += 1

        selecionar_aluno = input("\nInforme o código do aluno que deseja matricular em uma disciplina: ").strip().upper()
        nome_disciplina = input("\nDigite o nome da disciplina que o aluno será matriculado: ").strip().upper()

        if nome_disciplina in DISCIPLINAS_PERMITIDAS:
            if nome_disciplina not in alunos[selecionar_aluno]:
                alunos[selecionar_aluno]['Disciplinas']= {'Disciplina': nome_disciplina}

                print("\nAluno matriculado com sucesso!")

            else:
                print("\nAluno já cadastrado na disciplina!")
        else:
            print("\nDisciplina inválida!")
    else:
        print("\nSem alunos cadastrados!")


def notas_frequencias():
    if alunos:
        print("\n=== LISTA DE ALUNOS ===\n")

        i = 1
        for code, nome in alunos.items():
            print(f"{i} - Código: {code} | Nome: {nome['Nome do aluno']}")
            i += 1

        selecionar_aluno = input("\nInforme o código do aluno: ").upper().strip()

        if selecionar_aluno in alunos:

                i = 1
                print("\n=== LISTA DE DISCIPLINAS ===\n")

                for code, disciplina in alunos.items():
                    print(f"Disciplina {i} - {disciplina['Disciplinas']}")
                    i += 1

                selecionar_disciplina = input("\nInforme o nome da disciplina para lançamento: ").strip().upper()

                if selecionar_disciplina in DISCIPLINAS_PERMITIDAS:
                    nota_1 = input("\nInforme a nota 01: ")
                    nota_2 = input("Informe a nota 02: ")

                    frequencia = input("\nInforme a frequência total do aluno [SEM CARACTERES ESPECIAIS]: ")

                    try:
                        nota_1 = float(nota_1)
                        nota_2 = float(nota_2)
                        frequencia = float(frequencia)

                    except ValueError:
                        print("\nSomente números!")

                    alunos[selecionar_aluno]['Disciplinas'][selecionar_disciplina]= {
                        'Nota 1': nota_1,
                        'Nota 2': nota_2,
                        'Frequência': frequencia
                    }

                    print("\nNotas lançadas com sucesso!")

                else:
                    print("\nDisciplina inválida!")

        else:
            print("\nEste aluno não foi cadastrado!")


def listar_alunos():
    if alunos:
        print("\n=== LISTA DE ALUNOS ===\n")

        i = 1
        for code, aluno in alunos.items():
            print(f"{i} - {aluno['Nome do aluno']}")
            i += 1
    else:
        print("\nLista de alunos vazia!")
    


exibir_menu_principal()

