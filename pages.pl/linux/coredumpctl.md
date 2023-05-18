# coredumpctl

> Pobieraj i przetwarzaj zapisane zrzuty pamięci i metadane.
> Więcej informacji: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Wyświetl wszystkie zapisane zrzuty pamięci:

`coredumpctl list`

- Wyświetl zapisane zrzuty pamięci podanego programu:

`coredumpctl list {{program}}`

- Wyświetl informacje o zrzutach pamięci programu o podanym PID:

`coredumpctl info {{PID}}`

- Wywołaj debugger używając ostatniego zrzutu pamięci programu:

`coredumpctl debug {{program}}`

- Wyodrębnij ostatni zrzut pamięci programu do pliku:

`coredumpctl --output={{ścieżka/do/pliku}} dump {{program}}`
