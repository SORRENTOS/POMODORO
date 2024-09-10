from clases import *
from Paginas import *
import time
#from firebase import *


 #sound = AudioSegment.from_file("assets/ding.wav")
sonido = ft.Audio(src = "/home/benjamin/Escritorio/pruebasFlet/app/assets/ding.mp3")
trabajando = True
def DetenerPomodoro(timer):
        print("DETENIENDO POMODORO")
        global trabajando
        trabajando = False
        timer.value = "00:00"
def EmpezarPomodoro(work_t,rest_t,cycles,timer):

    print("EMPEZANDO POMODORO")
    
    global trabajando
    trabajando = True
    x =0
    while x < int(cycles):
        if trabajando:
            sonido.play()
        segundos = 0
        minutos = int(work_t)
        for i in range (int(work_t)* 60):
            if trabajando== True:
                timer.value = f"{minutos:02}:{segundos:02}"
                time.sleep(1)
                if(segundos > 0):
                    segundos -=1
                elif(segundos == 0):
                    segundos = 59
                    minutos -=1 
                timer.update()
            else:
                break
        segundos = 0
        minutos = int(rest_t)
        if trabajando:
            sonido.play()
        print("EMPEZANDO DESCANZO")
        for i in range (int(rest_t)* 60):
            if trabajando== True:
                timer.value = f"{minutos:02}:{segundos:02}"
                time.sleep(1)
                if(segundos > 0):
                    segundos -=1
                elif(segundos == 0):
                    segundos = 59
                    minutos -=1
                timer.update()
            else:
                break
        SumarPomo_usuario()
        x += 1 # sumo un ciclo


def main(page: ft.Page):
   #cambia pagina
    def cambiarpag(e):
        index = e.control.selected_index
        todo_pag.visible= True if index == 1 else False
        todo.visible =True if index == 0 else False
        login_pag.visible = True if index == 2 else False
        page.update()
    

    
    #barra de busqueda
    page.navigation_bar = ft.NavigationBar(
        bgcolor = ft.colors.RED_400,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.WORK,label="work"),
            ft.NavigationDestination(icon =ft.icons.EDIT,label ="Todo list"),
            ft.NavigationDestination(icon=ft.icons.SPORTS_SCORE,label= "Users")
        ],
        on_change=cambiarpag

    )
    #PAGINAS

    #pagina todo
    todo_pag= TodoPage(page)
    todo_pag.visible =False

    #pagina login/perfil
    login_pag= loginPage(page)
    login_pag.visible = False


    #opciones de la pagina
    page.controls.clear()
    page.bgcolor = ft.colors.RED_100
    
    page.window_width = 360
    page.window_height = 560
    page.title = "POMALORA"
    
    #instancia de controladores
    work = Contador(text="Work")
    rest =Contador(text="Rest")
    Cylces = Contador(text="Cycles")
  
    tiempo = Reloj()
    #botones
    btnStart = ft.ElevatedButton(text="START", on_click= lambda e:EmpezarPomodoro(work.Numero.value,rest.Numero.value,Cylces.Numero.value,tiempo),bgcolor=ft.colors.RED_300,color= ft.colors.RED_50)
    btnStop = ft.ElevatedButton(text="STOP", on_click=lambda e: DetenerPomodoro(tiempo),bgcolor=ft.colors.RED_300,color= ft.colors.RED_50)
    
    #contenedores
    controlsTiempo=[ 
           work,
           rest,
           Cylces,

        ]
    ArraydeBotones =[
        btnStart,
        btnStop
    ]
    opcionesTiempoFondo= ft.Container(content=None,bgcolor= ft.colors.RED_400,border_radius=30,height=220,margin= ft.margin.only(top=30),adaptive=False)
    opcionesTiempo = ft.Container(content= ft.Row(controlsTiempo,alignment= ft.MainAxisAlignment.CENTER),alignment= ft.alignment.center,adaptive=False,margin= ft.margin.only(top=30))
    stackOpciones = ft.Stack([opcionesTiempoFondo,opcionesTiempo],adaptive=True)
    Temporizador = ft.Container(content= tiempo,bgcolor=ft.colors.RED_400,border_radius=30,height=150,width=350,adaptive=True)
    Botones = ft.Container(content= ft.Row(ArraydeBotones,alignment= ft.MainAxisAlignment.CENTER))


    #TODO EL ECONTENIDO
    arraycontenido = [stackOpciones, Temporizador,Botones]
    todo = ft.ResponsiveRow(arraycontenido)
    page.overlay.append(sonido)
    page.add(
       todo,
       todo_pag,
       login_pag
       
    )
    
    

    

ft.app(main)
