# cat

> Vypisuje a spojuje soubory.
> Více informací: <https://manned.org/cat.1posix>.

- Vypíše obsah souboru do `stdout`:

`cat {{cesta/k/souboru}}`

- Spojí několik souborů do výstupního souboru:

`cat {{cesta/k/souboru1 cesta/k/souboru2 ...}} > {{cesta/k/vystupnimu_souboru}}`

- Přidá několik souborů do výstupního souboru:

`cat {{cesta/k/souboru1 cesta/k/souboru2 ...}} >> {{cesta/k/vystupnimu_souboru}}`

- Zkopíruje obsah souboru do výstupního souboru bez vyrovnávací paměti:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Vypíše `stdin` do souboru:

`cat - > {{cesta/k/souboru}}`
