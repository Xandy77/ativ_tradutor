import flet as ft
from deep_translator import GoogleTranslator
import asyncio

# Função assíncrona para realizar a tradução
async def traduzir_texto(texto, direcao):
    if direcao == "pt_en":
        return GoogleTranslator(source='pt', target='en').translate(texto)
    else:
        return GoogleTranslator(source='en', target='pt').translate(texto)

def main(page: ft.Page):
    # Função para traduzir a palavra/frase (chamada assíncrona)
    async def traduzir(e):
        texto = entrada_texto.value.strip()
        direcao = direcao_traducao.value

        if texto:
            traducao_resultado = await traduzir_texto(texto, direcao)  # Chama a função assíncrona para tradução
            traducao.value = traducao_resultado
        else:
            traducao.value = "Por favor, insira um texto para traduzir."

        page.update()

    # Configurações da página
    page.title = "Tradutor Simples"
    page.scroll = "adaptive"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Definindo a cor de fundo da página como azul
    page.bgcolor = ft.colors.BLUE  # Cor de fundo azul

    # Campo de entrada para a palavra/frase
    entrada_texto = ft.TextField(label="Texto para traduzir", width=400)

    # Dropdown para selecionar a direção da tradução
    direcao_traducao = ft.Dropdown(
        label="Selecionar direção da tradução",
        options=[
            ft.dropdown.Option("pt_en", "Português para Inglês"),
            ft.dropdown.Option("en_pt", "Inglês para Português")
        ],
        value="pt_en"  # Valor padrão
    )

    # Campo para exibir o resultado da tradução
    traducao = ft.Text(value="", size=20, italic=True)

    # Botão para acionar a tradução
    botao_traduzir = ft.ElevatedButton(text="Traduzir", on_click=lambda e: asyncio.run(traduzir(e)))

    # Layout da página
    page.add(
        ft.Row([ft.Text("Tradutor Simples", size=40, weight="bold", color=ft.colors.WHITE)], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([entrada_texto], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([direcao_traducao], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([botao_traduzir], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([traducao], alignment=ft.MainAxisAlignment.CENTER)
    )

    page.update()

ft.app(main)