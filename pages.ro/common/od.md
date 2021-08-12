# od

> Afișați conținutul fișierului în format octal, zecimal sau hexazecimal.
> Afișează opțional decalajul octeților și/sau reprezentarea tipăribilă pentru fiecare linie.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/od>

- Afișați fișierul utilizând setările implicite: format octal, 8 octeți pe linie, offset octal în octal și linii duplicate înlocuite cu `*`:

`od {{path/to/file}}`

- Afișează fișierul în modul verbose, adică fără a înlocui liniile duplicate cu `*`:

`od -v {{path/to/file}}`

- Afișează fișierul în format hexazecimal (unități de 2 octeți), cu offset de octeți în format zecimal:

`od --format={{x}} --address-radix={{d}} -v {{path/to/file}}`

- Afișează fișierul în format hexazecimal (unități de 1 octet) și 4 octeți pe linie:

`od --format={{x1}} --width={{4}} -v {{path/to/file}}`

- Afișați fișierul în format hexazecimal împreună cu reprezentarea sa de caractere și nu imprimați offset octet:

`od --format={{xz}} --address-radix={{n}} -v {{path/to/file}}`

- Citiți doar 100 de octeți dintr-un fișier pornind de la octet 500:

`od --read-bytes {{100}} --skip-bytes={{500}} -v {{path/to/file}}`
