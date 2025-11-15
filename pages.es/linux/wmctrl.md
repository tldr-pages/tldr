# wmctrl

> CLI para X Window Manager.
> Más información: <https://manned.org/wmctrl>.

- Lista todas las ventanas, gestionadas por el gestor de ventanas:

`wmctrl -l`

- Cambia a la primera ventana cuyo título (parcial) coincida:

`wmctrl -a {{título_ventana}}`

- Mueve una ventana al espacio de trabajo actual, levántala y dale foco:

`wmctrl -R {{título_ventana}}`

- Cambia a un espacio de trabajo:

`wmctrl -s {{número_de_espacio_de_trabajo}}`

- Selecciona una ventana y activa la pantalla completa:

`wmctrl -r {{título_ventana}} -b toggle,fullscreen`

- Selecciona una ventana y muévela a un espacio de trabajo:

`wmctrl -r {{título_ventana}} -t {{número_de_espacio_de_trabajo}}`
