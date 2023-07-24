from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


raiz=Tk()

def abreFichero():
	fichero=filedialog.askopenfilename(title="Abrir archivo", initialdir="C:", filetypes=(("Ficheros de Excel", "*.xlsx"),
		("Ficheros de texto", "*.txt"), ("Todos los ficheros", "*.*")))
	
	print(fichero)

def infoAdicional():
	messagebox.showinfo("Procesador de Mati", "Procesador de textos versión 2019")

def avisoLicensia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirAplicación():
	valor=messagebox.askquestion("Salir de la aplicación", "¿Deseas salir de la aplicación?")

	if valor=="yes":
		raiz.destroy()

#	valor=messagebox.askokcancel("Salir de la aplicación", "¿Deseas salir de la aplicación?")
#	if valor=="true":
#			raiz.destroy()

def cerrarDocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado.")

	if valor==True:
		raiz.destroy()


barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=300, height=300)


archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_command(label="Cerrar", command=cerrarDocumento)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=salirAplicación)


edicionMenu=Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")


herramientasMenu=Menu(barraMenu, tearoff=0)


ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=avisoLicensia)
ayudaMenu.add_separator()
ayudaMenu.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

raiz.mainloop()