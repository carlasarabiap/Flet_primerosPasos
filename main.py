import flet as ft
import random
from flet_core import MainAxisAlignment, RoundedRectangleBorder, BorderSide
from flet import (
    Column,
    Container,
    border_radius,
    colors,
)

participante = random.randint(0, 2) == 0
jugada = 0
juego = False

def main(page: ft.Page):
    page.title = "TaTeTi"
    page.vertical_alignment = MainAxisAlignment.CENTER

    def modificarBoton(event):
        global participante, jugada, juego
        if participante:
            event.control.text = "X"
            participante = False
            jugada += 1
            event.control.disabled = True
            page.update()
        else:
            event.control.text = "O"
            participante = True
            jugada += 1
            event.control.disabled = True
            page.update()
        if 4 < jugada < 10:
            revisarJugada()

    def reiniciar(event):
        global participante, jugada, juego
        participante = random.randint(0, 2) == 0
        jugada = 0
        juego = False
        boton1.text = "1"
        boton1.disabled = False
        boton2.text = "2"
        boton2.disabled = False
        boton3.text = "3"
        boton3.disabled = False
        boton4.text = "4"
        boton4.disabled = False
        boton5.text = "5"
        boton5.disabled = False
        boton6.text = "6"
        boton6.disabled = False
        boton7.text = "7"
        boton7.disabled = False
        boton8.text = "8"
        boton8.disabled = False
        boton9.text = "9"
        boton9.disabled = False

        t1.visible = False
        t1.value = ""
        page.update()

    def revisarJugada():
        global juego
        #REVISIÓN HORIZONTAL
        if boton1.text == boton2.text and boton1.text == boton3.text:
            t1.value = f"El ganador es {boton1.text}"
            t1.visible = True
            boton4.disabled = True
            boton5.disabled = True
            boton6.disabled = True
            boton7.disabled = True
            boton8.disabled = True
            boton9.disabled = True
            page.add(t1)
            juego = True
        elif boton4.text == boton5.text and boton4.text == boton6.text:
            t1.value = f"El ganador es {boton4.text}"
            t1.visible = True
            boton1.disabled = True
            boton2.disabled = True
            boton3.disabled = True
            boton7.disabled = True
            boton8.disabled = True
            boton9.disabled = True
            page.add(t1)
            juego = True
        elif boton7.text == boton8.text and boton7.text == boton9.text:
            t1.value = f"El ganador es {boton7.text}"
            t1.visible = True
            boton1.disabled = True
            boton2.disabled = True
            boton3.disabled = True
            boton4.disabled = True
            boton5.disabled = True
            boton6.disabled = True
            page.add(t1)
            juego = True
        #REVISIÓN VERTICAL
        if boton1.text == boton4.text and boton1.text == boton7.text:
            t1.value = f"El ganador es {boton1.text}"
            t1.visible = True
            boton2.disabled = True
            boton3.disabled = True
            boton5.disabled = True
            boton6.disabled = True
            boton8.disabled = True
            boton9.disabled = True
            page.add(t1)
            juego = True
        elif boton2.text == boton5.text and boton2.text == boton8.text:
            t1.value = f"El ganador es {boton2.text}"
            t1.visible = True
            boton1.disabled = True
            boton3.disabled = True
            boton4.disabled = True
            boton6.disabled = True
            boton7.disabled = True
            boton9.disabled = True
            page.add(t1)
            juego = True
        elif boton3.text == boton6.text and boton3.text == boton9.text:
            t1.value = f"El ganador es {boton3.text}"
            t1.visible = True
            t1.visible = True
            boton1.disabled = True
            boton2.disabled = True
            boton4.disabled = True
            boton5.disabled = True
            boton7.disabled = True
            boton8.disabled = True
            page.add(t1)
            juego = True
        #REVISIÓN DIAGONAL
        if boton1.text == boton5.text and boton1.text == boton9.text:
            t1.value = f"El ganador es {boton1.text}"
            t1.visible = True
            boton2.disabled = True
            boton3.disabled = True
            boton4.disabled = True
            boton6.disabled = True
            boton7.disabled = True
            boton8.disabled = True
            page.add(t1)
            juego = True
        elif boton3.text == boton5.text and boton3.text == boton7.text:
            t1.value = f"El ganador es {boton3.text}"
            t1.visible = True
            boton1.disabled = True
            boton2.disabled = True
            boton4.disabled = True
            boton6.disabled = True
            boton8.disabled = True
            boton9.disabled = True
            page.add(t1)
            juego = True
        if juego == False and jugada == 9:
            t1.value = "HAY UN EMPATE!!!"
            t1.visible = True
            page.add(t1)

    t = ft.Text(
        value="« Bienvenidos al TaTeTi »",
        size=40,
        color=ft.colors.BLUE_500)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    boton1 = ft.ElevatedButton(
        width=100,
        height=100,
        text="1",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton2 = ft.ElevatedButton(
        width=100,
        height=100,
        text="2",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton3 = ft.ElevatedButton(
        width=100,
        height=100,
        text="3",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton4 = ft.ElevatedButton(
        width=100,
        height=100,
        text="4",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton5 = ft.ElevatedButton(
        width=100,
        height=100,
        text="5",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton6 = ft.ElevatedButton(
        width=100,
        height=100,
        text="6",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton7 = ft.ElevatedButton(
        width=100,
        height=100,
        text="7",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton8 = ft.ElevatedButton(
        width=100,
        height=100,
        text="8",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton9 = ft.ElevatedButton(
        width=100,
        height=100,
        text="9",
        style=ft.ButtonStyle(
            shape=RoundedRectangleBorder(),
            padding=30,
            bgcolor={
                ft.MaterialState.HOVERED: ft.colors.PINK_200,
                ft.MaterialState.DISABLED: ft.colors.PINK_50,
                ft.MaterialState.DEFAULT: ft.colors.PINK_300,
            },
            side={
                ft.MaterialState.HOVERED: BorderSide(3, ft.colors.YELLOW),
            },
        ),
        expand=False,
        on_click=modificarBoton
    )
    boton10 = ft.ElevatedButton(
        text="Reiniciar Juego",
        bgcolor=colors.WHITE,
        color=colors.BLACK87,
        expand=False,
        on_click=reiniciar
    )

    t1 = ft.Text(value="", size=40, visible=False)
    row1 = ft.Row([boton1, boton2, boton3], alignment=MainAxisAlignment.CENTER)
    row3 = ft.Row([boton4, boton5, boton6], alignment=MainAxisAlignment.CENTER)
    row5 = ft.Row([boton7, boton8, boton9], alignment=MainAxisAlignment.CENTER)
    row6 = ft.Row([boton10], alignment=MainAxisAlignment.CENTER)

    page.add(t, row1, row3, row5, row6, t1)

ft.app(target=main)