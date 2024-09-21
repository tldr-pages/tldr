# svcs

> Wyświetl informację o uruchomionych usługach.
> Więcej informacji: <https://www.unix.com/man-page/linux/1/svcs>.

- Wypisz wszystkie uruchomione usługi:

`svcs`

- Wypisz wszystkie usługi, które nie są uruchomione:

`svcs -vx`

- Wypisz informacje o usłudze:

`svcs apache`

- Pokaż lokalizację pliku dziennika usługi:

`svcs -L apache`

- Wyświetl koniec pliku dziennika usługi:

`tail $(svcs -L apache)`
