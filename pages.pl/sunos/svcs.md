# svcs

> Lista informacji o uruchomionych usługach.
> Więcej informacji: <https://www.unix.com/man-page/linux/1/svcs>.

- Lista wszystkich uruchomionych usług:

`svcs`

- Lista wszystkich usług, które nie są uruchomione:

`svcs -vx`

- Lista informacji o usługach:

`svcs apache`

- Pokaż lokalizację pliku dziennika usługi:

`svcs -L apache`

- Wyświetlenie końca pliku dziennika usługi:

`tail $(svcs -L apache)`
