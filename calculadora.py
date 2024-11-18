import flet as ft
from flet import colors


#Criando a tela ou pagina.
def main(page: ft.Page):
    
    #Trazendo cor preta para o fundo da tela.
    page.bgcolor = "#000"
    
    #para a tela não ser redimensionada.
    page.window_resizable = False
    
    #Tamanho da tela.
    page.window_width = 250
    page.window_height = 300
    
    #Titulo do aplicativo.
    page.title = 'Calculadora'
    
    #tela ficar visivel.
    page.window_always_on_top = True
    
    #Criando tela de texto.
    result = ft.Text(value= '0', color=colors.WHITE, size=20,)
    
    display = ft.Row(
        width = 250,
        controls =(result),
        alignment = 'end',
    )
    
    btn = ft.Container(
        content=  ft.Text(value= 'AC', color= colors.WHITE),
        width= 50 ,
        height= 50 ,
        bgcolor= colors.BLUE_GREY_100,
        border= 100,
        alignment= ft.alignment.center,
    )

    
    page.add(
        
        display, 
        btn
        
    )
#abrir janela    
ft.app(target= main)