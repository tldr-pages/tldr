# xkill

> Cierra de manera forzosa una ventana interactivamente en una sesión gráfica.
> Vea también `kill` y `killall`.
> Más información: <https://www.x.org/releases/current/doc/man/man1/xkill.1.xhtml>.

- Muestra un cursor para cerrar forzosamente una ventana presionando con el botón izquierdo (presiona cualquier otro botón del ratón para cancelar):

`xkill`

- Muestra un cursor para seleccionar una ventana para cerrarla forzosamente al presionar cualquier botón del ratón:

`xkill -button any`

- Cierra forzosamente una ventana con un ID específico (use `xwininfo` para obtener información acerca de las ventanas):

`xkill -id {{id}}`
