# apt-get

> Narzędzie do zarządzania pakietami Debiana i Ubuntu.
> Szukaj pakietów używając `apt-cache`.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Zaktualizuj listę dostępnych pakietów oraz wersji (zalecane jest uruchomienie tego polecenia przed innymi poleceniami `apt-get`):

`apt-get update`

- Zainstaluj pakiet lub zaktualizuj go do najnowszej dostępnej wersji:

`apt-get install {{pakiet}}`

- Usuń pakiet:

`apt-get remove {{pakiet}}`

- Usuń pakiet i jego pliki konfiguracyjne:

`apt-get purge {{pakiet}}`

- Zaktualizuj wszystkie zainstalowane pakiety do ich najnowszych dostępnych wersji:

`apt-get upgrade`

- Wyczyść lokalne repozytorium - usuwa wszystkie pliki pakietów (`.deb`) z przerwanych pobrań które nie mogą już być pobrane:

`apt-get autoclean`

- Usuń wszystkie pakiety, które już nie są potrzebne:

`apt-get autoremove`

- Zaktualizuj zainstalowane pakiety (jak `upgrade`), ale usuń przestarzałe pakiety i zainstaluj dodatkowe pakiety, aby spełnić zależności:

`apt-get dist-upgrade`
