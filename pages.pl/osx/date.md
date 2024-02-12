# date

> Ustaw bądź wyświetl datę systemową.
> Więcej informacji: <https://keith.github.io/xcode-man-pages/date.1.html>.

- Wyświetl aktualną datę w domyślnym formacie:

`date +%c`

- Wyświetl aktualną datę w formacie UTC i ISO 8601:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Wyświetl aktualną datę jako znacznik czasu Unix (sekundy od epoki systemu Unix):

`date +%s`

- Wyświetl określoną datę jako znacznik czasu Unix w domyślnym formacie:

`date -r 1473305798`
