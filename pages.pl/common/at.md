# at

> Jednokrotnie wykonaj polecenia w późniejszym czasie.
> Usługa atd (lub atrun) powinna być uruchomiona dla rzeczywistych wykonań.
> Więcej informacji: <https://manned.org/at>.

- Wykonaj polecenia z `stdin` po upływie 5 minut (naciśnij `<Ctrl d>` po zakończeniu):

`at now + 5 minutes`

- Wykonaj polecenie z `stdin` dziś o 10:00:

`echo "{{./zrób_kopię_zapasową_bazy_danych.sh}}" | at 1000`

- Wykonaj polecenia z danego pliku w następny wtorek:

`at -f {{ścieżka/do/pliku}} 9:30 PM Tue`
