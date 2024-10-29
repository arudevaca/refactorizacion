def ingresar_puntuacion_y_comentario():
    while True:
        point = input('Por favor, introduzca una puntuación en una escala de 1 a 5: ')
        
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Por favor, introduzca un valor entre 1 y 5.')
            else:
                comment = input('Por favor, introduzca un comentario: ')
                post = f'punto: {point} comentario: {comment}'
                
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                print('Puntuación y comentario guardados.')
                break
        else:
            print('Por favor, introduzca la puntuación en números.')

def mostrar_resultados():
    print('Resultados hasta la fecha:')
    try:
        with open("data.txt", "r") as read_file:
            content = read_file.read()
            if content:
                print(content)
            else:
                print('No hay resultados guardados.')
    except FileNotFoundError:
        print('No se encontró el archivo de datos.')

def menu_principal():
    while True:
        print('Seleccione el proceso que desea aplicar:')
        print('1: Ingresar puntuación y comentario')
        print('2: Comprobar los resultados obtenidos hasta ahora.')
        print('3: Finalizar')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_puntuacion_y_comentario()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Finalizando')
                break
            else:
                print('Introduzca un número del 1 al 3')
        else:
            print('Introduzca un número del 1 al 3')

if __name__ == "__main__":
    menu_principal()
