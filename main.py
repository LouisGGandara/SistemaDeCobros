import tkinter as tk
from tkinter import messagebox

# ---------------- Especificaciones ----------------
FUENTE_TITULO = ("Arial", 14)
FUENTE_NORMAL = ("Arial", 12)
COLOR_FONDO = "#C8BFE7"  # lila del diseño

# ---------------- Datos de ejemplo ----------------
# Solo sirven para poder ver las pantallas: (código, nombre, estado)
DISPOSITIVOS = {
    "Computadoras": [("PC-001", "Dell OptiPlex 3080", "Libre"),
                     ("PC-002", "HP ProDesk 400", "Prestado"),
                     ("PC-003", "Lenovo ThinkCentre", "Libre")],
    "Bocinas": [("BOC-001", "JBL Flip 5", "Libre"),
                ("BOC-002", "Logitech Z313", "Prestado")],
    "Proyectores": [("PRO-001", "Epson PowerLite", "Libre"),
                    ("PRO-002", "BenQ MS550", "Libre")],
    "Cámaras": [("CAM-001", "Canon EOS Rebel T7", "Prestado"),
                ("CAM-002", "Nikon D3500", "Libre")],
}
PRESTAMOS = [1, 2, 3, 4]  # códigos de préstamo de ejemplo para el historial


# ---------------- Dibujos (en lugar de imágenes) ----------------
def dibujar_dispositivo(c, categoria):
    if categoria == "Computadoras":
        c.create_rectangle(5, 10, 35, 80, fill="black")              # torre
        c.create_line(10, 20, 30, 20, fill="white")
        c.create_line(10, 26, 30, 26, fill="white")
        c.create_oval(14, 55, 26, 67, outline="white", width=2)
        c.create_rectangle(42, 12, 105, 60, fill="black")            # monitor
        c.create_rectangle(47, 17, 100, 55, fill="white")
        c.create_rectangle(70, 60, 77, 67, fill="black")
        c.create_rectangle(60, 67, 87, 70, fill="black")
        c.create_rectangle(40, 74, 96, 82, fill="black")             # teclado
        c.create_oval(99, 75, 107, 83, fill="black")                 # mouse
    elif categoria == "Bocinas":
        c.create_rectangle(35, 5, 80, 82, fill="black")
        c.create_oval(50, 14, 65, 29, fill="white")
        c.create_oval(42, 40, 73, 71, fill="white")
        c.create_oval(52, 50, 63, 61, fill="black")
    elif categoria == "Proyectores":
        c.create_rectangle(10, 30, 100, 70, fill="black")
        c.create_oval(17, 36, 45, 64, fill="white")
        c.create_oval(24, 43, 38, 57, fill="gray")
        for x in (60, 70, 80, 90):
            c.create_line(x, 40, x, 60, fill="white")
        c.create_rectangle(18, 70, 26, 75, fill="black")
        c.create_rectangle(84, 70, 92, 75, fill="black")
    elif categoria == "Cámaras":
        c.create_rectangle(40, 15, 70, 25, fill="black")
        c.create_rectangle(15, 25, 100, 75, fill="black")
        c.create_oval(40, 31, 78, 69, fill="white")
        c.create_oval(49, 40, 69, 60, fill="black")
        c.create_rectangle(83, 30, 94, 37, fill="white")


def dibujar_avatar(c):
    c.create_oval(5, 5, 75, 75, width=3)
    c.create_oval(28, 16, 52, 40, fill="black")                                  # cabeza
    c.create_arc(20, 44, 60, 84, start=0, extent=180, style="chord", fill="black")  # cuerpo


