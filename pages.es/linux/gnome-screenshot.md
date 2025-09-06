# gnome-screenshot

> Captura la pantalla, una ventana o un área definida por el usuario y guarda la imagen a un archivo.
> Más información: <https://manned.org/gnome-screenshot>.

- Toma una captura de pantalla y la guarda en la ubicación predeterminada, normalmente `~/Pictures`:

`gnome-screenshot`

- Toma una captura de pantalla y la guarda en la ubicación de archivo indicada:

`gnome-screenshot --file {{ruta/al/archivo}}`

- Toma una captura de pantalla y la guarda en el portapapeles:

`gnome-screenshot --clipboard`

- Toma una captura después de un número determinado de segundos:

`gnome-screenshot --delay {{5}}`

- Lanza la interfaz gráfica (GUI) de Captura de Pantalla GNOME:

`gnome-screenshot --interactive`

- Toma una captura de pantalla de la ventana actual y la guarda en la ubicación especificada:

`gnome-screenshot --window --file {{ruta/al/archivo}}`

- Toma una captura después del un número determinado de segundos y la guarda en el portapapeles:

`gnome-screenshot --delay {{10}} --clipboard`

- Muestra la versión:

`gnome-screenshot --version`
