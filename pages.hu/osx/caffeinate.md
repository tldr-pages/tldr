# caffeinate

> A macOS alvó üzemmódjának megakadályozása. További információ: <https://ss64.com/osx/caffeinate.html>.

- Az alvás megakadályozása 1 órán keresztül (3600 másodperc):

`caffeinate -u -t {{3600}}`

- Az alvás megakadályozása egy parancs befejezéséig:

`caffeinate -s "{{command}}"`

- Az alvás megakadályozása (kilépéshez használja a `Ctrl + C` címet):

`caffeinate -i`

- A lemez alvás megakadályozása (kilépéshez használja a `Ctrl + C` címet):

`caffeinate -m`
