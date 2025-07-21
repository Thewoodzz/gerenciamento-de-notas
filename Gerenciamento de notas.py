import os 
alunos = {} 

def menu():
    print("MENU PRINCIPAL")
    print("1. Cadastrar novo aluno")
    print("2. Lançar notas")
    print("3. Ver boletim de um aluno")
    print("4. Listar todos os alunos cadastrados")
    print("5. Encerrar o sistema")

def cadastro_aluno():
    nome = input("Digite o nome completo do aluno: ")
    if nome in alunos:
        print("Aluno já cadastrado.")
    else:
        alunos[nome] = []
        print("Aluno cadastrado")

def lancar_notas():
    nome = input("Digite o nome do aluno: ")
    if nome not in alunos:
        print("Aluno não encontrado")
        return

    notas = []
    for cont in range(1, 5):
        nota = float(input(f"Digite a nota {cont} (0 a 10): "))
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um número entre 0 e 10.")
            return

    alunos[nome] = notas
    print("Notas lançadas")

def ver_boletim():
    nome = input("Digite o nome do aluno: ")
    if nome not in alunos:
        print("Aluno não encontrado.")
        return

    notas = alunos[nome]
    if len(notas) != 4:
        print("Notas incompletas para este aluno.")
        return

    media = sum(notas) / 4
    print("BOLETIM")
    print(f"Aluno: {nome}")
    print("Notas:", ", ".join(f"{n:.1f}" for n in notas))
    print(f"Média: {media:.2f}")

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Situação: {situacao}")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("ALUNOS CADASTRADOS")
    for nome in sorted(alunos):
        print(nome)

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastro_aluno()
        elif opcao == "2":
            lancar_notas()
        elif opcao == "3":
            ver_boletim()
        elif opcao == "4":
            listar_alunos()
        elif opcao == "5":
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida.")
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpador

main()
