# apt

> Narzędzie do zarządzania pakietami dla dystrybucji bazujących na Debianie.
> Zalecany zamiennik `apt-get` przy uyciu interaktywnym w Ubuntu w wersji 16.04 i wyższych.
> Więcej informacji: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Aktualizacja listy dostępnych pakietów i ich wersji (zalecane uruchomienie przed innymi poleceniami `apt`):

`sudo apt update`

- Wyszukanie podanego pakietu:

`apt search {{pakiet}}`

- Wyświetlenie informacji o pakiecie:

`apt show {{pakiet}}`

- Instalacja pakietu lub aktualizacja do najnowszej dostępnej wersji:

`sudo apt install {{pakiet}}`

- Usunięcie pakietu (użyj `purge` aby usunąć także pliki konfiguracyjne):

`sudo apt remove {{pakiet}}`

- Aktualizacja wszystkich zainstalowanych pakietów do ich najnowszych wersji:

`sudo apt upgrade`

- Wyświetlenie wszystkich pakietów:

`apt list`

- Wyświetlenie zainstalowanych pakietów:

`apt list --installed`
