# batch

> Wykonaj polecenia, gdy pozwoli na to poziom obciążenia systmu.
> Aby działać poprawnie wymaga działającego serwisu atd (lub atrun).
> Więcej informacji: <https://manned.org/batch>.

- Wykonaj polecenie wprowadzone przy użyciu wejścia standardowego (aby zakończyć naciśnij `Ctrl + D`):

`batch`

- Wykonaj polecenie podane z wejścia standardowego:

`echo "{{./zrób_backup.sh}}" | batch`

- Wykonaj polecenia z podanego pliku:

`batch -f {{ścieżka/do/pliku}}`
