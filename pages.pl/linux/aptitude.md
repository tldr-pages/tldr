# aptitude

> Narzędzie zarządzania pakietami dla Debiana i Ubuntu.
> Więcej informacji: <https://manned.org/aptitude>.

- Zaktualizuj listę dostępnych pakietów oraz wersji. Zalecane jest uruchomienie tego polecenia przed innymi poleceniami `aptitude`:

`sudo aptitude update`

- Zainstaluj nowy pakiet i jego zależności:

`sudo aptitude install {{pakiet}}`

- Wyszukaj pakiet:

`aptitude search {{pakiet}}`

- Wyszukaj zainstalowany pakiet (`?installed` jest terminem wyszukiwania w `aptitude`):

`aptitude search '?installed({{pakiet}})'`

- Usuń pakiet i wszystkie pakiety zależne od niego:

`sudo aptitude remove {{pakiet}}`

- Zaktualizuj zainstalowane pakiety do najnowszej dostępnej wersji:

`sudo aptitude upgrade`

- Zaktualizuj zainstalowane pakiety (jak robi `aptitude upgrade`) włącznie z usunięciem przestarzałych pakietów i instalacją dodatkowych pakietów w celu spełnienia zależności:

`sudo aptitude full-upgrade`

- Ustaw zainstalowany pakiet jako wstrzymany, aby zapobiec jego automatycznym aktualizacjom:

`sudo aptitude hold '?installed({{pakiet}})'`
