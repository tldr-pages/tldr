# a2query

> Recuperați configurația runtime de la Apache pe OS-uri bazate pe Debian.
> Mai multe informaţii: <https://manpages.debian.org/buster/apache2/a2query.1.en.html>

- Lista modulelor Apache activate:

`sudo a2query -m`

- Verificați dacă este instalat un anumit modul:

`sudo a2query -m {{module_name}}`

- Lista gazdelor virtuale activate:

`sudo a2query -s`

- Afișează modulul Multi Processing activat în prezent:

`sudo a2query -M`

- Afișează versiunea Apache:

`sudo a2query -v`
