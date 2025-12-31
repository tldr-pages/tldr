# bspc

> Configura y controla `bspwm`, gestionando nodos, escritorios, monitores y más.
> Vea también: `bspwm`.
> Más información: <https://github.com/baskerville/bspwm/blob/master/doc/bspwm.1.asciidoc>.

- Define dos escritorios virtuales:

`bspc monitor {{[-d|--reset-desktops]}} {{nombre_escritorio1}} {{nombre_escritorio2}}`

- Enfoca un determinado escritorio:

`bspc desktop {{[-f|--focus]}} {{número}}`

- Cierra las ventanas enraizadas en el nodo seleccionado:

`bspc node {{[-c|--close]}}`

- Envía el nodo seleccionado al escritorio especificado:

`bspc node {{[-d|--to-desktop]}} {{número}}`

- Activa el modo de pantalla completa para el nodo seleccionado:

`bspc node {{[-t|--state]}} ~fullscreen`

- Establece el valor de una configuración determinada:

`bspc config {{nombre_configuración}} {{valor}}`
