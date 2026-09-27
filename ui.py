#-------------------------Hecho con IA casi en su totalidad, pero solo es lo visual-----------------------


import tkinter as tk
from tkinter import ttk, messagebox
import logica
import validaciones


class EcoConsumoUI:
    def __init__(self, root: tk.Tk, pila: logica.PilaAparatos):
        self.root = root
        self.pila = pila
        
        self.root.title("ECO-CONSUMO | Análisis de Consumo Eléctrico")
        self.root.geometry("850x620")
        self.root.minsize(750, 550)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.configurar_estilos()
        self.crear_componentes()

    def configurar_estilos(self):
        PRIMARY = "#2e7d32"
        ACCENT = "#1b5e20"
        
        self.style.configure(".", font=("Segoe UI", 10))
        self.style.configure("Header.TLabel", font=("Segoe UI", 16, "bold"), foreground=PRIMARY)
        self.style.configure("SubHeader.TLabel", font=("Segoe UI", 10, "italic"), foreground="#555")
        self.style.configure("TLabelframe.Label", font=("Segoe UI", 10, "bold"), foreground=PRIMARY)
        
        self.style.configure("Primary.TButton", font=("Segoe UI", 9, "bold"), background=PRIMARY, foreground="white")
        self.style.map("Primary.TButton", background=[("active", ACCENT)])
        
        self.style.configure("Danger.TButton", font=("Segoe UI", 9, "bold"), background="#c62828", foreground="white")
        self.style.map("Danger.TButton", background=[("active", "#b71c1c")])

    def crear_componentes(self):
        main_frame = ttk.Frame(self.root, padding="15")
        main_frame.pack(fill=tk.BOTH, expand=True)

        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Label(header_frame, text="ECO-CONSUMO", style="Header.TLabel").pack(anchor=tk.W)
        ttk.Label(header_frame, text="Gestión de consumos basada en Pila (LIFO)", style="SubHeader.TLabel").pack(anchor=tk.W)

        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill=tk.BOTH, expand=True)

        # Formulario
        form_frame = ttk.LabelFrame(content_frame, text=" Registrar Aparato (PUSH) ", padding="15")
        form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        ttk.Label(form_frame, text="Nombre del Aparato:").pack(anchor=tk.W, pady=(0, 2))
        self.ent_nombre = ttk.Entry(form_frame, width=25)
        self.ent_nombre.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="Potencia (Watts):").pack(anchor=tk.W, pady=(0, 2))
        self.ent_potencia = ttk.Entry(form_frame, width=25)
        self.ent_potencia.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="Horas de uso al día (1 - 24):").pack(anchor=tk.W, pady=(0, 2))
        self.ent_horas = ttk.Entry(form_frame, width=25)
        self.ent_horas.pack(fill=tk.X, pady=(0, 10))

        ttk.Label(form_frame, text="Días de uso (1 - 31):").pack(anchor=tk.W, pady=(0, 2))
        self.ent_dias = ttk.Entry(form_frame, width=25)
        self.ent_dias.pack(fill=tk.X, pady=(0, 15))

        btn_push = ttk.Button(form_frame, text="➕ Agregar a Pila (PUSH)", style="Primary.TButton", command=self.btn_push_click)
        btn_push.pack(fill=tk.X, pady=(0, 5))

        # Vista de Pila
        right_frame = ttk.Frame(content_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        list_frame = ttk.LabelFrame(right_frame, text=" Estado Actual de la Pila ", padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        columns = ("pos", "nombre", "potencia", "horas", "dias", "consumo")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=8)

        self.tree.heading("pos", text="N° (Pila)")
        self.tree.heading("nombre", text="Nombre")
        self.tree.heading("potencia", text="Potencia (W)")
        self.tree.heading("horas", text="Horas/Día")
        self.tree.heading("dias", text="Días")
        self.tree.heading("consumo", text="Consumo (kWh)")

        self.tree.column("pos", width=60, anchor=tk.CENTER)
        self.tree.column("nombre", width=120)
        self.tree.column("potencia", width=90, anchor=tk.E)
        self.tree.column("horas", width=80, anchor=tk.E)
        self.tree.column("dias", width=60, anchor=tk.E)
        self.tree.column("consumo", width=110, anchor=tk.E)

        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Botones de Acción
        ops_frame = ttk.LabelFrame(right_frame, text=" Operaciones y Consultas ", padding="10")
        ops_frame.pack(fill=tk.X)

        btn_row1 = ttk.Frame(ops_frame)
        btn_row1.pack(fill=tk.X, pady=2)

        ttk.Button(btn_row1, text="👁️ Peek (Cúspide)", command=self.btn_peek_click).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        ttk.Button(btn_row1, text="🗑️ Pop (Desapilar)", command=self.btn_pop_click).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        ttk.Button(btn_row1, text="⚡ Mayor Consumo", command=self.btn_mayor_consumo_click).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        btn_row2 = ttk.Frame(ops_frame)
        btn_row2.pack(fill=tk.X, pady=2)

        ttk.Button(btn_row2, text="📊 Ver Total Consumo", command=self.btn_total_click).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)
        ttk.Button(btn_row2, text="🧹 Vaciar Pila (Clear)", style="Danger.TButton", command=self.btn_clear_click).pack(side=tk.LEFT, expand=True, fill=tk.X, padx=2)

        self.lbl_status = ttk.Label(main_frame, text="Aparatos en Pila: 0 / Máximo recomendado: 20", font=("Segoe UI", 9, "italic"))
        self.lbl_status.pack(anchor=tk.W, pady=(10, 0))

    def actualizar_tabla(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        aparatos = self.pila.obtener_lista()
        for i, ap in enumerate(reversed(aparatos)):
            idx_pila = len(aparatos) - i
            es_top = " (TOPE)" if i == 0 else ""
            self.tree.insert("", tk.END, values=(
                f"{idx_pila}{es_top}",
                ap["nombre"],
                f"{ap['potencia']:.1f}",
                ap["horas"],
                ap["dias"],
                f"{ap['consumo']:.2f}"
            ))

        self.lbl_status.config(text=f"Aparatos en Pila: {self.pila.size()} | Pila vacía: {'Sí' if self.pila.is_empty() else 'No'}")

    def btn_push_click(self):
        if self.pila.size() >= 20:
            messagebox.showwarning("Límite Alcanzado", "Se ha alcanzado el número máximo sugerido de aparatos (20).")
            return

        ok_nom, res_nom = validaciones.validar_nombre(self.ent_nombre.get())
        if not ok_nom:
            messagebox.showerror("Error de Validación", res_nom)
            return

        ok_pot, res_pot = validaciones.validar_potencia(self.ent_potencia.get())
        if not ok_pot:
            messagebox.showerror("Error de Validación", res_pot)
            return

        ok_hrs, res_hrs = validaciones.validar_horas(self.ent_horas.get())
        if not ok_hrs:
            messagebox.showerror("Error de Validación", res_hrs)
            return

        ok_dias, res_dias = validaciones.validar_dias(self.ent_dias.get())
        if not ok_dias:
            messagebox.showerror("Error de Validación", res_dias)
            return

        aparato = logica.crear_registro_aparato(res_nom, res_pot, res_hrs, res_dias)
        self.pila.push(aparato)

        self.ent_nombre.delete(0, tk.END)
        self.ent_potencia.delete(0, tk.END)
        self.ent_horas.delete(0, tk.END)
        self.ent_dias.delete(0, tk.END)

        self.actualizar_tabla()
        messagebox.showinfo("Éxito", f"Se agregó '{res_nom}' exitosamente a la Pila.")

    def btn_pop_click(self):
        if self.pila.is_empty():
            messagebox.showwarning("Pila Vacía", "No hay aparatos para eliminar.")
            return

        eliminado = self.pila.pop()
        self.actualizar_tabla()
        messagebox.showinfo("Elemento Eliminado (POP)", 
                            f"Se desapiló correctamente el aparato:\n\n"
                            f"• Nombre: {eliminado['nombre']}\n"
                            f"• Consumo: {eliminado['consumo']:.2f} kWh")

    def btn_peek_click(self):
        if self.pila.is_empty():
            messagebox.showwarning("Pila Vacía", "No hay aparatos registrados.")
            return

        ultimo = self.pila.peek()
        messagebox.showinfo("Último Aparato Ingresado (PEEK)", 
                            f"• Nombre: {ultimo['nombre']}\n"
                            f"• Potencia: {ultimo['potencia']} W\n"
                            f"• Uso: {ultimo['horas']} h/día ({ultimo['dias']} días)\n"
                            f"• Consumo Calculado: {ultimo['consumo']:.2f} kWh")

    def btn_total_click(self):
        if self.pila.is_empty():
            messagebox.showwarning("Pila Vacía", "No hay aparatos registrados.")
            return

        total = logica.obtener_total_consumo(self.pila)
        messagebox.showinfo("Consumo Total", f"El consumo total estimado de los {self.pila.size()} aparatos es:\n\n⚡ {total:.2f} kWh")

    def btn_mayor_consumo_click(self):
        mayor = logica.obtener_aparato_mayor_consumo(self.pila)
        if not mayor:
            messagebox.showwarning("Pila Vacía", "No hay aparatos registrados.")
            return

        messagebox.showinfo("Mayor Consumo", 
                            f"El aparato con mayor consumo registrado es:\n\n"
                            f"• Nombre: {mayor['nombre']}\n"
                            f"• Potencia: {mayor['potencia']} W\n"
                            f"• Consumo: {mayor['consumo']:.2f} kWh")

    def btn_clear_click(self):
        if self.pila.is_empty():
            messagebox.showinfo("Información", "La pila ya está vacía.")
            return

        confirm = messagebox.askyesno("Confirmar Vaciado", "¿Está seguro de vaciar todos los aparatos registrados?")
        if confirm:
            self.pila.clear()
            self.actualizar_tabla()
            messagebox.showinfo("Pila Vacía", "Todos los aparatos fueron eliminados de la pila.")