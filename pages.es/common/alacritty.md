# alacritty

> Emulador de terminal acelerado por GPU y multiplataforma.
> Más información: <https://github.com/alacritty/alacritty>.

- Abre una nueva ventana de Alacritty:

`alacritty`

- Ejecuta Alacritty en un directorio específico:

`alacritty --working-directory {{ruta/al/directorio}}`

- Ejecuta un comando en una nueva ventana de Alacritty:

`alacritty -e {{comando}}`

- Especifica un archivo de configuración alternativo (por defecto es `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file {{ruta/al/config.yml}}`

- Ejecuta con recarga automática de la configuración activada (puede activarse por defecto en `alacritty.yml`):

`alacritty --live-config-reload --config-file {{ruta/al/config.yml}}`
