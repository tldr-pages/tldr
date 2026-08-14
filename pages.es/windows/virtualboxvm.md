# virtualboxvm

> Administra máquinas virtuales de VirtualBox.
> Más información: <https://www.virtualbox.org/>.

- Inicia una máquina virtual:

`virtualboxvm --startvm {{nombre|uuid}}`

- Inicia una máquina virtual en modo de pantalla completa:

`virtualboxvm --startvm {{nombre|uuid}} --fullscreen`

- Monta el archivo de imagen de DVD especificado:

`virtualboxvm --startvm {{nombre|uuid}} --dvd {{ruta\al\archivo_de_imagen}}`

- Muestra una ventana de línea de comandos con información de depuración:

`virtualboxvm --startvm {{nombre|uuid}} --debug-command-line`

- Inicia una máquina virtual en estado pausado:

`virtualboxvm --startvm {{nombre|uuid}} --start-paused`
