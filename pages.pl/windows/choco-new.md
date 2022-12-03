# choco new

> Generowanie nowych specyfikacji pakietów Chocolatey.
> Więcej informacji: <https://chocolatey.org/docs/commands-new>.

- Utwórz nowy szkielet pakietu:

`choco new {{nazwa_pakietu}}`

- Utwórz nowy pakiet podając konkretną wersję:

`choco new {{nazwa_pakietu}} --version {{wersja}}`

- Utwórz nowy pakiet podając podając nazwę opiekuna:

`choco new {{nazwa_pakietu}} --maintainer {{nazwa_opiekuna}}`

- Utwórz nowy pakiet w podanym katalogu wyjściowym:

`choco new {{nazwa_pakietu}} --output-directory {{ścieżka/do/katalogu/wyjściowego}}`

- Utwórz nowy pakiet podając specyficzne adresy URL instalatoró dla wersji 32-bit i 64-bit:

`choco new {{nazwa_pakietu}} url="{{adres_url}}" url64="{{adres_url}}"`
