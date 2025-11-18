# apt-get

> Narzędzie do zarządzania pakietami Debiana i Ubuntu.
> Szukaj pakietów używając `apt-cache`.
> Więcej informacji: <https://manned.org/apt-get.8>.

- Zaktualizuj listę dostępnych pakietów oraz wersji (zalecane jest uruchomienie tego polecenia przed innymi poleceniami `apt-get`):

`sudo apt-get update`

- Zainstaluj pakiet lub zaktualizuj go do najnowszej dostępnej wersji:

`sudo apt-get install {{pakiet}}`

- Usuń pakiet:

`sudo apt-get remove {{pakiet}}`

- Usuń pakiet i jego pliki konfiguracyjne:

`sudo apt-get purge {{pakiet}}`

- Zaktualizuj wszystkie zainstalowane pakiety do ich najnowszych dostępnych wersji:

`sudo apt-get upgrade`

- Wyczyść lokalne repozytorium - usuwa wszystkie pliki pakietów (`.deb`) z przerwanych pobrań które nie mogą już być pobrane:

`sudo apt-get autoclean`

- Usuń wszystkie pakiety, które już nie są potrzebne:

`sudo apt-get autoremove`

- Zaktualizuj zainstalowane pakiety (jak `upgrade`), ale usuń przestarzałe pakiety i zainstaluj dodatkowe pakiety, aby spełnić zależności:

`sudo apt-get dist-upgrade`
