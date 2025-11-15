# fuzzel

> Un lanzador de aplicaciones y buscador difuso nativo de Wayland, inspirado en `rofi` y `dmenu`.
> Más información: <https://codeberg.org/dnkl/fuzzel>.

- Ejecuta aplicaciones:

`fuzzel`

- Ejecuta `fuzzel` en modo dmenu:

`fuzzel {{[-d|--dmenu]}}`

- Muestra un menú con la salida del comando `ls`:

`{{ls}} | fuzzel {{[-d|--dmenu]}}`

- Muestra un menú con elementos personalizados separados por una nueva línea (`\n`):

`echo -e "{{rojo}}\n{{verde}}\n{{azul}}" | fuzzel {{[-d|--dmenu]}}`

- Permite al usuario elegir entre varios elementos y guarda el seleccionado en un archivo:

`echo -e "{{rojo}}\n{{verde}}\n{{azul}}" | fuzzel {{[-d|--dmenu]}} > {{color.txt}}`

- Restablece el recuento de aplicaciones utilizadas (directorio de caché por defecto: `$XDG_CACHE_HOME/fuzzel`):

`rm -v $HOME/.cache/fuzzel`

- Inicia `fuzzel` en un monitor específico, vea `wlr-randr` o `swaymsg -t get_outputs`:

`fuzzel {{[-o|--output]}} "{{DP-1}}"`

- Utilice `fuzzel` para realizar una búsqueda en línea:

`fuzzel {{[-d|--dmenu]}} {{[-l|--lines]}} 0 --placeholder "{{Escriba su búsqueda}}" | sed 's/^/\«/g;s/$/\»/g' | xargs firefox --search`
