# hyprctl

> Controla partes del compositor Hyprland Wayland.
> Más información: <https://wiki.hyprland.org/Configuring/Using-hyprctl>.

- Recarga la configuración de Hyprland:

`hyprctl reload`

- Muestra el nombre de la ventana activa:

`hyprctl activewindow`

- Lista todos los dispositivos de entrada conectados:

`hyprctl devices`

- Lista todas las salidas con sus respectivas propiedades:

`hyprctl workspaces`

- Llama a un gestor con un argumento:

`hyprctl dispatch exec {{aplicación}}`

- Establece una palabra clave de configuración de forma dinámica:

`hyprctl keyword {{palabra_clave}} {{valor}}`

- Muestra versión:

`hyprctl version`
