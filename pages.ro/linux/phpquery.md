# phpquery

> Manager de extensii PHP pentru OS-uri bazate pe Debian.

- Lista versiunilor PHP disponibile:

`sudo phpquery -V`

- Lista SAPI-uri disponibile pentru PHP 7.3:

`sudo phpquery -v {{7.3}} -S`

- Lista extensiilor activate pentru PHP 7.3 cu cli SAPI:

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- Verificați dacă extensia json este activată pentru PHP 7.3 cu apache2 SAPI:

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`
