import tkinter as tk


def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)

    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu=menu_inicio)

    menu_inicio.add_command(label='Crear Registro en DB')
    menu_inicio.add_command(label='Eliminar Registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)


class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=500, height=300)
        self.root = root
        self.pack()
        # self.config(bg='blue')
        self.campos_peliculas()
        self.deshabilitar_campos()

    def campos_peliculas(self):
        # Labels de cada campo.
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0 , padx=10 , pady=10)

        self.label_duracion = tk.Label(self, text='Duracion: ')
        self.label_duracion.config(font=('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10 , pady=10)

        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font=('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10 , pady=10)

        #Entradas de cada campo.
        self.mi_nombre = tk.StringVar()
        self.entry_nombre=tk.Entry(self,textvariable=self.mi_nombre)
        self.entry_nombre.config(width=50,font=('Arial',12))
        self.entry_nombre.grid(row=0,column=1,padx=10,pady=10, columnspan = 2)

        self.my_duracion=tk.StringVar()
        self.entry_duracion = tk.Entry(self,textvariable=self.my_duracion)
        self.entry_duracion.config(width=50, font=('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10,columnspan=2)

        self.my_genero=tk.StringVar()
        self.entry_genero = tk.Entry(self,textvariable=self.my_genero)
        self.entry_genero.config(width=50, font=('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10,columnspan=2)

        #Botones
        self.boton_nuevo=tk.Button(self, text='Nuevo',command = self.habilitar_campos)
        self.boton_nuevo.config(width=20,font=('Arial',12,'bold'),
                                fg='#DAD5D6',bg='#158645',
                                cursor='hand2',activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4,column=0,padx=10,pady=10)

        self.boton_guardar = tk.Button(self, text='Guardar')
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'),
                                fg='#DAD5D6', bg='#0E00BD',
                                cursor='hand2', activebackground='#695EF4')
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        self.boton_cancelar = tk.Button(self, text='Cancelar')
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'),
                                  fg='#DAD5D6', bg='#FF0000',
                                  cursor='hand2', activebackground='#F45E5E')
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    #habilitadores
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')
    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.my_duracion.set('')
        self.my_genero.set('')

        self.entry_nombre.config(state='disable')
        self.entry_duracion.config(state='disable')
        self.entry_genero.config(state='disable')


        self.boton_guardar.config(state='disable')
        self.boton_cancelar.config(state='disable')