def dibujar_registro(c):
    oscuro, claro = "#44546A", "#5B9BD5"
    c.create_rectangle(5, 5, 85, 55, fill=oscuro)                     # monitor
    c.create_rectangle(10, 10, 80, 50, fill=claro, outline="")
    c.create_line(20, 45, 45, 15, fill="#9DC3E6", width=6)
    c.create_rectangle(40, 55, 50, 65, fill=oscuro)
    c.create_rectangle(28, 65, 62, 69, fill=oscuro)
    c.create_rectangle(70, 20, 104, 69, fill=oscuro)                  # tablet
    c.create_rectangle(74, 24, 100, 63, fill=claro, outline="")
    c.create_rectangle(98, 36, 122, 69, fill=oscuro)                  # celular
    c.create_rectangle(101, 40, 119, 64, fill=claro, outline="")


# ---------------- Ayudantes ----------------
def crear_titulo(padre, texto):
    tk.Label(padre, text=texto, font=FUENTE_TITULO, bd=1, relief="solid",
             padx=10).pack(anchor="w", padx=15, pady=10)


def crear_campo(padre, texto, fila, estado="normal"):
    # Etiqueta arriba y caja de texto abajo (columna 1; la columna 0 es para la imagen)
    tk.Label(padre, text=texto, bg="white").grid(row=fila * 2, column=1, sticky="w",
                                                 padx=10, pady=(8, 0))
    entrada = tk.Entry(padre, width=25, state=estado)
    entrada.grid(row=fila * 2 + 1, column=1, sticky="w", padx=10)
    return entrada


