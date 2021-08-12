# phpenmod

> Activează extensiile PHP pe OS-uri bazate pe Debian.

- Activează extensia json pentru fiecare SAPI din fiecare versiune PHP:

`sudo phpenmod {{json}}`

- Activați extensia json pentru PHP 7.3 cu cli SAPI:

`sudo phpenmod -v {{7.3}} -s {{cli}} {{json}}`
