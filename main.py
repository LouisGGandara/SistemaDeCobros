from datetime import date, datetime
import tkinter as tk
from tkinter import messagebox

FUENTE_TITULO = ("Arial", 14)
FUENTE_NORMAL = ("Arial", 12)
COLOR_FONDO = "#C8BFE7"
FORMATO_FECHA = "%d/%m/%Y"
CATEGORIAS = ["Computadoras", "Bocinas", "Proyectores", "Cámaras"]
COLORES = [
    "#7F7F7F",
    "#99D9EA",
    "#C8BFE7",
    "#C3C3C3",
    "#00A2E8",
    "#3F48CC",
    "#FFFFFF",
    "#B97A57",
    "#000000",
]

DISPOSITIVOS_INICIALES = [
    ("PC-001", "Dell OptiPlex 3080", "Computadoras"),
    ("PC-002", "HP ProDesk 400", "Computadoras"),
    ("PC-003", "Lenovo ThinkCentre", "Computadoras"),
    ("BOC-001", "JBL Flip 5", "Bocinas"),
    ("BOC-002", "Logitech Z313", "Bocinas"),
    ("PRO-001", "Epson PowerLite", "Proyectores"),
    ("PRO-002", "BenQ MS550", "Proyectores"),
    ("CAM-001", "Canon EOS Rebel T7", "Cámaras"),
    ("CAM-002", "Nikon D3500", "Cámaras"),
]


def dibujar_dispositivo(c, tipo):
    if tipo == "Computadoras":
        c.create_rectangle(5, 10, 35, 80, fill="black")  # torre
        c.create_line(10, 20, 30, 20, fill="white")
        c.create_line(10, 26, 30, 26, fill="white")
        c.create_oval(14, 55, 26, 67, outline="white", width=2)
        c.create_rectangle(42, 12, 105, 60, fill="black")  # monitor
        c.create_rectangle(47, 17, 100, 55, fill="white")
        c.create_rectangle(70, 60, 77, 67, fill="black")
        c.create_rectangle(60, 67, 87, 70, fill="black")
        c.create_rectangle(40, 74, 96, 82, fill="black")  # teclado
        c.create_oval(99, 75, 107, 83, fill="black")  # mouse
    elif tipo == "Bocinas":
        c.create_rectangle(35, 5, 80, 82, fill="black")
        c.create_oval(50, 14, 65, 29, fill="white")
        c.create_oval(42, 40, 73, 71, fill="white")
        c.create_oval(52, 50, 63, 61, fill="black")
    elif tipo == "Proyectores":
        c.create_rectangle(10, 30, 100, 70, fill="black")
        c.create_oval(17, 36, 45, 64, fill="white")
        c.create_oval(24, 43, 38, 57, fill="gray")
        for x in (60, 70, 80, 90):
            c.create_line(x, 40, x, 60, fill="white")
        c.create_rectangle(18, 70, 26, 75, fill="black")
        c.create_rectangle(84, 70, 92, 75, fill="black")
    elif tipo == "Cámaras":
        c.create_rectangle(40, 15, 70, 25, fill="black")
        c.create_rectangle(15, 25, 100, 75, fill="black")
        c.create_oval(40, 31, 78, 69, fill="white")
        c.create_oval(49, 40, 69, 60, fill="black")
        c.create_rectangle(83, 30, 94, 37, fill="white")


def dibujar_avatar(c):
    c.create_oval(5, 5, 75, 75, width=3)
    c.create_oval(28, 16, 52, 40, fill="black")  # cabeza
    c.create_arc(
        20, 44, 60, 84, start=0, extent=180, style="chord", fill="black"
    )  # cuerpo


def dibujar_registro(c):
    oscuro, claro = "#44546A", "#5B9BD5"
    c.create_rectangle(5, 5, 85, 55, fill=oscuro)  # monitor
    c.create_rectangle(10, 10, 80, 50, fill=claro, outline="")
    c.create_line(20, 45, 45, 15, fill="#9DC3E6", width=6)
    c.create_rectangle(40, 55, 50, 65, fill=oscuro)
    c.create_rectangle(28, 65, 62, 69, fill=oscuro)
    c.create_rectangle(70, 20, 104, 69, fill=oscuro)  # tablet
    c.create_rectangle(74, 24, 100, 63, fill=claro, outline="")
    c.create_rectangle(98, 36, 122, 69, fill=oscuro)  # celular
    c.create_rectangle(101, 40, 119, 64, fill=claro, outline="")