# =============== VENTANA PRINCIPAL ===============
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Préstamo de dispositivos")
        self.config(bg=COLOR_FONDO)
        self.option_add("*Font", FUENTE_NORMAL)  # Arial 12 para todo lo demás

        # Siempre en pantalla completa, con maximizar bloqueado
        try:
            self.state("zoomed")              # Windows
        except tk.TclError:
            self.attributes("-zoomed", True)  # Linux
        self.resizable(False, False)

        self.crear_menu()
        self.crear_buscador()
        self.crear_panel_categorias()
        self.crear_panel_dispositivos()
        self.crear_panel_prestamo()

    def crear_menu(self):
        barra = tk.Menu(self)

        opciones = tk.Menu(barra, tearoff=0)
        opciones.add_command(label="Color de fondo", command=lambda: VentanaColor(self))
        barra.add_cascade(label="Opciones", menu=opciones)

        herramientas = tk.Menu(barra, tearoff=0)
        herramientas.add_command(label="Historial", command=lambda: VentanaHistorial(self))
        herramientas.add_command(label="Registro de dispositivo",
                                 command=lambda: VentanaRegistro(self))
        barra.add_cascade(label="Herramientas", menu=herramientas)

        acerca = tk.Menu(barra, tearoff=0)
        acerca.add_command(label="Información", command=lambda: VentanaInformacion(self))
        barra.add_cascade(label="Acerca de", menu=acerca)

        self.config(menu=barra)

    def crear_buscador(self):
        fila = tk.Frame(self, bg=COLOR_FONDO)
        fila.place(relx=0.02, rely=0.02)
        tk.Label(fila, text="Buscador:", bg=COLOR_FONDO).pack(side="left")
        self.entrada_buscador = tk.Entry(fila, width=20)
        self.entrada_buscador.pack(side="left", padx=5)

    def crear_panel_categorias(self):
        self.panel_categorias = tk.Frame(self, bg="white", bd=1, relief="solid")
        self.panel_categorias.place(relx=0.02, rely=0.08, relwidth=0.20, relheight=0.89)
        for categoria in DISPOSITIVOS:
            tk.Button(self.panel_categorias, text=categoria,
                      command=lambda c=categoria: self.mostrar_dispositivos(c)
                      ).pack(fill="x", padx=15, pady=(10, 0))

    def crear_panel_dispositivos(self):
        # Se crea vacío; aparece al elegir una categoría
        self.panel_dispositivos = tk.Frame(self, bg="white", bd=1, relief="solid")

    def mostrar_dispositivos(self, categoria):
        for widget in self.panel_dispositivos.winfo_children():
            widget.destroy()

        for codigo, nombre, estado in DISPOSITIVOS[categoria]:
            tarjeta = tk.Frame(self.panel_dispositivos, bg="white", bd=1, relief="groove")
            tarjeta.pack(fill="x", padx=10, pady=8)

            # La imagen funciona como botón para abrir el panel de préstamo
            imagen = tk.Canvas(tarjeta, width=110, height=85, bg="white",
                               highlightthickness=0, cursor="hand2")
            imagen.pack(side="left", padx=10, pady=5)
            dibujar_dispositivo(imagen, categoria)
            imagen.bind("<Button-1>", self.mostrar_prestamo)

            datos = tk.Frame(tarjeta, bg="white")
            datos.pack(side="left", padx=10)
            for texto in (codigo, nombre, estado):
                tk.Label(datos, text=texto, bg="white", bd=1, relief="solid",
                         width=25).pack(pady=3)

        self.panel_dispositivos.place(relx=0.23, rely=0.08, relwidth=0.40, relheight=0.89)

    def crear_panel_prestamo(self):
        # Se crea oculto; aparece al hacer clic en la imagen de un dispositivo
        self.panel_prestamo = tk.Frame(self, bg="white", bd=1, relief="solid")

        avatar = tk.Canvas(self.panel_prestamo, width=80, height=80, bg="white",
                           highlightthickness=0)
        avatar.grid(row=0, column=0, rowspan=8, sticky="n", padx=15, pady=20)
        dibujar_avatar(avatar)

        self.entrada_nombre = crear_campo(self.panel_prestamo, "Nombre", 0)
        self.entrada_equipo = crear_campo(self.panel_prestamo, "Equipo prestado", 1)
        self.entrada_fecha_prestamo = crear_campo(self.panel_prestamo, "Fecha préstamo", 2)
        self.entrada_fecha_devolucion = crear_campo(self.panel_prestamo, "Fecha de devolución", 3)

        botones = tk.Frame(self.panel_prestamo, bg="white")
        botones.place(relx=0.5, rely=0.97, anchor="s")
        tk.Button(botones, text="Cancelar", width=12,
                  command=self.cancelar_prestamo).pack(side="left", padx=10)
        tk.Button(botones, text="Guardar", width=12).pack(side="left", padx=10)

    def mostrar_prestamo(self, evento=None):
        self.panel_prestamo.place(relx=0.64, rely=0.08, relwidth=0.34, relheight=0.89)

    def cancelar_prestamo(self):
        if messagebox.askyesno("Cancelar", "¿Está seguro de cancelar el préstamo?"):
            self.panel_prestamo.place_forget()


