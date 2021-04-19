# at

> Wykonuje polecenia o zadanym czasie.
> Aby działać poprawnie wymaga działającego serwisu atd (lub atrun).
> Więcej informacji: <https://manned.org/at>.

- Wykonaj za 5 minut polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`at now + 5 minutes`

- Wykonaj o 10:00 rano polecenie podane z wejścia standardowego:

`echo "{{./zrób_backup.sh}}" | at 1000`

- Wykonaj polecenia z podanego pliku w najbliższy wtorek o 21:30:

`at -f {{ścieżka/do/pliku}} 9:30 PM Tue`
