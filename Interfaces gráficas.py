from tkinter import *

raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

minombre=StringVar()

cuadroTexto=Entry(miFrame,textvariable=minombre)
cuadroTexto.grid(row=0,column=1,padx=10,pady=20,)

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1,column=1,padx=10,pady=20)
cuadroPass.config(show="x")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1,padx=10,pady=20)

cuadroDirección=Entry(miFrame)
cuadroDirección.grid(row=3,column=1,padx=10,pady=20)

textoComentario=Text(miFrame,width=16, height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=20)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2,sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=20)

nombreApellido=Label(miFrame, text="Apellido:")
nombreApellido.grid(row=2,column=0,sticky="e",padx=10,pady=20)

nombreDirección=Label(miFrame, text="Dirección:")
nombreDirección.grid(row=3,column=0,sticky="e",padx=10,pady=20)

nombrePass=Label(miFrame, text="Password:")
nombrePass.grid(row=1,column=0,sticky="e",padx=10,pady=20)

nombreComentarios=Label(miFrame, text="Comentarios:")
nombreComentarios.grid(row=4,column=0,sticky="e",padx=10,pady=20)

def codigoBoton():

	minombre.set("DOU")

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton)
botonEnvio.pack()

raiz.mainloop()