def aviso(texto, padre=None):
    messagebox.showinfo("Aviso", texto, parent=padre)


def leer_fecha(texto):
    try:
        return datetime.strptime(texto, FORMATO_FECHA).date()
    except ValueError:
        return None


def crear_titulo(padre, texto):
    tk.Label(
        padre, text=texto, font=FUENTE_TITULO, bd=1, relief="solid", padx=10
    ).pack(anchor="w", padx=15, pady=10)


def crear_campo_entry(padre, texto, fila, estado="normal"):
    tk.Label(padre, text=texto, bg="white").grid(
        row=fila * 2, column=1, sticky="w", padx=10, pady=(8, 0)
    )
    entrada = tk.Entry(padre, width=28, state=estado)
    entrada.grid(row=fila * 2 + 1, column=1, sticky="w", padx=10)
    return entrada


def poner_texto_bloqueado(entrada, texto):
    # Una caja bloqueada (readonly) no acepta texto: se desbloquea, se escribe y se vuelve a bloquear
    entrada.config(state="normal")
    entrada.insert(0, texto)
    entrada.config(state="readonly")


def crear_lista_con_scroll(padre):
    lienzo = tk.Canvas(padre, bg="white", highlightthickness=0)
    barra = tk.Scrollbar(padre, command=lienzo.yview)
    lienzo.config(yscrollcommand=barra.set)
    barra.pack(side="right", fill="y")
    lienzo.pack(side="left", fill="both", expand=True)
    lista = tk.Frame(lienzo, bg="white")
    lienzo.create_window((0, 0), window=lista, anchor="nw")
    lista.bind(
        "<Configure>", lambda e: lienzo.config(scrollregion=lienzo.bbox("all"))
    )
    return lista

