import flet as ft
from clases import *

from firebase import *



import flet as ft

#DATA USER
pomodoros = 100

def loginPage(Page):

    IconoUsarario = ft.Container(content=ft.Icon(name=ft.icons.PERSON,size=50),alignment=ft.alignment.center)
    NombreUsuario = ft.TextField(value="usuario",border_color=ft.colors.RED_50,text_align=ft.TextAlign.CENTER)
    Numero_pomodoros = ft.Container(content=ft.Text(value="Pomodoros Totales: "+str(pomodoros)),margin=ft.margin.all(5),bgcolor=ft.colors.RED_100,border_radius=10,padding=10)
    Tiempo_de_estudio = ft.Container(content=ft.Text(value = "Tiempo de estudio: 0"),margin=ft.margin.all(5),bgcolor=ft.colors.RED_100,border_radius=10,padding=10)
    userdata = ft.Column([IconoUsarario,NombreUsuario,Numero_pomodoros,Tiempo_de_estudio],alignment=ft.alignment.center)

    contendorFondoUsario = ft.Container(content= None,bgcolor= ft.colors.RED_50,height=250,border_radius=10)

    stackUsuario = ft.Stack([contendorFondoUsario,userdata])
    contenedor = ft.ResponsiveRow([stackUsuario])


    return contenedor
    



def TodoPage(page):
    

    def click(e):
        if todo.textInput.value != "":
            contenedor.controls.append(Tarea(todo.textInput.value))
            todo.textInput.value = ""
        page.update()

    todo = TareaCreator()
    TODO = ft.ResponsiveRow([todo])
    contenedor = ft.Column([ft.Container(content=TODO,margin=ft.margin.only(top=20))])
    todo.btn.on_click=click
    
    
    return contenedor

