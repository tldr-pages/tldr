# feh

> Visor de imagenes.
> Para mas informacion: <https://feh.finalrewind.org>.

- Para imagenes locales o de URL:

`feh {{ruta/a/imagen}}`

- Para ver imagenes recursivamente:

`feh --recursive {{ruta/al/directorio}}`

- Para ver imagenes sin bordes:

`feh --borderless {{ruta/a/imagen}}`

- Para cerrar despues de una imagen:

`feh --cycle-once {{ruta/a/imagen}}`

- Agrega una demora a la presentacion:

`feh --slideshow-delay {{secundos}} {{ruta/a/imagen}}`

- Cambia el fondo de pantalla (centrado, llenar, maximizado, ampliado o amontonado):

`feh --bg-{{center|fill|max|scale|tile}} {{ruta/a/imagen}}`

- Crea un montage de todas las imágenes en un directorio. Produce una nueva imagen.

`feh --montage --thumb-height {{150}} --thumb-width {{150}} --index-info "{{%nn%wx%h}}" --output {{ruta/a/nueva_imagen}}`
