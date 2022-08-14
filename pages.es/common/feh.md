# feh

> Utilidad ligera de visualización de imágenes.
> Más información: <https://feh.finalrewind.org>.

- Muestra imágenes localmente o usando una URL:

`feh {{ruta/a/imagen}}`

- Muestra imágenes recursivamente:

`feh --recursive {{ruta/al/directorio}}`

- Muestra imágenes sin bordes:

`feh --borderless {{ruta/a/imagen}}`

- Cierra después de la última imagen:

`feh --cycle-once {{ruta/a/imagen}}`

- Agrega una demora al ciclo de la presentación:

`feh --slideshow-delay {{secundos}} {{ruta/a/imagen}}`

- Cambia el fondo de pantalla (centrado, llenar, maximizado, ampliado o amontonado):

`feh --bg-{{center|fill|max|scale|tile}} {{ruta/a/imagen}}`

- Crea un montage de todas las imágenes en un directorio. Produce una nueva imagen:

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{ruta/a/nueva_imagen}}`
