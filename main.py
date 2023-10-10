import tkinter as tk
from tkinter import messagebox


class torresHanoi:
    def __init__(self):
        self.root = tk.Tk()

        self.movimientosTotales = 0

        self.root.geometry("1280x720")  # cambia el tamaño de la ventana
        self.root.title("Torres de Hanoi")  # Cambia el título de la ventana

        self.datoSeleccionado = 0

        self.referencia = [3,2,1]
        self.columnaIzquierda=[3,2,1]
        self.columnaMedia=[]
        self.columnaDerecha=[]
    def mainmenu(self):

        self.datoSeleccionado = 0

        izquierda = tk.Button(self.root, text="",command=self.asignarATorreIzquierda, width=50, height=30,bg='gray', relief=tk.FLAT)
        izquierda.place(relx=.2, rely=0.7, anchor=tk.CENTER)

        media = tk.Button(self.root, text="",command=self.asignarATorreMedia, width=50, height=30,bg='gray', relief=tk.FLAT)
        media.place(relx=.5, rely=0.7, anchor=tk.CENTER)

        derecha = tk.Button(self.root, text="",command=self.asignarATorreDerecha, width=50, height=30,bg='gray', relief=tk.FLAT)
        derecha.place(relx=.8, rely=0.7, anchor=tk.CENTER)

        # Etiquetas
        Menu_label = tk.Label(self.root, text="Torres de hanoi", font=("Helvetica", 15))
        Menu_label.place(relx=0.5, rely=.05, anchor=tk.CENTER)

        self.botonAgregarDatos = tk.Button(self.root, text="3",command=self.seleccionarDisco3, width=30, bg="blue", relief=tk.FLAT)
        self.botonAgregarDatos.place(relx=.20, rely=0.9, anchor=tk.CENTER)

        self.botonAgregarDatos2 = tk.Button(self.root, text="2",command=self.seleccionarDisco2, width=20, bg="red", relief=tk.FLAT)
        self.botonAgregarDatos2.place(relx=.200, rely=0.8, anchor=tk.CENTER)

        self.botonAgregarDatos3 = tk.Button(self.root, text="1",command=self.seleccionarDisco1, width=10, bg="green", relief=tk.FLAT)
        self.botonAgregarDatos3.place(relx=.205, rely=0.7, anchor=tk.CENTER)



        # Las tres listas actualizadas después de las operaciones
        print("Columna Izquierda:", self.columnaIzquierda)
        print("Columna Media:", self.columnaMedia)
        print("Columna Derecha:", self.columnaDerecha)

        self.root.mainloop()

    def revisarOrden(self):
        print("hola")
        if self.columnaMedia == self.referencia or self.columnaDerecha == self.referencia:
            messagebox.showinfo("Logrado", "Ganaste")

    def seleccionarDisco3(self):
        elemento_buscado = 3

        if elemento_buscado in self.columnaIzquierda:
            print(f"{elemento_buscado} seleccionado en columna izquierda")
            self.datoSeleccionado = elemento_buscado
            self.columnaIzquierda.remove(elemento_buscado)
        elif elemento_buscado in self.columnaMedia:
            print(f"{elemento_buscado} seleccionado en columna media")
            self.datoSeleccionado = elemento_buscado
            self.columnaMedia.remove(elemento_buscado)
        elif elemento_buscado in self.columnaDerecha:
            print(f"{elemento_buscado} seleccionado en columna derecha")
            self.datoSeleccionado = elemento_buscado
            self.columnaDerecha.remove(elemento_buscado)
        else:
            print(f"{elemento_buscado} no encontrado en ninguna columna")

    def seleccionarDisco2(self):
        elemento_buscado = 2

        if elemento_buscado in self.columnaIzquierda:
            print(f"{elemento_buscado} seleccionado en columna izquierda")
            self.datoSeleccionado = elemento_buscado
            self.columnaIzquierda.remove(elemento_buscado)
        elif elemento_buscado in self.columnaMedia:
            print(f"{elemento_buscado} seleccionado en columna media")
            self.datoSeleccionado = elemento_buscado
            self.columnaMedia.remove(elemento_buscado)
        elif elemento_buscado in self.columnaDerecha:
            print(f"{elemento_buscado} seleccionado en columna derecha")
            self.datoSeleccionado = elemento_buscado
            self.columnaDerecha.remove(elemento_buscado)
        else:
            print(f"{elemento_buscado} no encontrado en ninguna columna")
    def seleccionarDisco1(self):
        elemento_buscado = 1

        if elemento_buscado in self.columnaIzquierda:
            print(f"{elemento_buscado} seleccionado en columna izquierda")
            self.datoSeleccionado = elemento_buscado
            self.columnaIzquierda.remove(elemento_buscado)

        elif elemento_buscado in self.columnaMedia:
            print(f"{elemento_buscado} seleccionado en columna media")
            self.datoSeleccionado = elemento_buscado
            self.columnaMedia.remove(elemento_buscado)

            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10, bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.5, rely=0.7, anchor=tk.CENTER)
        elif elemento_buscado in self.columnaDerecha:
            print(f"{elemento_buscado} seleccionado en columna derecha")
            self.datoSeleccionado = elemento_buscado

            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10, bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.7, rely=0.7, anchor=tk.CENTER)
            self.columnaDerecha.remove(elemento_buscado)
        else:
            print(f"{elemento_buscado} no encontrado en ninguna columna")

    def asignarATorreIzquierda(self):
        if not self.columnaIzquierda:  # se verifica que la lista esté vacía
            self.columnaIzquierda.append(self.datoSeleccionado)
            # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
            self.valifacionDeHuevaL()

            print("dato insertado en columna izquierda, primer dato")
            self.movimientosTotales += 1

        elif self.datoSeleccionado < self.columnaIzquierda[-1]:  # se verifica que el dato a insertar sea menor que el ultimo en la lista
            self.columnaIzquierda.append(self.datoSeleccionado)
            print("dato insertado en columna izquierda más de 1 dato")

            longitud = len(self.columnaIzquierda)
            print("Valores en la columna derecha " + str(longitud))

            #llamada a método para dibujar boton en caso de haber más de un valor en la columna derecha
            #esto sirve para simular que hay un cilindro encima de otro
            if longitud == 2:
                self.validacionDeHuevaIzquierda2piso()
            if longitud == 3:
                self.validacionDeHuevaIzquierda3piso()
            self.movimientosTotales += 1
        else:
            print("No se puede insertar un disco grande encima de uno pequeño")
        # Las tres listas actualizadas después de las operaciones
        print("Columna Izquierda:", self.columnaIzquierda)
        print("Columna Media:", self.columnaMedia)
        print("Columna Derecha:", self.columnaDerecha)

    def asignarATorreMedia(self):
        if not self.columnaMedia:  # se verifica que la lista esté vacía
            self.columnaMedia.append(self.datoSeleccionado)
            #validacion para posicionar botones en la zona baja de cada torre segun boton presionado
            self.valifacionDeHuevaM()

            print("dato insertado en columna media, primer dato")
            self.movimientosTotales += 1

        elif self.datoSeleccionado < self.columnaMedia[-1]:  # se verifica que el dato a insertar sea menor que el ultimo en la lista
            self.columnaMedia.append(self.datoSeleccionado)

            longitud = len(self.columnaMedia)
            print("Valores en la columna derecha " + str(longitud))

            #llamada a método para dibujar boton en caso de haber más de un valor en la columna derecha
            #esto sirve para simular que hay un cilindro encima de otro
            if longitud == 2:
                self.validacionDeHuevaMedia2piso()
            if longitud == 3:
                self.validacionDeHuevaMedia3piso()


            self.movimientosTotales += 1
        else:
            print("No se puede insertar un disco grande encima de uno pequeño")
        # Las tres listas actualizadas después de las operaciones
        print("Columna Izquierda:", self.columnaIzquierda)
        print("Columna Media:", self.columnaMedia)
        print("Columna Derecha:", self.columnaDerecha)
        self.revisarOrden()

    def asignarATorreDerecha(self):
        if not self.columnaDerecha:  # se verifica que la lista esté vacía
            self.columnaDerecha.append(self.datoSeleccionado)
            print("dato insertado en columna derecha, primer dato")

            #validacion para posicionar botones en la zona baja de cada torre segun boton presionado
            self.validacionDeHuevaR()

            self.movimientosTotales += 1
        elif self.datoSeleccionado < self.columnaDerecha[-1]:  # se verifica que el dato a insertar sea menor que el ultimo en la lista
            self.columnaDerecha.append(self.datoSeleccionado)

            longitud = len(self.columnaDerecha)
            print("Valores en la columna derecha " + str(longitud))

            #llamada a método para dibujar boton en caso de haber más de un valor en la columna derecha
            #esto sirve para simular que hay un cilindro encima de otro
            if longitud == 2:
                self.validacionDeHuevaDerecha2piso()
            if longitud == 3:
                self.validacionDeHuevaDerecha3piso()


            print("dato insertado en columna derecha más de 1 dato")
            self.movimientosTotales += 1
        else:
            print("No se puede insertar un disco grande encima de uno pequeño")
        # Las tres listas actualizadas después de las operaciones
        print("Columna Izquierda:", self.columnaIzquierda)
        print("Columna Media:", self.columnaMedia)
        print("Columna Derecha:", self.columnaDerecha)
        self.revisarOrden()

    def valifacionDeHuevaL(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.2, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.2, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.2, rely=0.90, anchor=tk.CENTER)
    def valifacionDeHuevaM(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.5, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.5, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.5, rely=0.90, anchor=tk.CENTER)

    def validacionDeHuevaR(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.8, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.8, rely=0.90, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.8, rely=0.90, anchor=tk.CENTER)

    def validacionDeHuevaIzquierda2piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.2, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.2, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.2, rely=0.80, anchor=tk.CENTER)
    def validacionDeHuevaMedia2piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.5, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.5, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.5, rely=0.80, anchor=tk.CENTER)

    def validacionDeHuevaDerecha2piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.8, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.8, rely=0.80, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.8, rely=0.80, anchor=tk.CENTER)

    def validacionDeHuevaIzquierda3piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.2, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.2, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.2, rely=0.70, anchor=tk.CENTER)

    def validacionDeHuevaDerecha3piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.8, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.8, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.8, rely=0.70, anchor=tk.CENTER)

    def validacionDeHuevaMedia3piso(self):
        # validacion para posicionar botones en la zona baja de cada torre segun boton presionado
        if self.datoSeleccionado == 1:
            # en caso de haber presionado el boton más pequeño
            self.botonAgregarDatos3.destroy()
            self.botonAgregarDatos3 = tk.Button(self.root, text="1", command=self.seleccionarDisco1, width=10,
                                                bg="green", relief=tk.FLAT)
            self.botonAgregarDatos3.place(relx=.5, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 2:
            # en caso de haber presionado el boton mediano
            self.botonAgregarDatos2.destroy()
            self.botonAgregarDatos2 = tk.Button(self.root, text="2", command=self.seleccionarDisco2, width=20, bg="red",
                                                relief=tk.FLAT)
            self.botonAgregarDatos2.place(relx=.5, rely=0.70, anchor=tk.CENTER)
        elif self.datoSeleccionado == 3:
            # en caso de haber presionado el boton más grande
            self.botonAgregarDatos.destroy()
            self.botonAgregarDatos = tk.Button(self.root, text="3", command=self.seleccionarDisco3, width=30, bg="blue",
                                               relief=tk.FLAT)
            self.botonAgregarDatos.place(relx=.5, rely=0.70, anchor=tk.CENTER)



myMenu = torresHanoi()
myMenu.mainmenu()
