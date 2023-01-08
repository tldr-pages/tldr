# wajig

> Uproszczone narzędzie do zarządzania pakietami dla systemów oparych na Debianie.
> Więcej informacji: <https://wajig.togaware.com>.

- Aktualizacja listy dostępnych pakietów i ich wersji:

`wajig update`

- Instalacja pakietu lub aktualizacja do najnowszej wersji:

`wajig install {{pakiet}}`

- Usunięcie pakietu i jego plików konfiguracyjnych:

`wajig purge {{pakiet}}`

- Wykonanie update, a następnie dist-upgrade:

`wajig daily-upgrade`

- Wyświetlenie rozmiaru zainstalowanych pakietów:

`wajig sizes`

- Lista wersji i dystrybucji dla wszystkich zainstalowanych pakietów:

`wajig versions`

- Lista wersji pakietów możliwych do aktualizacji:

`wajig toupgrade`

- Wyświetlenie pakietów, które posiadają zaleność od podanego pakietu:

`wajig dependents {{pakiet}}`
