USUARIO_CORRETO = "aluno"
SENHA_CORRETA = "1234"
TENTATIVAS_MAXIMAS = 3
tentativas_restantes = TENTATIVAS_MAXIMAS
acesso_concedido = False
while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}")
    usuario_digitado = input("Usuário: ")
    senha_digitada = input("Senha: ")

    if usuario_digitado == USUARIO_CORRETO and senha_digitada == SENHA_CORRETA:
        acesso_concedido = True
        break 
    else:
        print("Usuário ou senha incorretos.\n")
        tentativas_restantes -= 1

if not acesso_concedido:
    print("ERRO: Conta bloqueada. Você excedeu o número de tentativas permitidas.")
else:
    print("\nAcesso concedido! Bem-vindo ao sistema de notas.\n")


    notas = []
    quantidade_notas = 0
  
    while True:
        try:
            nota_input = input(f"Digite a nota {quantidade_notas + 1} (ou 's' para sair): ")
            
            if nota_input.lower() == 's':
                break  
            
            nota = float(nota_input)
            if 0 <= nota <= 100:
                notas.append(nota)
                quantidade_notas += 1
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 100.\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número ou 's' para sair.\n")
            
 
    if quantidade_notas > 0:
        soma_notas = sum(notas)
        media = soma_notas / quantidade_notas
        print("-" * 30)
        print(f"Notas inseridas: {notas}")
        print(f"Total de notas: {quantidade_notas}")
        print(f"Média das notas: {media:.2f}")
        print("-" * 30)
    else:
        print("Nenhuma nota foi inserida. A média não pode ser calculada.")