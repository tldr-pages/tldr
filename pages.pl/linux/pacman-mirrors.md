# pacman-mirrors

> Wygeneruj listę serwerów lustrzanych dla Manjaro Linuksa.
> Każde uruchomienie pacman-mirrors wymaga zsynchronizowanej bazy danych oraz zaktualizowania systemu używając `sudo pacman -Syyu`.
> Zobacz także: `pacman`.
> Więcej informacji: <https://wiki.manjaro.org/index.php?title=Pacman-mirrors>.

- Wygeneruj listę serwerów lustrzanych używając domyślnych ustawień:

`sudo pacman-mirrors --fasttrack`

- Wyświetl status aktualnych serwerów lustrzanych:

`pacman-mirrors --status`

- Pokaż aktualną gałąź:

`pacman-mirrors --get-branch`

- Przęłącz na inną gałąź:

`sudo pacman-mirrors --api --set-branch {{stable|unstable|testing}}`

- Wygeneruj listę serwerów lustrzanych, używając tylko tych w twoim kraju:

`sudo pacman-mirrors --geoip`
