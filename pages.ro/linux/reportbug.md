# reportbug

> Instrumentul de raportare a erorilor din distribuția Debian.
> Mai multe informaţii: <https://manpages.debian.org/buster/reportbug/reportbug.1.en.html>

- Generați un raport de eroare despre un anumit pachet, apoi trimiteți-l prin e-mail:

`reportbug {{package}}`

- Raportați o eroare care nu are legătură cu un anumit pachet (problemă generală, infrastructură etc.):

`reportbug other`

- Scrieți raportul de eroare într-un fișier în loc să îl trimiteți prin e-mail:

`reportbug -o {{filename}} {{package}}`
