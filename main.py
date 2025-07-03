alunos = {}
lista_disciplinas = []

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
        print("7 - Listar alunos")
        print("8 - Sair\n")

        selecionar_opcao = input("\nInforme o número referente aopção desejada: ")

        try:
            selecionar_opcao = int(selecionar_opcao)
        except:
            print("\nSomente números!")

        if selecionar_opcao == 1:
            cadastrar_aluno()
        
        elif selecionar_opcao == 2:
            cadastrar_disciplinas()

        elif selecionar_opcao == 3:
            matricular_alunos()

        elif selecionar_opcao == 7:
            listar_alunos()

        elif selecionar_opcao == 8:
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


def cadastrar_disciplinas():
    nome_disciplina = input("\nInforme o nome da disciplina que deseja cadastrar: ").upper().strip()
    lista_disciplinas.append(nome_disciplina)

    print("\nDisciplina cadastrada com sucesso!")


def matricular_alunos():
    if lista_disciplinas:

        if alunos:
            print("\n=== LISTA DE ALUNOS ===\n")
            i = 1

            for code, aluno in alunos.items():
                print(f"{i} - Nome: {code['Nome do aluno']} | Código: {code}")
                i += 1

            selecionar_codigo_aluno = input("n\Informe o código do aluno que deseja realizar cadastrosde disciplinas: ").upper()

            if selecionar_codigo_aluno in alunos:
                i = 1

                for lista in lista_disciplinas:
                    print(f"{i} - {lista}")
                    i += 1

                selecionar_disciplina = input("\nInforme o número referente a disciplina que deseja cadastrar aluno: ").upper().strip()

                try:
                    selecionar_disciplina = int(selecionar_disciplina)
                    selecionar_disciplina -= 1
                except ValueError:
                    print("\nSomente números!")

                if 0 <= selecionar_disciplina and selecionar_disciplina <= len(lista_disciplinas):
                    alunos[selecionar_codigo_aluno] = {'Disciplina': lista_disciplinas}
                    print("\nAluno matriculado com sucesso!")

                else:
                    print("\Disciplina inválida!")
            else:
                print("\nCódigo de aluno inválido!")
        else:
            print("\nLista de alunos vazia!")
    else:
        print("\nLista de disciplinas vazia!")
    
def notas_frequencias():
    if alunos:
        print("\n=== LISTA DE ALUNOS ===\n")

        i = 1
        for code, nome in alunos.items():
            print(f"{i} - Código: {code} | Nome: {code['Nome do aluno']}")
            i += 1

        selecionar_codigo = input("\nInforme o código do aluno: ").upper().strip()

        if selecionar_codigo in alunos:
            if 'Disciplina' in alunos[selecionar_codigo]:
                print("\n=== DISCIPLINAS DO ALUNO ===\n")

                for disciplina in disciplina[selecionar_codigo]['Diciplina']:
                    print(f"Disciplina {i} - {disciplina['Nome da disciplina']}")
                    i += 1
                
                selecionar_disciplina = input("\nInforme o nome da disciplina que serão lançadas as notas e frequências: ").strip().upper()

                if selecionar_disciplina in alunos[selecionar_codigo]['Disciplina']:
                    nota_1 = input("\nDigite a primeira nota do aluno: ")
                    nota_2 = input("\Digite a segunda nota do aluno: ")

                    try:
                        nota_1 = float(nota_1)
                        nota_2 = float(nota_2)
                    except:
                        print("\nSomente números!")

                    media_final =(nota_1 + nota_2) / 2
                else:
                    print("\nDisciplina não encontrada para este aluno!")
            else:
                print("\nO aluno não possui cadastro em nenhuma matéria!")
            
        else:
            print("\nAluno não encontrado!")
    else:
        print("\nLista de alunos vazia!")






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

