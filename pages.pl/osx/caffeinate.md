# caffeinate

> Nie pozwól aby macOS się uśpił.
> Więcej informacji: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Nie usypiaj przez 1 godzinę (3600 sekund):

`caffeinate -u -t {{3600}}`

- Nie usypiaj dopóki komenda nie zostanie zakończona:

`caffeinate -s "{{command}}"`

- Nie usypiaj dopóki nie przerwiesz naciskając `Ctrl - C`:

`caffeinate -i`

- Nie usypiaj dysku twardego dopóki nie przerwiesz naciskając `Ctrl + C`:

`caffeinate -m`
