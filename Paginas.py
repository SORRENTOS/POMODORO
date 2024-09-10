import flet as ft
from clases import *

from firebase import *



import flet as ft

def loginPage(Page):
    # Crear el contenedor fuera de la función de verificación para acceder a él globalmente dentro de esta función
    contenedorDeFields = ft.Container(content=ft.ResponsiveRow([]), bgcolor=ft.colors.RED_400, border_radius=30, margin=ft.margin.only(top=100))

    def verficar_credenciales(e):
        bool,Pomodoros =login(EmailField.value, PasswordField.value)
        if bool:
            # Actualizar solo el contenido del contenedorDeFields
            CorreoUser = ft.Text(value=EmailField.value,text_align=ft.TextAlign.CENTER)
            Iconouser = ft.Icon(name=ft.icons.FACE,size= 50)
            pomodorsDelUsario = ft.Text(value="pomodoros totales: " +str(Pomodoros),text_align=ft.TextAlign.CENTER,)
            Titulo = ft.Text(value="LOS MAS ESTUDIOSOS",text_align=ft.TextAlign.CENTER,size=15)
            TituloContainer = ft.Container(content=Titulo,bgcolor=ft.colors.RED_50,border_radius=10,margin=20)
            ArrayPostLogin =[
                Iconouser,
                CorreoUser,
                pomodorsDelUsario,
                TituloContainer
            ]
            nuevo_contenido = ft.ResponsiveRow(ArrayPostLogin)
            top = obtener_top_usuarios(10)
            for user in top:
                texto_usuario = f" {user['Correo']}, Pomodoros: {user['Pomodoros']}"
                texto_flet = ft.Text(value=texto_usuario,text_align=ft.TextAlign.CENTER)
                fila = ft.Row(controls=[texto_flet])

                contenedor = ft.Container(content= fila,
                padding= 10,border_radius= 10, bgcolor= ft.colors.RED_50, margin= 10)
                nuevo_contenido.controls.append(contenedor)
            contenedorDeFields.content = nuevo_contenido
        else:
            # En caso de fallo, puedes mostrar un mensaje de error o algo similar
            texto.value = "Correo o contraseña incorrectos"
        Page.update()
    texto = ft.Text(value="",color=ft.colors.RED_900,text_align=ft.TextAlign.CENTER)
    EmailField = ft.TextField(label="Email", border_radius=10, border_color=ft.colors.RED_200)
    EmailContaner = ft.Container(content=EmailField, margin=ft.margin.only(top=10, left=20, right=20))
    PasswordField = ft.TextField(label="Password", password=True, border_radius=10, border_color=ft.colors.RED_200)
    PassworConatiner = ft.Container(content=PasswordField, margin=ft.margin.only(top=10, left=20, right=20))
    btnLogin = ft.ElevatedButton(text="Login", bgcolor=ft.colors.RED_300, color=ft.colors.RED_50, on_click=verficar_credenciales)
    btnLoginContainer = ft.Container(content=btnLogin, margin=20)
    
    ArrayDeFields = [
        texto,
        EmailContaner,
        PassworConatiner,
        btnLoginContainer
    ]
    
    contenedorDeFields.content = ft.ResponsiveRow(ArrayDeFields)
  
    # Devolver el contenedor principal con el contenido inicial
    return contenedorDeFields



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

