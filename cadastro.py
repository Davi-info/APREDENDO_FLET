import flet as ft

def main(page: ft.Page):
    
    page.title = "Cadastro"
    
    def cadastrar(e):
        print("chamando")
        
    
    tex_titulo = ft.Text('Titulo do Produto.')
    produto = ft.TextField(label="Digite seu produto....", text_align=ft.TextAlign.LEFT)
    text_preco = ft.Text('Preço do produto.')
    preco = ft.TextField(value="R$: 0.00", label="Digite o preço...", text_align=ft.TextAlign.LEFT)
    btn_cadastro = ft.ElevatedButton('Cadastrar', on_click=cadastrar)
    
    
    page.add(
        
        tex_titulo,
        produto,
        text_preco,
        preco,
        btn_cadastro
        
    )

ft.app(target=main)