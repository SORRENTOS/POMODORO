#clases


#CONTADORES ====================================0
import flet as ft
class Contador(ft.Column):
    def __init__(self,text):
        super().__init__()
        self.label =ft.Container(content= ft.Text(value= text, text_align=ft.TextAlign.RIGHT,color= ft.colors.RED_50))
        
        self.sumarBtn = ft.Container(content=ft.IconButton(ft.icons.ADD, on_click= self.sumar,alignment= ft.alignment.center,bgcolor=ft.colors.RED_300,icon_color=ft.colors.RED_400),margin=ft.margin.only(left=5))
        
        self.Numero =  ft.TextField(value="0",text_align=ft.TextAlign.CENTER,width=50,border_color= ft.colors.RED_400, bgcolor=ft.colors.RED_300,color=ft.colors.RED_50)
        self.numContainer = ft.Container(content=self.Numero)
        self.RestarBtn =ft.Container(content= ft.IconButton(ft.icons.REMOVE, on_click= self.restar,bgcolor=ft.colors.RED_300,icon_color=ft.colors.RED_400),margin=ft.margin.only(left=5))
        self.controls = [
            
            self.label,
            self.sumarBtn,
            self.numContainer,
            self.RestarBtn,

        ]
    def sumar(self,e):
        self.Numero.value = str(int(self.Numero.value) + 1)
        self.update()
    def restar(self,e):
        self.Numero.value = str(int(self.Numero.value) - 1)
        self.update()
#RELOJ==============================
class Reloj(ft.Text):
    def __init__(self):
        super().__init__(value="00:00", size=100,color= ft.colors.RED_50,text_align=ft.TextAlign.CENTER)
        
#TODO CON check

class Tarea(ft.Column):
    #variables globales dentro de la clase:
    
    def __init__(self,textoTarea):
        super().__init__()
        
        #controles
        self.label = ft.Text(textoTarea)
        self.check = ft.Checkbox()
        self.btn = ft.IconButton(icon= ft.icons.EDIT,on_click=self.btn_edit_tarea)
        self.Mostrar = True

    
        elementos_fila = ft.Row(controls=[self.check,self.label,self.btn])

        self.Contenedor = ft.Container(
            content = elementos_fila,
            bgcolor = ft.colors.RED_50,
            border_radius= 10
        )
        #cosas para la descripcion mas detallada
        self.descripcionDetallada = ft.TextField(label="Describe tu tarea",border_color=ft.colors.RED_50,multiline= True)
        self.Icono = ft.Icon(name=  ft.icons.EDIT_NOTE)
        self.labeldesc = ft.Text("Descripcion:")
        self.TituloTarea = ft.Row(controls=[self.Icono,self.labeldesc])
        


            #para unir todo usar ft.column
        self.columnaDetallada = ft.Column(
            controls= [self.TituloTarea,
            self.descripcionDetallada]
        )


        self.ContenedorDetallado = ft.Container(
            content= self.columnaDetallada,
            bgcolor = ft.colors.RED_50,
            border_radius=10,
            padding= 10
            ,visible= False
        )

        

        #conttroles de la clase
        self.controls=[self.Contenedor,self.ContenedorDetallado]
        #funciones del boton editar
    def btn_edit_tarea(self,e):
        if self.Mostrar == True:
            
        
            #como muestro la descripcion
            self.ContenedorDetallado.visible = True
            self.update()
            self.Mostrar = False
        elif self.Mostrar == False:
            self.ContenedorDetallado.visible = False
            self.update()
            self.Mostrar = True
        
    
class TareaCreator(ft.ResponsiveRow):
    def __init__(self):
        super().__init__()
        self.textInput = ft.TextField(label="algo para hacer...", text_align=ft.TextAlign.LEFT)
        self.btn = ft.IconButton(icon=ft.icons.ADD_TASK, bgcolor=ft.colors.RED_300)
        
        self.controls = [self.textInput, self.btn]