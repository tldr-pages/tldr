# alacritty

> Emulador de terminal multiplataforma acelerado por GPU.
> Más información: <https://manned.org/alacritty>.

- Inicia un nuevo proceso Alacritty y crea una ventana:

`alacritty`

- Inicia el programa residente de Alacritty (sin crear una ventana):

`alacritty --daemon`

- Crea una nueva ventana utilizando el proceso Alacritty ya en ejecución:

`alacritty msg create-window`

- Inicia el intérprete de comandos en un directorio específico (también funciona con `alacritty msg create-window`):

`alacritty --working-directory {{ruta/a/directorio}}`

- [e]jecuta un comando en una nueva ventana de Alacritty (también funciona con `alacritty msg create-window`):

`alacritty {{[-e|--command]}} {{comando}}`

- Utiliza un archivo de configuración alternativo (por defecto es `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{ruta/a/config.toml}}`
