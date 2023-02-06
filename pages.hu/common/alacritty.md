# alacritty

> Cross-platform, GPU-gyorsított terminál emulátor. További információ: <https://github.com/alacritty/alacritty>.

- Új Alacritty ablak megnyitása:

`alacritty`

- Futtatás egy adott könyvtárban:

`alacritty --working-directory {{path/to/directory}}`

- Parancs futtatása egy új Alacritty ablakban:

`alacritty -e {{command}}`

- Alternatív konfigurációs fájl megadása (alapértelmezés szerint `$XDG_CONFIG_HOME/alacritty/alacritty.yml`):

`alacritty --config-file {{path/to/config.yml}}`

- Live config reload engedélyezve futtatása (alapértelmezés szerint is engedélyezhető a `alacritty.yml`):

`alacritty --live-config-reload --config-file {{path/to/config.yml}}`
