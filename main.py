import flet as ft
import random

def main(page: ft.Page):
    
    opcao = ['pedra', 'papel', 'tesoura']
    
    def jogar(e):
        escolha_comput = random.choice(opcao)
        escolha_jogador = player.value.lower()

        if escolha_jogador not in opcao:
            resultado.value = "Escolha inválida! Tente novamente."
        else:
            if escolha_jogador == escolha_comput:
                vencedor = "Empate!"
            elif (escolha_jogador == 'pedra' and escolha_comput == 'tesoura') or \
                 (escolha_jogador == 'papel' and escolha_comput == 'pedra') or \
                 (escolha_jogador == 'tesoura' and escolha_comput == 'papel'):
                vencedor = "Você venceu!"
            else:
                vencedor = "O computador venceu!"

            resultado.value = f'Sua escolha: {escolha_jogador}. Escolha do computador: {escolha_comput}. {vencedor}'

        page.update()

    page.title = 'Jogo Joquempô'
    
    player = ft.TextField(label='Escolha pedra, papel ou tesoura:', text_align=ft.TextAlign.LEFT)
    jogar_btn = ft.ElevatedButton("Jogar", on_click=jogar)
    resultado = ft.Text()

    page.add(
        player,
        jogar_btn,
        resultado
    )

ft.app(target=main)
