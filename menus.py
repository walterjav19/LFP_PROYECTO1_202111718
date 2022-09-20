
from itertools import tee
import tkinter
from tkinter import Entry, ttk,filedialog
from tkinter import messagebox
from tkinter.font import Font
import webbrowser as wb
from analizador_lexico import *
from funcion import Funcion
from generador import Generador

principal=tkinter.Tk()
def inicio():
    principal.title("Menu Principal")
    principal.geometry("500x500")


    curso=tkinter.Label(principal,text="Nombre del curso: Lab Lenguajes Formales y de Programacion")
    curso.place(x=10,y=10)


    nombre=tkinter.Label(principal,text="Nombre del estudiante: Walter Javier Santizo Mazariegos")
    nombre.place(x=10,y=50)

    carne=tkinter.Label(principal,text="Carne del estudiante: 202111718")
    carne.place(x=10,y=90)

    Cargar=tkinter.Button(principal,text="Archivo",command=Archivo)
    Cargar.place(x=200,y=130)

    gestionar=tkinter.Button(principal,text="Help",command=help)
    gestionar.place(x=200,y=170)

    salir=tkinter.Button(principal,text="Salir",command=funcion_salir)
    salir.place(x=200,y=220)

    principal.mainloop()
        

def Archivo():
    global gestionar,entry
    principal.withdraw()
    gestionar=tkinter.Tk()
    gestionar.title("Archivo")
    gestionar.geometry("900x500")
    entry=tkinter.Text(gestionar)
    entry.place(x=0,y=0,width=900,height=300)
    btnListar=tkinter.Button(gestionar,text="abrir",command=abrir)
    btnListar.place(x=200,y=450)
    btnAgregar=tkinter.Button(gestionar,text="guardar",command=guardar)
    btnAgregar.place(x=250,y=450)
    btnEditar=tkinter.Button(gestionar,text="guardar como",command=guardar_como)
    btnEditar.place(x=350,y=450)
    btnEliminar=tkinter.Button(gestionar,text="analizar",command=analizar)
    btnEliminar.place(x=450,y=450)
    btnEliminar=tkinter.Button(gestionar,text="errores",command=generar_repo)
    btnEliminar.place(x=550,y=450)  
    def funcion_regresar_gestionar_principal():
        principal.deiconify()
        gestionar.withdraw()
    Regresar=tkinter.Button(gestionar,text="Regresar",command=funcion_regresar_gestionar_principal)
    Regresar.place(x=650,y=450)    

def generar_repo():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".html")
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Erores lexicos</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>
<table class="default" border="1">
  <tr>
    <th>No.</th>
    <th>Lexema</th>
    <th>Tipo</th>
    <th>Columna</th>
    <th>Linea</th>
  </tr>  
'''
    cuerpo=''''''
    for i in range(len(errores_)):
        cuerpo+='''  <tr>
    <th>'''+str(i+1)+'''</th>
    <th>'''+errores_[i].lexema+'''</th>
    <th>'''+errores_[i].tipo+'''</th>
    <th>'''+str(errores_[i].columna)+'''</th>
    <th>'''+str(errores_[i].fila)+'''</th>
  </tr>'''

    pie='''
    </table>
</body>
</html>'''
    if (f):
        f.write(cabecera+cuerpo+pie)
        f.close ()
        messagebox.showinfo("Aviso","Archivo Generado por favor revise su carpeta")

def abrir():
    global entry,path
    entry.delete(1.0,"end")
    path=filedialog.askopenfilename()
    if(path):
        file=open(path,"r")
        text=file.read()
        file.close()
        entry.insert(1.0,text)


 

def guardar():
    global path,entry
    file=open(path,"w")
    file.write(entry.get(1.0,"end"))
    file.close()
    messagebox.showinfo("Aviso","Su archivo se guardo correctamente")





def guardar_como():
    global entry
    f = filedialog.asksaveasfile(mode='w', defaultextension=".lfp")
    if (f): 
        f.write(entry.get(1.0,"end"))
        f.close()
        messagebox.showinfo("Aviso","Archivo guardado correctamente")


    




    

#version final
def analizar():
    global entry
    errores_.clear()
    f = filedialog.asksaveasfile(mode='w', defaultextension=".html")
    cabecera='''<!DOCTYPE html>
