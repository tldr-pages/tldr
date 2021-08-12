# phpdismod

> Dezactivați extensiile PHP pe OS-uri bazate pe Debian.

- Dezactivați extensia json pentru fiecare SAPI din fiecare versiune PHP:

`sudo phpdismod {{json}}`

- Dezactivați extensia json pentru PHP 7.3 cu cli SAPI:

`sudo phpdismod -v {{7.3}} -s {{cli}} {{json}}`
