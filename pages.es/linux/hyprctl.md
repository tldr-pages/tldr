# hyprctl

> Controla partes del compositor Hyprland Wayland.
> Más información: <https://wiki.hypr.land/Configuring/Using-hyprctl/>.

- Recarga la configuración de Hyprland:

`hyprctl reload`

- Muestra el nombre de la ventana activa:

`hyprctl activewindow`

- Lista todos los dispositivos de entrada conectados:

`hyprctl devices`

- Lista todas las salidas con sus respectivas propiedades:

`hyprctl workspaces`

- Llama a un despachador:

`hyprctl dispatch {{despachador}}`

- Establece una configuración de una palabra clave (keyword) de forma dinámica:

`hyprctl keyword {{palabra_clave}} {{valor}}`

- Muestra versión:

`hyprctl version`
