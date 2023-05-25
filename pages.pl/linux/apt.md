# apt

> Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie.
> Zalecany zamiennik `apt-get` przy użyciu interaktywnym w Ubuntu w wersjach 16.04 i wyższych.
> Odpowiednie polecenia dla innych menedżerów pakietów: <https://wiki.archlinux.org/title/Pacman/Rosetta>.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Zaktualizuj listę dostępnych pakietów i ich wersji (zaleca się uruchomienie tego przed innymi poleceniami `apt`):

`sudo apt update`

- Wyszukaj podany pakiet:

`apt search {{pakiet}}`

- Wyświetl informacje o podanym pakiecie:

`apt show {{pakiet}}`

- Zainstaluj pakiet lub zaktualizuj go do najnowszej dostępnej wersji:

`sudo apt install {{pakiet}}`

- Usuń pakiet (użyj `purge` aby usunąć także pliki konfiguracyjne):

`sudo apt remove {{pakiet}}`

- Zaktualizuj wszystkie zainstalowane pakiety do ich najnowszych wersji:

`sudo apt upgrade`

- Wyświetl wszystkie pakiety:

`apt list`

- Wyświetl zainstalowane pakiety:

`apt list --installed`
