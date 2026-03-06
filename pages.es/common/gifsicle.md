# gifsicle

> Crea, edita, manipula y obtiene información sobre archivos GIF.
> Más información: <https://www.lcdf.org/gifsicle/>.

- Optimiza un GIF como un nuevo archivo:

`gifsicle {{ruta/a/archivo_entrada.gif}} {{[-O|--optimize=]}}3 {{[-o|--output]}} {{ruta/a/archivo_salida.gif}}`

- Utiliza el modo por lotes (modifica cada archivo dado su lugar) y desoptimiza un archivo GIF:

`gifsicle {{[-b|--batch]}} {{ruta/a/archivo_entrada.gif}} {{[-U|--unoptimize]}}`

- Extrae un fotograma de un archivo GIF:

`gifsicle {{ruta/a/archivo_entrada.gif}} '#{{0}}' > {{ruta/a/primer_fotograma.gif}}`

- Crea una animación GIF a partir de GIF seleccionados:

`gifsicle {{*.gif}} {{[-d|--delay]}} {{10}} {{[-l|--loop]}} > {{ruta/a/archivo_salida.gif}}`

- Reducir el tamaño del archivo utilizando compresión con pérdida:

`gifsicle {{[-b|--batch]}} {{ruta/a/archivo_entrada.gif}} {{[-O|--optimize=]}}3 --lossy={{100}} {{[-k|--colors]}} {{16}} {{[-f|--dither]}}`

- Elimina los primeros 10 fotogramas y todos los fotogramas posteriores al fotograma 20 de un GIF:

`gifsicle {{[-b|--batch]}} {{ruta/a/archivo_entrada.gif}} --delete “#{{0-9}}” '#{{20-}}'`

- Modifica todos los fotogramas recortándolos en un rectángulo, cambiando su escala, volteándolos y rotándolos:

`gifsicle {{[-b|--batch]}} --crop {{starting_x}},{{starting_y}}+{{rect_width}}x{{rect_height}} --scale {{0.25}} --flip-horizontal --rotate-{{90|180|270}} {{ruta/a/archivo_entrada.gif}}`