# Ventana Principal
class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Préstamo de dispositivos")
        self.config(bg=COLOR_FONDO)
        self.option_add("*Font", FUENTE_NORMAL)

        try:
            self.state("zoomed")
        except tk.TclError:
            self.attributes("-zoomed", True)
        self.resizable(False, False)

        self.dispositivos = []
        for codigo, nombre, tipo in DISPOSITIVOS_INICIALES:
            self.dispositivos.append({
                "codigo": codigo,
                "nombre": nombre,
                "cantidad": 1,
                "tipo": tipo,
                "estado": "Libre",
            })

        self.prestamos = []
        self.siguiente_codigo = 1
        self.categoria_actual = None
        self.dispositivo_elegido = None
        self.historial = None

        self.crear_menu()
        self.crear_buscador()
        self.crear_panel_categorias()
        self.crear_panel_dispositivos()
        self.crear_panel_prestamo()

    def crear_menu(self):
        barra = tk.Menu(self)

        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(
            label="Color de fondo", command=lambda: VentanaColor(self)
        )
        barra.add_cascade(label="Opciones", menu=opciones)

        herramientas = tk.Menu(barra, tearoff=0)
        herramientas.add_command(label="Historial", command=self.abrir_historial)
        herramientas.add_command(
            label="Registro de dispositivo", command=lambda: VentanaRegistro(self)
        )
        barra.add_cascade(label="Herramientas", menu=herramientas)

        acerca = tk.Menu(barra, tearoff=0)
        acerca.add_command(
            label="Información", command=lambda: VentanaInformacion(self)
        )
        barra.add_cascade(label="Acerca de", menu=acerca)

        self.config(menu=barra)

    def abrir_historial(self):
        self.historial = VentanaHistorial(self)

    def crear_buscador(self):
        caja = tk.Frame(self, bg="white", bd=1, relief="solid")
        caja.place(relx=0.02, rely=0.02)
        tk.Label(caja, text="Buscador:", bg="white").pack(side="left", padx=5)

        self.entrada_buscador = tk.Entry(caja, width=20)
        self.entrada_buscador.pack(side="left", padx=5, pady=3)
        self.entrada_buscador.bind("<KeyRelease>", self.filtrar_dispositivos)

    def crear_panel_categorias(self):
        panel = tk.Frame(self, bg="white", bd=1, relief="solid")
        panel.place(relx=0.02, rely=0.08, relwidth=0.20, relheight=0.89)
        for categoria in CATEGORIAS:
            tk.Button(
                panel,
                text=categoria,
                command=lambda c=categoria: self.elegir_categoria(c),
            ).pack(fill="x", padx=15, pady=(10, 0))

    def elegir_categoria(self, categoria):
        self.categoria_actual = categoria
        self.entrada_buscador.delete(0, tk.END)
        self.filtrar_dispositivos()

    def crear_panel_dispositivos(self):
        self.panel_dispositivos = tk.Frame(self, bg="white", bd=1, relief="solid")
        self.lista_dispositivos = crear_lista_con_scroll(self.panel_dispositivos)

    def filtrar_dispositivos(self, event=None):
        texto = self.entrada_buscador.get().strip().lower()

        for widget in self.lista_dispositivos.winfo_children():
            widget.destroy()

        if texto != "":
            for d in self.dispositivos:
                if texto in d["codigo"].lower():
                    self.crear_tarjeta(d)
            self.panel_dispositivos.place(
                relx=0.23, rely=0.08, relwidth=0.40, relheight=0.89
            )
        elif self.categoria_actual:
            for d in self.dispositivos:
                if d["tipo"] == self.categoria_actual:
                    self.crear_tarjeta(d)
            self.panel_dispositivos.place(
                relx=0.23, rely=0.08, relwidth=0.40, relheight=0.89
            )
        else:
            self.panel_dispositivos.place_forget()

    def crear_tarjeta(self, d):
        tarjeta = tk.Frame(
            self.lista_dispositivos, bg="white", bd=1, relief="groove"
        )
        tarjeta.pack(fill="x", padx=10, pady=8)

        imagen = tk.Canvas(
            tarjeta, width=110, height=85, bg="white", highlightthickness=0
        )
        imagen.pack(side="left", padx=10, pady=5)
        dibujar_dispositivo(imagen, d["tipo"])

        if d["estado"] == "Libre":
            imagen.config(cursor="hand2")
            imagen.bind("<Button-1>", lambda e: self.mostrar_prestamo(d))
        else:
            imagen.create_rectangle(
                0, 0, 110, 85, fill="white", outline="", stipple="gray50"
            )

        datos = tk.Frame(tarjeta, bg="white")
        datos.pack(side="left", padx=10)
        for texto in (d["codigo"], d["nombre"], d["estado"]):
            tk.Label(datos, text=texto, bg="white", bd=1, relief="solid", width=25).pack(
                pady=3
            )

    def crear_panel_prestamo(self):
        self.panel_prestamo = tk.Frame(self, bg="white", bd=1, relief="solid")

        avatar = tk.Canvas(
            self.panel_prestamo, width=80, height=80, bg="white", highlightthickness=0
        )
        avatar.grid(row=0, column=0, rowspan=8, sticky="n", padx=15, pady=20)
        dibujar_avatar(avatar)

        self.entrada_nombre = crear_campo_entry(self.panel_prestamo, "Nombre", 0)
        self.entrada_equipo = crear_campo_entry(
            self.panel_prestamo, "Equipo prestado", 1, estado="readonly"
        )
        self.entrada_fecha_prestamo = crear_campo_entry(
            self.panel_prestamo, "Fecha préstamo", 2, estado="readonly"
        )
        self.entrada_fecha_devolucion = crear_campo_entry(
            self.panel_prestamo, "Fecha de devolución (dd/mm/aaaa)", 3
        )

        botones = tk.Frame(self.panel_prestamo, bg="white")
        botones.place(relx=0.5, rely=0.97, anchor="s")
        tk.Button(botones, text="Cancelar", command=self.cancelar_prestamo).pack(
            side="left", padx=10
        )
        tk.Button(botones, text="Guardar", command=self.guardar_prestamo).pack(
            side="left", padx=10
        )

    def mostrar_prestamo(self, dispositivo):
        self.dispositivo_elegido = dispositivo

        self.entrada_nombre.delete(0, tk.END)

        self.entrada_equipo.config(state="normal")
        self.entrada_equipo.delete(0, tk.END)
        self.entrada_equipo.insert(
            0, f"{dispositivo['codigo']} - {dispositivo['nombre']}"
        )
        self.entrada_equipo.config(state="readonly")

        self.entrada_fecha_prestamo.config(state="normal")
        self.entrada_fecha_prestamo.delete(0, tk.END)
        self.entrada_fecha_prestamo.insert(
            0, date.today().strftime(FORMATO_FECHA)
        )
        self.entrada_fecha_prestamo.config(state="readonly")

        self.entrada_fecha_devolucion.delete(0, tk.END)
        self.panel_prestamo.place(
            relx=0.64, rely=0.08, relwidth=0.34, relheight=0.89
        )

    def guardar_prestamo(self):
        nombre = self.entrada_nombre.get().strip()
        texto_fecha = self.entrada_fecha_devolucion.get().strip()
        fecha_prestamo = leer_fecha(self.entrada_fecha_prestamo.get())
        fecha_devolucion = leer_fecha(texto_fecha)

        if nombre == "":
            aviso("El campo Nombre está vacío.", self)
        elif not nombre.replace(" ", "").isalpha():
            aviso("El nombre solo puede contener letras.", self)
        elif texto_fecha == "":
            aviso("El campo Fecha de devolución está vacío.", self)
        elif fecha_devolucion is None:
            aviso("La fecha de devolución debe tener el formato dd/mm/aaaa.", self)
        elif fecha_devolucion <= fecha_prestamo:
            aviso(
                "La fecha de devolución no puede ser igual ni menor a la fecha de"
                " préstamo.",
                self,
            )
        else:
            self.prestamos.append({
                "codigo": self.siguiente_codigo,
                "nombre": nombre,
                "equipo": self.entrada_equipo.get(),
                "fecha_prestamo": fecha_prestamo,
                "fecha_devolucion": fecha_devolucion,
            })
            self.dispositivo_elegido["estado"] = "Prestado"
            aviso(f"Préstamo guardado con el código {self.siguiente_codigo}.", self)
            self.siguiente_codigo += 1

            self.panel_prestamo.place_forget()
            self.filtrar_dispositivos()
            if self.historial and self.historial.winfo_exists():
                self.historial.mostrar_prestamos()

    def cancelar_prestamo(self):
        if messagebox.askyesno(
                "Cancelar", "¿Está seguro de cancelar el préstamo?", parent=self
        ):
            self.panel_prestamo.place_forget()


