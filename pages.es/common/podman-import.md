# podman import

> Importa un archivo tar y lo guarda como una imagen del sistema de archivos.
> Vea también: `podman export`, `podman save`.
> Más información: <HTTPS://docs.podman.io/en/latest/markdown/podman-import.1.html>.

- Importa un archivo tar desde un archivo local y crea una imagen:

`podman import {ruta/al/archivo.tar} {imagen:etiqueta}}`

- Importa un archivo tar desde una URL:

`podman import {https://example.com/imagen.tar} {imagen:etiqueta}}`

- Importa un archivo tar y añade un mensaje de confirmación:

`podman import {{[-m|--message]}} "[mensaje_de_confirmación]" {{ruta/al/archivo.tar}} {{imagen:etiqueta}}`

- Importa un archivo tar y establece un comando por defecto (necesario para ejecutar el contenedor):

`podman import {{[-c|--change]}} CMD={{/bin/bash}} {{ruta/al/archivo.tar}} {{imagen:etiqueta}}`
