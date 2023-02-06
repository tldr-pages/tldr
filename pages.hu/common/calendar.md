# calendar

> Közelgő események megjelenítése egy naptárfájlból. További információ: <https://www.commandlinux.com/man-page/man1/calendar.1.html>.

- A mai és a holnapi (vagy a pénteki hétvégi) események megjelenítése az alapértelmezett naptárból:

`calendar`

- Look \[A\]head, a következő 30 nap eseményeinek megjelenítése:

`calendar -A {{30}}`

- Look \[B\]ack, az előző 7 nap eseményeinek megjelenítése:

`calendar -B {{7}}`

- Egyéni naptárból származó események megjelenítése \[f\]ile:

`calendar -f {{path/to/file}}`
