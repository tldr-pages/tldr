# mpremote

> Controla remotamente dispositivos MicroPython.
> Más información: <https://docs.micropython.org/en/latest/reference/mpremote.html>.

- Lista todos los dispositivos MicroPython conectados:

`mpremote connect list`

- Abre una sesión REPL interactiva con un dispositivo conectado:

`mpremote connect {{dispositivo}}`

- Ejecuta un script local en un dispositivo conectado:

`mpremote run {{ruta/a/script.py}}`

- Monta un directorio local en el dispositivo:

`mpremote mount {{ruta/al/directorio}}`

- Instala un paquete mip en el dispositivo:

`mpremote mip install {{paquete}}`