class VentanaColor(tk.Toplevel):

    def __init__(self, app):
        super().__init__(app)
        self.title("Color")
        self.geometry("400x330")
        self.resizable(False, False)

        crear_titulo(self, "Color")
        marco = tk.Frame(self, bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        rejilla = tk.Frame(marco)
        rejilla.pack(expand=True)

        for i, color in enumerate(COLORES):
            tk.Button(
                rejilla,
                bg=color,
                activebackground=color,
                width=7,
                height=2,
                command=lambda c=color: app.config(bg=c),
            ).grid(row=i // 3, column=i % 3, padx=8, pady=8)


# Historial
class VentanaHistorial(tk.Toplevel):

    def __init__(self, padre):
        super().__init__(padre)
        self.app = padre  # ventana principal, donde se guardan los préstamos
        self.title("Historial")
        self.geometry("430x420")

        crear_titulo(self, "Historial")
        fila = tk.Frame(self)
        fila.pack(anchor="w", padx=20)
        tk.Label(fila, text="Buscador:").pack(side="left")
        self.entrada_buscador = tk.Entry(fila, width=20)
        self.entrada_buscador.pack(side="left", padx=5)
        # Cada vez que se suelta una tecla, se vuelve a filtrar la lista
        self.entrada_buscador.bind("<KeyRelease>", self.mostrar_prestamos)

        marco = tk.Frame(self, bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(5, 20))
        # Lista con barra de desplazamiento para que no se corte si hay muchos préstamos
        self.lista = crear_lista_con_scroll(marco)

        self.mostrar_prestamos()

    def mostrar_prestamos(self, evento=None):
        # Borra las filas que había antes
        for widget in self.lista.winfo_children():
            widget.destroy()

        texto = self.entrada_buscador.get().strip()
        fila = 0
        for prestamo in self.app.prestamos:
            # Filtra por código: solo muestra los que contienen lo escrito
            if texto in str(prestamo["codigo"]):
                tk.Label(self.lista, text=f"Código: {prestamo['codigo']}", bg="white", bd=1,
                         relief="solid", width=15).grid(row=fila, column=0, padx=15, pady=8)
                # p=prestamo hace que cada botón recuerde su propio préstamo
                tk.Button(self.lista, text="✎", bg="#2E75B6", fg="white", width=3,
                          command=lambda p=prestamo: VentanaEditar(self, p)
                          ).grid(row=fila, column=1, padx=5)
                tk.Button(self.lista, text="✖", bg="#C00000", fg="white", width=3,
                          command=lambda p=prestamo: self.borrar(p)
                          ).grid(row=fila, column=2, padx=5)
                fila = fila + 1

        if fila == 0:
            tk.Label(self.lista, text="Sin resultados", bg="white").grid(row=0, column=0,
                                                                         padx=15, pady=8)

    def borrar(self, prestamo):
        respuesta = messagebox.askyesno("Borrar", "¿Desea borrar el préstamo? "
                                                  "Esta acción no se puede deshacer.", parent=self)
        if respuesta:
            self.app.prestamos.remove(prestamo)
            self.mostrar_prestamos()


# Editar el historial
class VentanaEditar(tk.Toplevel):

    def __init__(self, padre, prestamo):
        super().__init__(padre)
        self.prestamo = prestamo
        self.title("Editar")
        self.geometry("460x440")
        self.transient(padre)  # ventana hija
        self.grab_set()  # bloquea el resto del programa mientras esté abierta
        self.protocol("WM_DELETE_WINDOW", lambda: None)  # solo se cierra con los botones

        crear_titulo(self, "Editar")
        marco = tk.Frame(self, bg="white", bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        avatar = tk.Canvas(marco, width=80, height=80, bg="white", highlightthickness=0)
        avatar.grid(row=0, column=0, rowspan=8, sticky="n", padx=15, pady=20)
        dibujar_avatar(avatar)

        # Datos visibles pero no editables
        self.entrada_nombre = crear_campo_entry(marco, "Nombre", 0, "readonly")
        self.entrada_equipo = crear_campo_entry(marco, "Equipo prestado", 1, "readonly")
        self.entrada_fecha_prestamo = crear_campo_entry(marco, "Fecha préstamo", 2, "readonly")
        self.entrada_fecha_devolucion = crear_campo_entry(marco, "Fecha de devolución", 3)

        # fechas guardadas como tal, despu[es convertidas en texto
        poner_texto_bloqueado(self.entrada_nombre, prestamo["nombre"])
        poner_texto_bloqueado(self.entrada_equipo, prestamo["equipo"])
        poner_texto_bloqueado(self.entrada_fecha_prestamo,
                              prestamo["fecha_prestamo"].strftime(FORMATO_FECHA))
        self.entrada_fecha_devolucion.insert(
            0, prestamo["fecha_devolucion"].strftime(FORMATO_FECHA))  # única editable

        botones = tk.Frame(marco, bg="white")
        botones.place(relx=0.5, rely=0.96, anchor="s")
        tk.Button(botones, text="Guardar cambio",
                  command=self.guardar).pack(side="left", padx=10)
        tk.Button(botones, text="Cancelar",
                  command=self.destroy).pack(side="left", padx=10)  # descarta y cierra

    def guardar(self):
        texto = self.entrada_fecha_devolucion.get().strip()

        if texto == "":
            aviso("El campo Fecha de devolución está vacío.", self)
            return

        # Verificación de formato de fecha
        try:
            nueva_fecha = datetime.strptime(texto, FORMATO_FECHA).date()
        except ValueError:
            aviso("La fecha de devolución debe tener el formato dd/mm/aaaa.", self)
            return

        if nueva_fecha < self.prestamo["fecha_prestamo"]:
            aviso("La nueva fecha de devolución no puede ser anterior "
                  "a la fecha de préstamo.", self)
            return

        # Guarda le fecha si está correcta
        self.prestamo["fecha_devolucion"] = nueva_fecha
        self.destroy()


# Registrar un nuevo dispositivo
class VentanaRegistro(tk.Toplevel):

    def __init__(self, padre):
        super().__init__(padre)
        self.app = padre  # ventana principal, donde se guardan los dispositivos
        self.title("Registro de dispositivo")
        self.geometry("480x460")

        crear_titulo(self, "Registro de dispositivo")
        marco = tk.Frame(self, bg="white", bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        imagen = tk.Canvas(marco, width=130, height=75, bg="white", highlightthickness=0)
        imagen.grid(row=0, column=0, rowspan=8, sticky="n", padx=10, pady=20)
        dibujar_registro(imagen)

        self.entrada_nombre = crear_campo_entry(marco, "Nombre", 0)
        self.entrada_codigo = crear_campo_entry(marco, "Código", 1)
        self.entrada_cantidad = crear_campo_entry(marco, "Cantidad", 2)
        self.entrada_tipo = crear_campo_entry(marco, "Tipo", 3)

        botones = tk.Frame(marco, bg="white")
        botones.place(relx=0.5, rely=0.96, anchor="s")

        # Empieza desactivado hasta que todos los campos tengan algo
        self.boton_guardar = tk.Button(botones, text="Guardar cambio", state="disabled",
                                       command=self.guardar)
        self.boton_guardar.pack(side="left", padx=10)
        tk.Button(botones, text="Cancelar",
                  command=self.destroy).pack(side="left", padx=10)  # cierra sin guardar

        # Cada vez que se suelta una tecla en un campo, se revisa si se activa el botón
        self.entrada_nombre.bind("<KeyRelease>", self.revisar_campos)
        self.entrada_codigo.bind("<KeyRelease>", self.revisar_campos)
        self.entrada_cantidad.bind("<KeyRelease>", self.revisar_campos)
        self.entrada_tipo.bind("<KeyRelease>", self.revisar_campos)

    def revisar_campos(self, evento=None):
        if (self.entrada_nombre.get().strip() == ""
                or self.entrada_codigo.get().strip() == ""
                or self.entrada_cantidad.get().strip() == ""
                or self.entrada_tipo.get().strip() == ""):
            self.boton_guardar.config(state="disabled")
        else:
            self.boton_guardar.config(state="normal")

    def guardar(self):
        nombre = self.entrada_nombre.get().strip()
        codigo = self.entrada_codigo.get().strip()
        cantidad = self.entrada_cantidad.get().strip()
        tipo = self.entrada_tipo.get().strip()

        # Verificación de código repetido
        for dispositivo in self.app.dispositivos:
            if dispositivo["codigo"].lower() == codigo.lower():
                aviso("El código ya existe, no se puede repetir.", self)
                return

        # Verificación, número no negativo
        if not cantidad.isdigit() or int(cantidad) <= 0:
            aviso("La cantidad debe ser un número mayor que cero.", self)
            return

        # Agregar dispositivo
        self.app.dispositivos.append({"codigo": codigo, "nombre": nombre,
                                      "cantidad": int(cantidad), "tipo": tipo,
                                      "estado": "Libre"})
        # Actualizar la lista visible de dispositivos
        self.app.filtrar_dispositivos()
        aviso("Dispositivo registrado correctamente.", self)


class VentanaInformacion(tk.Toplevel):

    def __init__(self, app):
        super().__init__(app)

        self.title("Información")
        self.geometry("500x490")
        self.resizable(False, False)

        crear_titulo(self, "Información")

        marco = tk.Frame(
            self,
            bg="white",
            bd=1,
            relief="solid"
        )

        marco.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        tk.Label(
            marco,
            text="SISTEMA DE PRÉSTAMO DE DISPOSITIVOS",
            bg="white",
            font=("Arial", 12, "bold")
        ).pack(pady=(20, 10))

        tk.Label(
            marco,
            text="Versión: 1.0",
            bg="white"
        ).pack()

        tk.Label(
            marco,
            text=(
                "Este sistema permite administrar\n"
                "el préstamo de computadoras,\n"
                "bocinas, proyectores y cámaras."
            ),
            bg="white",
            justify="center"
        ).pack(pady=10)

        tk.Label(
            marco,
            text="Integrantes del equipo:",
            bg="white",
            font=("Arial", 12, "bold")
        ).pack()

        tk.Label(
            marco,
            text=(
                "Joan Santos\n"
                "Didier Otuc\n"
                "Louis Gutierrez-Gandara"
            ),
            bg="white"
        ).pack(pady=10)

        tk.Label(
            marco,
            text="Curso: Programación en Python",
            bg="white"
        ).pack()

        tk.Label(
            marco,
            text="Año: 2025",
            bg="white"
        ).pack(pady=5)

        tk.Button(
            marco,
            text="Cerrar",
            width=15,
            command=self.destroy
        ).pack(pady=20)


if __name__ == "__main__":
    App().mainloop()