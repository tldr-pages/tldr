# inotifywait

> Espera a que se produzcan cambios en los archivos.
> Vea también: `fatrace`.
> Más información: <https://manned.org/inotifywait>.

- Vigila un archivo específico en busca de eventos, saliendo tras el primero:

`inotifywait {{ruta/al/archivo}}`

- Vigila continuamente un archivo específico en busca de eventos sin salir:

`inotifywait {{[-m|--monitor]}} {{ruta/al/archivo}}`

- Vigila un directorio de forma recursiva en busca de eventos:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} {{ruta/al/directorio}}`

- Vigila un directorio en busca de cambios, excluyendo los archivos cuyos nombres coincidan con una `expresión regular`:

`inotifywait {{[-m|--monitor]}} {{[-r|--recursive]}} --exclude "{{regex}}" {{ruta/al/directorio}}`

- Vigila un archivo en busca de cambios, cerrándose cuando no se produzca ningún evento durante 30 segundos:

`inotifywait {{[-m|--monitor]}} {{[-t|--timeout]}} {{30}} {{ruta/al/archivo}}`

- Vigila un archivo solo en busca de eventos de modificación:

`inotifywait {{[-e|--event]}} {{modify}} {{ruta/al/archivo}}`

- Vigila un archivo mostrando solo los eventos, sin mensajes de estado:

`inotifywait {{[-q|--quiet]}} {{ruta/al/archivo}}`

- Ejecuta un comando cuando se accede a un archivo:

`inotifywait {{[-e|--event]}} {{access}} {{ruta/al/archivo}} && {{command}}`
