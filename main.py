import tkinter as tk
from tkinter import messagebox


def main():


    #Colores de items
    COLOR_FONDO = "#f0f0f0"  # Gris claro
    COLOR_BOTONES = "#4CAF50"  # Verde
    COLOR_TEXTO_BOTONES = "white"
    COLOR_ENTRADA = "white"
    COLOR_RESULTADO = "#e0e0e0"  # Gris más oscuro

    #Tipos de fuente de letra
    FUENTE_TITULO = ("Helvetica", 16, "bold")
    FUENTE_NORMAL = ("Helvetica", 12)
    FUENTE_BOTONES = ("Helvetica", 12, "bold")


    def lista_contigua():
        ventana_contigua = tk.Toplevel(root)
        ventana_contigua.title("Lista Contigua")
        ventana_contigua.geometry("400x300")
        ventana_contigua.configure(bg=COLOR_FONDO)

        label_n = tk.Label(ventana_contigua, text="Ingrese el número de elementos (máximo 10):")
        label_n.pack(pady=5)
        entry_n = tk.Entry(ventana_contigua)
        entry_n.pack(pady=5)

        elementos = []

        def ingresar_elementos():
            n = int(entry_n.get())  
            if n > 10:
                messagebox.showerror("Error", "El número máximo de elementos es 10.")
                return

            elementos.clear()

            for i in range(n):
                label_elemento = tk.Label(ventana_contigua, text=f"Ingrese el elemento {i}:")
                label_elemento.pack(pady=2)
                entry_elemento = tk.Entry(ventana_contigua)
                entry_elemento.pack(pady=2)
                elementos.append(entry_elemento) 
     
            boton_mostrar = tk.Button(ventana_contigua, text="Mostrar Lista", command=mostrar_lista)
            boton_mostrar.pack(pady=10)
 
        def mostrar_lista():
            lista = []
            for entry in elementos:
                valor = entry.get() 
                lista.append(valor)

            resultado_text.delete(1.0, tk.END)  
            resultado_text.insert(tk.END, "Lista Contigua: " + " ".join(lista))

        marco = tk.Frame(ventana_contigua, bg=COLOR_FONDO)
        marco.pack(pady=20)

        label_valor = tk.Label(marco, text="Ingrese un valor:", )

        boton_ingresar = tk.Button(ventana_contigua, text="Ingresar Elementos", command=ingresar_elementos)
        boton_ingresar.pack(pady=10)
        
    def lista_ligada():
        ventana_ligada = tk.Toplevel(root)
        ventana_ligada.title("Lista Ligada")
        ventana_ligada.geometry("400x300")

        nodos = []
        cabeza = -1  

       
        def ingresar_elemento():
            nonlocal cabeza
            valor = entry_valor.get()  
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

            
            nuevo_nodo = [valor, cabeza]  
            nodos.append(nuevo_nodo)
            cabeza = len(nodos) - 1 
           
            entry_valor.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista ligada.")

        def mostrar_lista():
            resultado_text.delete(1.0, tk.END) 
            if cabeza == -1:
                resultado_text.insert(tk.END, "La lista ligada está vacía.")
                return

            resultado = "Lista Ligada: "
            actual = cabeza
            while actual != -1:
                resultado += str(nodos[actual][0]) + " -> "
                actual = nodos[actual][1]
            resultado += "NULL"
            resultado_text.insert(tk.END, resultado)

        label_valor = tk.Label(ventana_ligada, text="Ingrese un valor:")
        label_valor.pack(pady=5)
        entry_valor = tk.Entry(ventana_ligada)
        entry_valor.pack(pady=5)

        boton_ingresar = tk.Button(ventana_ligada, text="Ingresar Elemento", command=ingresar_elemento)
        boton_ingresar.pack(pady=10)

        boton_mostrar = tk.Button(ventana_ligada, text="Mostrar Lista Ligada", command=mostrar_lista)
        boton_mostrar.pack(pady=10)

    def lista_doblemente_ligada():
        ventana_doble = tk.Toplevel(root)
        ventana_doble.title("Lista Doblemente Ligada")
        ventana_doble.geometry("400x300")

        nodos = []
        cabeza = -1  
        cola = -1    

        def ingresar_elemento():
            nonlocal cabeza, cola
            valor = entry_valor.get()  
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

           
            nuevo_nodo = [valor, cabeza, -1]  
            nodos.append(nuevo_nodo)

            if cabeza != -1:
                nodos[cabeza][2] = len(nodos) - 1

            cabeza = len(nodos) - 1

            if cola == -1:
                cola = cabeza

            entry_valor.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista doblemente ligada.")

        def mostrar_lista():
            resultado_text.delete(1.0, tk.END)  
            if cabeza == -1:
                resultado_text.insert(tk.END, "La lista doblemente ligada está vacía.")
                return

            resultado = "Lista Doblemente Ligada (de cabeza a cola): "
            actual = cabeza
            while actual != -1:
                resultado += str(nodos[actual][0]) + " <-> "
                actual = nodos[actual][1]
            resultado += "NULL\n"

            resultado += "Lista Doblemente Ligada (de cola a cabeza): "
            actual = cola
            while actual != -1:
                resultado += str(nodos[actual][0]) + " <-> "
                actual = nodos[actual][2]
            resultado += "NULL"
            resultado_text.insert(tk.END, resultado)

        label_valor = tk.Label(ventana_doble, text="Ingrese un valor:")
        label_valor.pack(pady=5)
        entry_valor = tk.Entry(ventana_doble)
        entry_valor.pack(pady=5)

        boton_ingresar = tk.Button(ventana_doble, text="Ingresar Elemento", command=ingresar_elemento)
        boton_ingresar.pack(pady=10)

        boton_mostrar = tk.Button(ventana_doble, text="Mostrar Lista Doblemente Ligada", command=mostrar_lista)
        boton_mostrar.pack(pady=10)


    def lista_indexada():
        ventana_indexada = tk.Toplevel(root)
        ventana_indexada.title("Lista Indexada")
        ventana_indexada.geometry("500x400")
        ventana_indexada.configure(bg=COLOR_FONDO)

        valores = []
        indices = [] 

        def ingresar_elemento():
            valor = entry_valor.get() 
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

           
            indices.append(len(valores)) 
            valores.append(valor)

            
            entry_valor.delete(0, tk.END)
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista indexada.")

      
        def mostrar_lista():
            resultado_text.delete(1.0, tk.END) 
            if not valores:
                resultado_text.insert(tk.END, "La lista indexada está vacía.")
                return

            resultado = "Lista Indexada:\n"
            for i in range(len(valores)):
                resultado += f"Índice: {indices[i]} -> Valor: {valores[i]}\n"
            resultado_text.insert(tk.END, resultado)

        marco = tk.Frame(ventana_indexada, bg=COLOR_FONDO)
        marco.pack(pady=20)

        label_valor = tk.Label(marco, text="Ingrese un valor:", font=FUENTE_NORMAL, bg=COLOR_FONDO)
        label_valor.grid(row=0, column=0, padx=10, pady=10)

        entry_valor = tk.Entry(marco, font=FUENTE_NORMAL, bg=COLOR_ENTRADA, relief="flat", bd=2)
        entry_valor.grid(row=0, column=1, padx=10, pady=10)

        boton_ingresar = tk.Button(marco, text="Ingresar Elemento", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command=ingresar_elemento)
        boton_ingresar.grid(row=1, column=0, columnspan=2, pady=10)

        boton_mostrar = tk.Button(marco, text="Mostrar Lista Indexada", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command=mostrar_lista)
        boton_mostrar.grid(row=2, column=0, columnspan=2, pady=10)

        resultado_text = tk.Text(ventana_indexada, font=FUENTE_NORMAL, bg=COLOR_RESULTADO, relief="flat", bd=2, height=10, width=50)
        resultado_text.pack(pady=20)

   #Ventana principal
    root = tk.Tk()
    root.title("Simulación de Listas")
    root.geometry("600x500")
    root.configure(bg=COLOR_FONDO)
  
    titulo = tk.Label(root, text="Simulación de Listas", font=FUENTE_TITULO, bg=COLOR_FONDO)
    titulo.pack(pady=20)
   
    marco_botones = tk.Frame(root, bg=COLOR_FONDO)
    marco_botones.pack(pady=20)

    button_contigua = tk.Button(marco_botones, text="1. Lista Contigua", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command = lista_contigua)
    button_contigua.grid(row=0, column=0, padx=10, pady=10)

    button_ligada = tk.Button(marco_botones, text="2. Lista Ligada", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command=lista_ligada)
    button_ligada.grid(row=0, column=1, padx=10, pady=10)

    button_doblemente_ligada = tk.Button(marco_botones, text="3. Lista Doblemente Ligada", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command=lista_doblemente_ligada)
    button_doblemente_ligada.grid(row=1, column=0, padx=10, pady=10)

    button_indexada = tk.Button(marco_botones, text="4. Lista Indexada", font=FUENTE_BOTONES, bg=COLOR_BOTONES, fg=COLOR_TEXTO_BOTONES, relief="flat", command=lista_indexada)
    button_indexada.grid(row=1, column=1, padx=10, pady=10)

    button_salir = tk.Button(marco_botones, text="5. Salir", font=FUENTE_BOTONES, bg="#f44336", fg=COLOR_TEXTO_BOTONES, relief="flat", command=root.quit)
    button_salir.grid(row=2, column=0, columnspan=2, pady=20)

    resultado_text = tk.Text(root, font=FUENTE_NORMAL, bg=COLOR_RESULTADO, relief="flat", bd=2, height=10, width=50)
    resultado_text.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()