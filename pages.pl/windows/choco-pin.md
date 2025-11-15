# choco pin

> Przypięcie obecnej bądź podanej wersji dla danego pakietu zarządzanego przez Chocolatey.
> Przypięte pakiety są automatycznie pomijane podczas aktualizacji pakietów.
> Więcej informacji: <https://chocolatey.org/docs/commands-pin>.

- Wyświetlanie listy obecnie przypiętych pakietów wraz z wersjami:

`choco pin list`

- Przypnij pakiet w jego obecnej wersji:

`choco pin add --name {{pakiet}}`

- Przypnij pakiet w podanej wersji:

`choco pin add --name {{pakiet}} --version {{wersja}}`

- Odepnij dany pakiet:

`choco pin remove --name {{pakiet}}`
