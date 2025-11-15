# imv

> Visor de imágenes de línea de comando para Wayland y X11 dirigido a gestores de ventanas en mosaico.
> Maneja múltiples formatos incluyendo Photoshop (PSD).
> Más información: <https://sr.ht/~exec64/imv>.

- Muestra múltiples imágenes:

`imv {{ruta/a/la/imagen1.ext ruta/a/la/imagen2.ext ...}}`

- Vista en modo de pantalla completa:

`imv -f {{ruta/a/la/imagen.ext}}`

- Muestra imágenes de un directorio [r]ecursivamente:

`imv -r --slideshow {{ruta/al/directorio}}`

- Abre múltiples imágenes vía `stdin`:

`find . -type f -name "{{*.svg}}" | imv`

- Hace una presentación desde un directorio que muestra cada imagen durante 10 segundos:

`imv -t 10 {{ruta/al/directorio}}`

- Muestra múltiples imágenes de la web:

`curl -Osw '%{filename_effective}\n' '{{http://www.example.com/[1-10].jpg}}' | imv`
