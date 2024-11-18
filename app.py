# Ciar um jogo Pedra, Papel e Tesoura.
# Com Interface grafica.

import random

def joquempo():
    # Opções disponíveis
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    # Computador escolhe uma opção aleatória
    escolha_computador = random.choice(opcoes)
    
    # Usuário faz uma escolha
    escolha_usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

    # Verifica se a escolha do usuário é válida
    if escolha_usuario not in opcoes:
        print("Escolha inválida! Tente novamente.")
        return
    
    print(f"Você escolheu: {escolha_usuario}")
    print(f"Computador escolheu: {escolha_computador}")
    
    # Lógica do jogo
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "Pedra" and escolha_computador == "Tesoura") or \
         (escolha_usuario == "Papel" and escolha_computador == "Pedra") or \
         (escolha_usuario == "Tesoura" and escolha_computador == "Papel"):
        print("Você venceu!")
    else:
        print("Computador venceu!")

# Executa o jogo
joquempo()

