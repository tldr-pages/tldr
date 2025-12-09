# wezterm

> Wez's Terminal Emulator - un potente emulador de terminal multiplataforma y multiplexor.
> Más información: <https://wezterm.org/cli/general>.

- Inicia un nuevo proceso Wezterm y crea una ventana:

`wezterm`

- Establece una sesión `ssh`:

`wezterm ssh {{usuario}}@{{host}}:{{puerto}}`

- Conecta con el multiplexor (`wezterm-mux-server`):

`wezterm connect {{nombre_dominio}}`

- Envía una imagen al terminal:

`wezterm imgcat {{ruta/a/imagen}}`

- Graba una sesión de terminal como un asciicat (por defecto las grabaciones se encuentran en `/tmp`):

`wezterm record`

- Reproduce una sesión de terminal asciicat:

`wezterm replay {{ruta/al/archivo_cast}}`

- Especifica el archivo de configuración a utilizar (anula la resolución normal del archivo de configuración):

`wezterm --config-file {{ruta/al/archivo_config}}`

- Muestra la ayuda:

`wezterm help`
