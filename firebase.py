import firebase_admin
from firebase_admin import credentials, firestore


# Ruta al archivo JSON de credenciales
cred = credentials.Certificate("pomalora-firebase-adminsdk-edbhh-73718cca7e.json")

# Verifica si la app ya está inicializada
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Obtener una referencia a la base de datos Firestore
db = firestore.client()

# Aquí puedes añadir el código para interactuar con la base de datos
# Por ejemplo, leer una colección o un documento específico
usuarios_ref = db.collection('users')
docs = usuarios_ref.stream()
datos_del_usuario = None
logeado = False

def login(Email_log,password_log):
    docs = usuarios_ref.stream()
    global datos_del_usuario 
    print("Verificando login...")
    print ("buscando al usuario ",Email_log)
    for doc in docs:
        correo = doc.get('Correo')
        password = doc.get('password')
        pomodoros = doc.get('Pomodoros')
        if Email_log == correo and password_log ==password:
            print("Usuario encontrado")
            datos_del_usuario = doc.reference #guardar datos usuarios
            logeado =True
            return True,pomodoros
    print("no se encontradron concidencias")
    return False

def SumarPomo_usuario():
    if logeado:
        # Obtener el documento actual
        doc_snapshot = datos_del_usuario.get()
            
            # Obtener el valor actual de Pomodoros
        PomoActuales = doc_snapshot.get('Pomodoros')
        datos_del_usuario.update({
            'Pomodoros': PomoActuales +1
        })

def obtener_top_usuarios(n=5):
    # Obtener los usuarios ordenados por Pomodoros en orden descendente
    top_usuarios = usuarios_ref.order_by('Pomodoros', direction='DESCENDING').limit(n).stream()
    

    lista_top_usuarios = []
    
    for doc in top_usuarios:
        datos = doc.to_dict()  # Convertir el documento a un diccionario
        lista_top_usuarios.append({
            'Correo': datos['Correo'],
            'Pomodoros': datos['Pomodoros']
        })
    
    return lista_top_usuarios

