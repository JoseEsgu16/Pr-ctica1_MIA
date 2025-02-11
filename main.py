import tkinter as tk
from tkinter import messagebox


def main():
# Función para la lista contigua
    def lista_contigua():
        # Crear una nueva ventana para la lista contigua
        ventana_contigua = tk.Toplevel(root)
        ventana_contigua.title("Lista Contigua")
        ventana_contigua.geometry("400x300")

        # Etiqueta y campo de entrada para el número de elementos
        label_n = tk.Label(ventana_contigua, text="Ingrese el número de elementos (máximo 10):")
        label_n.pack(pady=5)
        entry_n = tk.Entry(ventana_contigua)
        entry_n.pack(pady=5)

        # Lista para almacenar los elementos
        elementos = []

        # Función para ingresar elementos
        def ingresar_elementos():
            n = int(entry_n.get())  # Obtener el número de elementos
            if n > 10:
                messagebox.showerror("Error", "El número máximo de elementos es 10.")
                return

            # Limpiar la lista de elementos
            elementos.clear()

            # Crear campos de entrada para cada elemento
            for i in range(n):
                label_elemento = tk.Label(ventana_contigua, text=f"Ingrese el elemento {i}:")
                label_elemento.pack(pady=2)
                entry_elemento = tk.Entry(ventana_contigua)
                entry_elemento.pack(pady=2)
                elementos.append(entry_elemento)  # Guardar el campo de entrada en la lista

            # Botón para mostrar la lista contigua
            boton_mostrar = tk.Button(ventana_contigua, text="Mostrar Lista", command=mostrar_lista)
            boton_mostrar.pack(pady=10)

        # Función para mostrar la lista contigua
        def mostrar_lista():
            lista = []
            for entry in elementos:
                valor = entry.get()  # Obtener el valor de cada campo de entrada
                lista.append(valor)

            # Mostrar la lista en un widget Text
            resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            resultado_text.insert(tk.END, "Lista Contigua: " + " ".join(lista))

        # Botón para ingresar elementos
        boton_ingresar = tk.Button(ventana_contigua, text="Ingresar Elementos", command=ingresar_elementos)
        boton_ingresar.pack(pady=10)
        
    # Función para la lista ligada
    def lista_ligada():
        # Crear una nueva ventana para la lista ligada
        ventana_ligada = tk.Toplevel(root)
        ventana_ligada.title("Lista Ligada")
        ventana_ligada.geometry("400x300")

        # Lista para almacenar los nodos (valor, siguiente)
        nodos = []
        cabeza = -1  # Índice del primer nodo en la lista

        # Función para ingresar un elemento
        def ingresar_elemento():
            nonlocal cabeza
            valor = entry_valor.get()  # Obtener el valor del campo de entrada
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

            # Crear un nuevo nodo
            nuevo_nodo = [valor, cabeza]  # [valor, siguiente]
            nodos.append(nuevo_nodo)
            cabeza = len(nodos) - 1  # Actualizar la cabeza de la lista

            # Limpiar el campo de entrada
            entry_valor.delete(0, tk.END)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista ligada.")

        # Función para mostrar la lista ligada
        def mostrar_lista():
            resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            if cabeza == -1:
                resultado_text.insert(tk.END, "La lista ligada está vacía.")
                return

            # Construir la cadena de la lista ligada
            resultado = "Lista Ligada: "
            actual = cabeza
            while actual != -1:
                resultado += str(nodos[actual][0]) + " -> "
                actual = nodos[actual][1]
            resultado += "NULL"
            resultado_text.insert(tk.END, resultado)

        # Etiqueta y campo de entrada para el valor
        label_valor = tk.Label(ventana_ligada, text="Ingrese un valor:")
        label_valor.pack(pady=5)
        entry_valor = tk.Entry(ventana_ligada)
        entry_valor.pack(pady=5)

        # Botón para ingresar el elemento
        boton_ingresar = tk.Button(ventana_ligada, text="Ingresar Elemento", command=ingresar_elemento)
        boton_ingresar.pack(pady=10)

        # Botón para mostrar la lista ligada
        boton_mostrar = tk.Button(ventana_ligada, text="Mostrar Lista Ligada", command=mostrar_lista)
        boton_mostrar.pack(pady=10)

    # Función para la lista doblemente ligada
    def lista_doblemente_ligada():
        # Crear una nueva ventana para la lista doblemente ligada
        ventana_doble = tk.Toplevel(root)
        ventana_doble.title("Lista Doblemente Ligada")
        ventana_doble.geometry("400x300")

        # Lista para almacenar los nodos (valor, siguiente, anterior)
        nodos = []
        cabeza = -1  # Índice del primer nodo en la lista
        cola = -1    # Índice del último nodo en la lista

        # Función para ingresar un elemento
        def ingresar_elemento():
            nonlocal cabeza, cola
            valor = entry_valor.get()  # Obtener el valor del campo de entrada
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

            # Crear un nuevo nodo
            nuevo_nodo = [valor, cabeza, -1]  # [valor, siguiente, anterior]
            nodos.append(nuevo_nodo)

            # Si la lista no está vacía, actualizar el puntero anterior del antiguo primer nodo
            if cabeza != -1:
                nodos[cabeza][2] = len(nodos) - 1

            # Actualizar la cabeza de la lista
            cabeza = len(nodos) - 1

            # Si es el primer nodo, también es la cola
            if cola == -1:
                cola = cabeza

            # Limpiar el campo de entrada
            entry_valor.delete(0, tk.END)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista doblemente ligada.")

        # Función para mostrar la lista doblemente ligada
        def mostrar_lista():
            resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            if cabeza == -1:
                resultado_text.insert(tk.END, "La lista doblemente ligada está vacía.")
                return

            # Construir la cadena de la lista doblemente ligada (de cabeza a cola)
            resultado = "Lista Doblemente Ligada (de cabeza a cola): "
            actual = cabeza
            while actual != -1:
                resultado += str(nodos[actual][0]) + " <-> "
                actual = nodos[actual][1]
            resultado += "NULL\n"

            # Construir la cadena de la lista doblemente ligada (de cola a cabeza)
            resultado += "Lista Doblemente Ligada (de cola a cabeza): "
            actual = cola
            while actual != -1:
                resultado += str(nodos[actual][0]) + " <-> "
                actual = nodos[actual][2]
            resultado += "NULL"
            resultado_text.insert(tk.END, resultado)

        # Etiqueta y campo de entrada para el valor
        label_valor = tk.Label(ventana_doble, text="Ingrese un valor:")
        label_valor.pack(pady=5)
        entry_valor = tk.Entry(ventana_doble)
        entry_valor.pack(pady=5)

        # Botón para ingresar el elemento
        boton_ingresar = tk.Button(ventana_doble, text="Ingresar Elemento", command=ingresar_elemento)
        boton_ingresar.pack(pady=10)

        # Botón para mostrar la lista doblemente ligada
        boton_mostrar = tk.Button(ventana_doble, text="Mostrar Lista Doblemente Ligada", command=mostrar_lista)
        boton_mostrar.pack(pady=10)


    # Función para la lista indexada
    def lista_indexada():
        # Crear una nueva ventana para la lista indexada
        ventana_indexada = tk.Toplevel(root)
        ventana_indexada.title("Lista Indexada")
        ventana_indexada.geometry("400x300")

        # Lista para almacenar los valores
        valores = []
        indices = []  # Lista para almacenar los índices

        # Función para ingresar un elemento
        def ingresar_elemento():
            valor = entry_valor.get()  # Obtener el valor del campo de entrada
            if not valor:
                messagebox.showerror("Error", "Por favor, ingrese un valor.")
                return

            # Agregar el valor y su índice a las listas
            indices.append(len(valores))  # El índice es la posición actual en la lista
            valores.append(valor)

            # Limpiar el campo de entrada
            entry_valor.delete(0, tk.END)

            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", f"Elemento '{valor}' agregado a la lista indexada.")

        # Función para mostrar la lista indexada
        def mostrar_lista():
            resultado_text.delete(1.0, tk.END)  # Limpiar el contenido anterior
            if not valores:
                resultado_text.insert(tk.END, "La lista indexada está vacía.")
                return

            # Construir la cadena de la lista indexada
            resultado = "Lista Indexada:\n"
            for i in range(len(valores)):
                resultado += f"Índice: {indices[i]} -> Valor: {valores[i]}\n"
            resultado_text.insert(tk.END, resultado)

        # Etiqueta y campo de entrada para el valor
        label_valor = tk.Label(ventana_indexada, text="Ingrese un valor:")
        label_valor.pack(pady=5)
        entry_valor = tk.Entry(ventana_indexada)
        entry_valor.pack(pady=5)

        # Botón para ingresar el elemento
        boton_ingresar = tk.Button(ventana_indexada, text="Ingresar Elemento", command=ingresar_elemento)
        boton_ingresar.pack(pady=10)

        # Botón para mostrar la lista indexada
        boton_mostrar = tk.Button(ventana_indexada, text="Mostrar Lista Indexada", command=mostrar_lista)
        boton_mostrar.pack(pady=10)

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Simulación de Listas")
    root.geometry("500x400")

    # Widget para mostrar resultados
    resultado_text = tk.Text(root, height=15, width=50)
    resultado_text.pack(pady=10)

    # Menú de opciones
    label = tk.Label(root, text="Seleccione el tipo de lista a probar:")
    label.pack(pady=10)

    button_contigua = tk.Button(root, text="1. Lista Contigua", command=lista_contigua)
    button_contigua.pack(pady=5)

    button_ligada = tk.Button(root, text="2. Lista Ligada", command=lista_ligada)
    button_ligada.pack(pady=5)

    button_doblemente_ligada = tk.Button(root, text="3. Lista Doblemente Ligada", command=lista_doblemente_ligada)
    button_doblemente_ligada.pack(pady=5)

    button_indexada = tk.Button(root, text="4. Lista Indexada", command=lista_indexada)
    button_indexada.pack(pady=5)

    button_salir = tk.Button(root, text="5. Salir", command=root.quit)
    button_salir.pack(pady=10)

    # Ejecutar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()