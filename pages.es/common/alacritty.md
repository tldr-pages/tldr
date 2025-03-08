# alacritty

> Emulador de terminal multiplataforma acelerado por GPU.
> Más información: <https://github.com/alacritty/alacritty>.

- Inicia un nuevo proceso Alacritty y crea una ventana:

`alacritty`

- Inicia el programa residente de Alacritty (sin crear una ventana):

`alacritty --daemon`

- Crea una nueva ventana utilizando el proceso Alacritty que ya está en marcha:

`alacritty msg create-window`

- Inicia el intérprete de comandos en un directorio específico (también funciona con `alacritty msg create-window`):

`alacritty --working-directory {{ruta/a/directorio}}`

- [e]jecuta un comando en una nueva ventana de Alacritty (también funciona con `alacritty msg create-window`):

`alacritty -e {{comando}}`

- Utiliza un archivo de configuración alternativo (por defecto es `$XDG_CONFIG_HOME/alacritty/alacritty.toml`):

`alacritty --config-file {{ruta/a/config.toml}}`

- Ejecuta con la recarga de la configuración activa (también puede activarse por defecto en `alacritty.toml`):

`alacritty --live-config-reload --config-file {{ruta/a/config.toml}}`
