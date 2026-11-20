# choco new

> Generowanie nowych specyfikacji pakietów Chocolatey.
> Więcej informacji: <https://docs.chocolatey.org/en-us/create/commands/new/>.

- Utwórz nowy szkielet pakietu:

`choco new {{pakiet}}`

- Utwórz nowy pakiet podając konkretną wersję:

`choco new {{pakiet}} --version {{wersja}}`

- Utwórz nowy pakiet podając podając nazwę opiekuna:

`choco new {{pakiet}} --maintainer {{nazwa_opiekuna}}`

- Utwórz nowy pakiet w podanym katalogu wyjściowym:

`choco new {{pakiet}} {{[--out|--output-directory]}} {{ścieżka/do/katalogu/wyjściowego}}`

- Utwórz nowy pakiet podając specyficzne adresy URL instalatoró dla wersji 32-bit i 64-bit:

`choco new {{pakiet}} url="{{adres_url}}" url64="{{adres_url}}"`
