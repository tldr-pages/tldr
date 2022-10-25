# caffeinate

> Nie pozwól aby macOS się uśpił.
> Więcej informacji: <https://ss64.com/osx/caffeinate.html>.

- Nie usypiaj przez 1 godzinę (3600 sekund):

`caffeinate -u -t {{3600}}`

- Nie usypiaj dopóki komenda nie zostanie zakończona:

`caffeinate -s "{{command}}"`

- Nie zasypiaj dopóki nie przerwiesz przez Ctrl-C:

`caffeinate -i`
