# caffeinate

> Evita que macOS entre en modo de reposo.
> Más información: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Evita entrar en modo reposo por 1 hora (3600 segundos):

`caffeinate -u -t {{3600}}`

- Evita entrar en modo reposo hasta que un comando finaliza:

`caffeinate -s "{{command}}"`

- Evita entrar en modo reposo (use `Ctrl + C` para salir):

`caffeinate -i`

- Evita al disco entrar en modo reposo (use `Ctrl + C` para salir):

`caffeinate -m`
