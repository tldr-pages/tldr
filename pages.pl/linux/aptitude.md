# aptitude

> Narzędzie zarządzania pakietami dla Debiana i Ubuntu.
> Więcej informacji: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Zaktualizuj listę dostępnych pakietów oraz wersji. Zalecane jest uruchomienie tego polecenia przed innymi poleceniami `aptitude`:

`aptitude update`

- Zainstaluj nowy pakiet i jego zależności:

`aptitude install {{pakiet}}`

- Wyszukaj pakiet:

`aptitude search {{pakiet}}`

- Wyszukaj zainstalowany pakeit (`?installed` jest wyszukiwanym terminem w `aptitude`):

`aptitude search '?installed({{pakiet}})'`

- Usuń pakiet i wszystkie pakiety zależne od niego:

`aptitude remove {{pakiet}}`

- Zaktualizuj zainstalowane pakiety do najnowszej dostępnej wersji:

`aptitude upgrade`

- Zaktualizuj zainstalowane pakiety (jak robi `aptitude upgrade`) włącznie z usunięciem przestarzałych pakietów i instalacją dodatkowych pakietów w celu spełnienia zależności:

`aptitude full-upgrade`

- Ustaw zainstalowany pakiet jako wstrzymany, aby zapobiec jego automatycznym aktualizacjom:

`aptitude hold '?installed({{pakiet}})'`
