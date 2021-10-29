# Juego sudoku
# Nombre: Tamara Peña

# El cosdigo consiste en utilizar listas para formar la matriz de 9x9, luego determinar un conjunto de números posibles para cada uno de los casilleros vacíos
# y luego selecciona números aleatoriamente hasta obtener el resultado correcto.

# Se utiliza el modulo ramdon (elegir de forma aleatoria)

from random import choice

def numero_fila(grid, fila, numero): #Función que ve si el número que le asigna como argumento se encuentra en la fila definida.
    return numero in grid[fila]      #"grid" nos indica donde se ubicará el numero,  ya sea por ejemplo en la celda correspondiente a la fila 1 y la columna 1.
                                     #La declaración de retorno finaliza la ejecución de la función y especifica un valor que se devolverá al llamador de la función.

def numero_columna(grid, columna, numero):  #Función que ve si el número que le asigna como argumento se encuentra en la columna definida.
    return numero in (fila[columna] for fila in grid)

def numero_caja(grid, fila, columna, numero):   #Función que verifica si el número indicado se encuentra en la subcelda 3×3 (caja) que corresponde a la posición definida.

    casilla_fila, casilla_columna = casilla_posicion(fila, columna)   #Función que ayuda a numero_caja()a verificar si un número se encuentra en la subcelda de 3×3.

    numeros_de_casillas = unpack(                              #Se construye una lista con los números en la caja.
        fila[casilla_columna*3:casilla_columna*3 + 3]
        for fila in grid[casilla_fila*3:casilla_fila*3 + 3]
    )
    return numero in numeros_de_casillas

def reducir(n):       #Función que reduce la posición, de 9x9 a 3x3.
    n /= 3
    if n == 0 or n != int(n):
        n += 1
    return int(n)

def casilla_posicion(fila, columna):
    fila += 1                                     # Se trabaja temporalmente con base 1.
    columna += 1 
    return reducir(fila) - 1, reducir(columna) - 1  # se obtiene base 0 nuevamente.

def unpack(iterable):
    for item in iterable:
        yield from item #La sintaxis yield from permite encadenar generadores.
        
def obtener_posibles_numeros(grid, fila, columna): #Función que retorna los valores posibles para una determinada casilla.
    for numero in range(1, 10):
        if (not numero_fila(grid, fila, numero) and
            not numero_columna(grid, columna, numero) and
            not numero_caja(grid, fila, columna, numero)):
            yield numero
            
def main():     # La función main() ejecuta el código principal para juego completo.
    while True: 
        grid2 = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],         #Tenemos la caja de 9x9 completa del juego, donde los ceros representan las casillas vacías.
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9],
        ]
        s = \
        """\
        *-------*-------*-------*
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        *-------*-------*-------*
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        *-------*-------*-------*
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        | {} {} {} | {} {} {} | {} {} {} |
        *-------*-------*-------*
        """
        
        # Haciendo uso de "\" se puede romper el código en varias líneas.
        
        while True:
            posibles_numeros = {
                (fila, columna): None for fila in range(9) for columna in range(9)
            }
            # Obtener una lista de números posibles para cada una de las posiciones vacías.
            for fila in range(9):
                for columna in range(9):
                    numero = grid2[fila][columna]
                    if numero == 0:
                        opciones = list(
                            obtener_posibles_numeros(grid2, fila, columna)
                        )
                        if opciones:
                            posibles_numeros[(fila, columna)] = opciones
            
            # Se cambia los valores 0(espacios vacíos) y se ordena por la cantidad de posibilidades.
            posibles_numeros = sorted(
                (
                    (k, v)
                    for (k, v) in posibles_numeros.items()
                    if v is not None
                ),
                key=lambda kv: len(kv[1]) #Las funciones Lambda se definen como una línea que ejecuta una sola expresión.
            )
            
            if posibles_numeros: # Obtener el primer item
                (fila, columna), numeros = posibles_numeros[0]#se obtiene un número aleatorio de la lista de posibiilidades hasta que la grilla esté completa
                grid2[fila][columna] = choice(numeros)
            else:
                break
        
        # Se comprueba si la forma aleatoria dió resultado,si no hay más ceros en las casillas entonces el Sudoku está resuelto.
        if 0 not in unpack(grid2):
            print(s.format(*(unpack(grid2))))
            break
if __name__ == "__main__": #Cuando se ejecuta el script , la variable "__name__"se establecerá como "__main__", esto
    main()                 #si el módulo que se está ejecutando es el programa principal.
print("El juego está resuelto")

