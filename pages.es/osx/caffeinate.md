# caffeinate

> Evita que macOS se duerma.
> Más información: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Evita que macOS entre en reposo durante 1 hora (3600 segundos):

`caffeinate -u -t {{3600}}`

- Evita que entre en reposo hasta que termine de ejecutarse un comando:

`caffeinate -s "{{comando}}"`

- Evita que el sistema entre en reposo hasta que finalice un proceso con el PID especificado:

`caffeinate -w {{pid}}`

- Evita que entre en reposo (usa `<Ctrl c>` para salir):

`caffeinate -i`

- Evita que el disco entre en reposo (usa `<Ctrl c>` para salir):

`caffeinate -m`
