def aplicar_inverso(event, editor):

    pixeles_salida = editor.imagen_procesada.load()

    for x in range(editor.ancho):
        for y in range(editor.alto):
            pixel = editor.pixeles[x, y]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]

            pixeles_salida[x, y] = (255 - r, 255 - g, 255 - b)
    editor.mostrar_imagen2(editor.imagen_procesada)