<html lang="en">
<head>
    <title>Erores lexicos</title>
    <link rel="Stylesheet" type="text/css" href="estilo.css">
</head>
<body>
<h1>Generacion de Archivo HTML</h1>
'''
    cuerpo=''''''

    pie='''
</body>
</html>'''
    if (f):
        actualizar_input(entry.get(1.0,"end"))
        variable=parse(entry.get(1.0,"end"))
        getER = True#expresion
        getER2=False#resultado
        # Esta variable nos sirve para determinar si queremos el Resultado o la Expresion Regular
        # True para regresar la expresion regular de la forma (3+4)*5....
        # False para regresar el resultado de la operacion 60
        

        # En el primer for vienen las operaciones como <Tipo>, <Escribir>, <Estilo>
        # En el segundo for vienen los nodos de <Operacion>, Texto de <Escribir>, Texto de <Estilo>
        i=1
        if variable:
            for var in variable:
                if isinstance(var, list):
                    for var_ in var:
                        if var_.ejecutar(getER)!=None and var_.ejecutar(getER2)!=None:
                            cuerpo+='''<h4><p>Operacion '''+str(i)+''':</p></h4>
    <p>'''+str(var_.ejecutar(getER))+'''='''+str(var_.ejecutar(getER2))+'''</p>
    '''         
                        print(var_.ejecutar(getER))
                        print(var_.ejecutar(getER2))
                        i+=1
                elif isinstance(var,Texto):
                    print(var.ejecutar(getER))
                elif isinstance(var,Funcion):
                    print(var.ejecutar(getER))            

        f.write(cabecera+cuerpo+pie)
        f.close ()
        messagebox.showinfo("Aviso","Archivo Generado por favor revise su carpeta")
    
    


def help():
    global gestionar
    principal.withdraw()
    gestionar=tkinter.Tk()
    gestionar.title("Gestionar")
    gestionar.geometry("500x500")
    btnListar=tkinter.Button(gestionar,text="Manual de Usuario",command=abrir_usuario)
    btnListar.place(x=200,y=100)
    btnAgregar=tkinter.Button(gestionar,text="Manual Tecnico",command=abrir_tecnico)
    btnAgregar.place(x=200,y=150)
    btnEditar=tkinter.Button(gestionar,text="Temas de ayuda",command=ayuda)
    btnEditar.place(x=200,y=200)
    def funcion_regresar_gestionar_principal():
        principal.deiconify()
        gestionar.withdraw()
    Regresar=tkinter.Button(gestionar,text="Regresar",command=funcion_regresar_gestionar_principal)
    Regresar.place(x=200,y=300)        

def abrir_usuario():
    wb.open_new("Manual_usuario.pdf")

def abrir_tecnico():
    wb.open_new("Manual_tecnico.pdf")
    
def ayuda():
    messagebox.showinfo("INFORMACION DEL DESARROLADOR","Nombre: WALTER JAVIER SANTIZO MAZARIEGOS\nCarnet: 202111718\nCUI: 2070097670101")    




def ventana_conteo():
    fuente=Font(family="Roboto Cn",size=14)
    principal.withdraw()
    conteo=tkinter.Tk()
    conteo.title("Conteo")
    conteo.geometry("500x500")
    titulo=tkinter.Label(conteo,text="Creditos aprobados, Cursando y pendientes Totales",font=fuente)
    titulo.place(x=30,y=20)
    obligatorios=tkinter.Label(conteo,text="Creditos Aprobados hasta semestre N: ")
    obligatorios.place(x=30,y=140)
    txtCobligatorios=tkinter.Entry(conteo)
    txtCobligatorios.place(x=235,y=140,width=70,height=20)
    Semestre=tkinter.Label(conteo,text="Semestre")
    Semestre.place(x=60,y=180)
    spin1=ttk.Spinbox(conteo,width=10,from_=1,to=10,increment=1)
    spin1.place(x=135,y=180)
    def funcion_regresar_conteo_principal():
        principal.deiconify()
        conteo.withdraw()
    Regresar=tkinter.Button(conteo,text="Regresar",command=funcion_regresar_conteo_principal)
    Regresar.place(x=400,y=400)   

def funcion_salir():
    principal.destroy()
    exit()
    



inicio()