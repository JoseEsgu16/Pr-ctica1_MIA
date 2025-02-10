import tkinter as tk
from tkinter import messagebox


def main():
    def lista_contigua():
        lista = [0] * 10  # Arreglo de tamaño fijo (10 elementos)
        n = int(input("Ingrese el número de elementos (máximo 10): "))
        
        # Insertar elementos
        for i in range(n):
            lista[i] = int(input(f"Ingrese el elemento {i}: "))
        
        # Mostrar la lista
        print("Lista Contigua:", " ".join(map(str, lista[:n])))
        
    def lista_ligada():
        nodo = [[-1, -1] for _ in range(10)]  # Matriz que almacena [valor, siguiente]
        cabeza = -1
        actual = 0
        fin = False

        print("Ingrese elementos (-1 para terminar):")
        while actual < 10 and not fin:
            valor = int(input())
            if valor == -1:
                fin = True
            else:
                # Insertar al inicio
                nodo[actual][0] = valor
                nodo[actual][1] = cabeza
                cabeza = actual
                actual += 1

        # Mostrar la lista
        print("Lista Ligada:", end=" ")
        actual = cabeza
        while actual != -1:
            print(nodo[actual][0], "->", end=" ")
            actual = nodo[actual][1]
        print("NULL")

    def lista_doblemente_ligada():
        nodo = [[-1, -1, -1] for _ in range(10)]  # Matriz que almacena [valor, siguiente, anterior]
        cabeza = -1
        actual = 0
        previo = -1
        fin = False

        print("Ingrese elementos (-1 para terminar):")
        while actual < 10 and not fin:
            valor = int(input())
            if valor == -1:
                fin = True
            else:
                # Insertar al inicio
                nodo[actual][0] = valor
                nodo[actual][1] = cabeza
                nodo[actual][2] = previo

                if cabeza != -1:
                    nodo[cabeza][2] = actual

                cabeza = actual
                previo = actual
                actual += 1

        # Mostrar la lista
        print("Lista Doblemente Ligada:", end=" ")
        actual = cabeza
        while actual != -1:
            print(nodo[actual][0], "<->", end=" ")
            actual = nodo[actual][1]
        print("NULL")

    def lista_indexada():
        lista = [0] * 10  # Lista de valores
        indice = [0] * 10  # Lista de índices
        n = int(input("Ingrese el número de elementos (máximo 10): "))

        # Insertar elementos
        for i in range(n):
            lista[i] = int(input(f"Ingrese el elemento {i}: "))
            indice[i] = i

        # Mostrar la lista
        print("Lista Indexada:")
        for i in range(n):
            print(f"Índice: {indice[i]} -> Valor: {lista[i]}")


    # Crear la ventana principal
    root = tk.Tk()
    root.title("Simulación de Listas")
    root.geometry("400x300")

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