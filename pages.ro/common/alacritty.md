# alacritty

> Emulator terminal accelerat de GPU cu platformă încrucișată.
> Mai multe informaţii: <https://github.com/alacritty/alacritty>

- Deschide o nouă fereastră Alacritty:

`alacritty`

- Rulați într-un anumit director:

`alacritty --working-directory {{path/to/directory}}`

- Rulați o comandă într-o fereastră nouă Alacritty:

`alacritty -e {{command}}`

- Specificați fișierul de configurare alternativă (implicit la `$xDG_config_home/Alacritty/Alacritty.yml`):

`alacritty --config-file {{path/to/config.yml}}`

- Rulați cu live config reload activat (poate fi, de asemenea, activat în mod implicit în `alacritty.yml`):

`alacritty --live-config-reload --config-file {{path/to/config.yml}}`
