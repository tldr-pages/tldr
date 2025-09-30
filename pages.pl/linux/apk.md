# apk

> Narzędzie zarządzania pakietami Alpine Linux.
> Więcej informacji: <https://wiki.alpinelinux.org/wiki/Alpine_Package_Keeper>.

- Zaktualizuj indeksy repozytoriów i wszystkie pakiety:

`apk upgrade {{[-U|--update-cache]}}`

- Zaktualizuj tylko indeksy repozytoriów:

`apk update`

- Zainstaluj nowy pakiet:

`apk add {{pakiet}}`

- Usuń pakiet:

`apk del {{pakiet}}`

- Napraw/Zainstaluj ponownie pakiet bez modyfikacji głównych zależności:

`apk fix {{pakiet}}`

- Wyszukaj pakiety ze słowem kluczowym w ich nazwie i wyświetl wyniki z opisami:

`apk search {{[-v|--verbose]}} {{słowo_kluczowe}}`

- Wyszukaj pakiety ze słowem kluczowym w ich opisie:

`apk search {{[-d|--description]}} {{słowo_kluczowe}}`

- Wyświetl informacje o określonym pakiecie:

`apk info {{pakiet}}`
