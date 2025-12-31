# dialog

> Muestra cuadros de diálogo en el terminal.
> Más información: <https://manned.org/dialog>.

- Muestra un mensaje:

`dialog --msgbox "{{Mensaje}}" {{altura}} {{ancho}}`

- Solicita ingreso de texto al usuario:

`dialog --inputbox "{{Ingrese texto:}}" {{8}} {{40}} 2>{{salida.txt}}`

- Solicitar al usuario una pregunta de sí/no:

`dialog --yesno "{{¿Continuar?}}" {{7}} {{40}}`
