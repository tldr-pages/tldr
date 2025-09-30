# polybar-msg

> Controla `polybar` utilizando mensajería entre procesos (IPC).
> Nota: IPC está desactivado por defecto y se puede habilitar configurando `enable-ipc = true` en la configuación de Polybar.
> Más información: <https://polybar.rtfd.io/en/stable/user/ipc.html>.

- Cierra la barra:

`polybar-msg cmd quit`

- Reinicia la barra en su lugar:

`polybar-msg cmd restart`

- Oculta la barra (no hace nada si la barra ya está oculta):

`polybar-msg cmd hide`

- Muestra la barra nuevamente (no hace nada si la barra no está oculta):

`polybar-msg cmd show`

- Alterna entre oculto/visible:

`polybar-msg cmd toggle`

- Ejecuta una acción de módulo (la cadena de datos es opcional):

`polybar-msg action "#{{nombre_módulo}}.{{nombre_acción}}.{{cadena_de_datos}}"`

- Envía mensajes solo a una instancia específica de Polybar (todas las instancias por defecto):

`polybar-msg -p {{pid}} {{cmd|action}} {{carga}}`