# =============== OPCIONES > COLOR DE FONDO ===============
class VentanaColor(tk.Toplevel):
    COLORES = ["#7F7F7F", "#99D9EA", "#C8BFE7",
               "#C3C3C3", "#00A2E8", "#3F48CC",
               "#FFFFFF", "#B97A57", "#000000"]

    def __init__(self, padre):
        super().__init__(padre)
        self.title("Color")
        self.geometry("400x330")
        self.resizable(False, False)  # maximizar bloqueado

        crear_titulo(self, "Color")
        marco = tk.Frame(self, bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        rejilla = tk.Frame(marco)
        rejilla.pack(expand=True)

        for i, color in enumerate(self.COLORES):
            tk.Button(rejilla, bg=color, activebackground=color, width=7,
                      height=2).grid(row=i // 3, column=i % 3, padx=8, pady=8)


# =============== HERRAMIENTAS > HISTORIAL ===============
class VentanaHistorial(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Historial")
        self.geometry("430x420")

        crear_titulo(self, "Historial")
        fila = tk.Frame(self)
        fila.pack(anchor="w", padx=20)
        tk.Label(fila, text="Buscador:").pack(side="left")
        self.entrada_buscador = tk.Entry(fila, width=20)
        self.entrada_buscador.pack(side="left", padx=5)

        marco = tk.Frame(self, bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(5, 20))

        for fila, codigo in enumerate(PRESTAMOS):
            tk.Label(marco, text=f"Código: {codigo}", bd=1, relief="solid",
                     width=15).grid(row=fila, column=0, padx=15, pady=8)
            tk.Button(marco, text="✎", bg="#2E75B6", fg="white", width=3,
                      command=lambda: VentanaEditar(self)).grid(row=fila, column=1, padx=5)
            tk.Button(marco, text="✖", bg="#C00000", fg="white",
                      width=3).grid(row=fila, column=2, padx=5)


# =============== HISTORIAL > EDITAR (ventana hija) ===============
class VentanaEditar(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Editar")
        self.geometry("420x440")
        self.transient(padre)   # ventana hija
        self.grab_set()         # bloquea el resto del programa mientras esté abierta
        self.protocol("WM_DELETE_WINDOW", lambda: None)  # solo se cierra con los botones

        crear_titulo(self, "Editar")
        marco = tk.Frame(self, bg="white", bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        avatar = tk.Canvas(marco, width=80, height=80, bg="white", highlightthickness=0)
        avatar.grid(row=0, column=0, rowspan=8, sticky="n", padx=15, pady=20)
        dibujar_avatar(avatar)

        # Bloqueados (solo lectura). Para escribirles: config(state="normal"),
        # insert(...), y luego config(state="readonly").
        self.entrada_nombre = crear_campo(marco, "Nombre", 0, "readonly")
        self.entrada_equipo = crear_campo(marco, "Equipo prestado", 1, "readonly")
        self.entrada_fecha_prestamo = crear_campo(marco, "Fecha préstamo", 2, "readonly")
        self.entrada_fecha_devolucion = crear_campo(marco, "Fecha de devolución", 3)

        botones = tk.Frame(marco, bg="white")
        botones.place(relx=0.5, rely=0.96, anchor="s")
        tk.Button(botones, text="Guardar cambio").pack(side="left", padx=10)
        tk.Button(botones, text="Cancelar", command=self.destroy).pack(side="left", padx=10)


# =============== HERRAMIENTAS > REGISTRO DE DISPOSITIVO ===============
class VentanaRegistro(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Registro de dispositivo")
        self.geometry("440x440")

        crear_titulo(self, "Registro de dispositivo")
        marco = tk.Frame(self, bg="white", bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))

        imagen = tk.Canvas(marco, width=130, height=75, bg="white", highlightthickness=0)
        imagen.grid(row=0, column=0, rowspan=8, sticky="n", padx=10, pady=20)
        dibujar_registro(imagen)

        self.entrada_nombre = crear_campo(marco, "Nombre", 0)
        self.entrada_codigo = crear_campo(marco, "Código", 1)
        self.entrada_cantidad = crear_campo(marco, "Cantidad", 2)
        self.entrada_tipo = crear_campo(marco, "Tipo", 3)

        botones = tk.Frame(marco, bg="white")
        botones.place(relx=0.5, rely=0.96, anchor="s")
        tk.Button(botones, text="Guardar cambio").pack(side="left", padx=10)
        tk.Button(botones, text="Cancelar", command=self.destroy).pack(side="left", padx=10)


# =============== ACERCA DE > INFORMACIÓN ===============
class VentanaInformacion(tk.Toplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Información")
        self.geometry("400x400")

        crear_titulo(self, "Información")
        marco = tk.Frame(self, bg="white", bd=1, relief="solid")
        marco.pack(fill="both", expand=True, padx=20, pady=(0, 20))
        tk.Label(marco, bg="white",
                 text="Nombres del equipo de desarrollo\n\n"
                      "Integrante 1\nIntegrante 2\nIntegrante 3").pack(expand=True)


if __name__ == "__main__":
    App().mainloop()