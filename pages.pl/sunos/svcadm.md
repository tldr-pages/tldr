# svcadm

> Manipulowanie instancjami usług.
> Więcej informacji: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Włączenie usługi w bazie danych usług:

`svcadm enable {{nazwa_uslugi}}`

- Wyłączenie usługi:

`svcadm disable {{nazwa_uslugi}}`

- Ponowne uruchomienie aktywnej usługi:

`svcadm restart {{nazwa_uslugi}}`

- Usługa poleceń do ponownego odczytu plików konfiguracyjnych:

`svcadm refresh {{nazwa_uslugi}}`

- Usunięcie usługi ze stanu konserwacji i polecenie jej uruchomienia:

`svcadm clear {{nazwa_uslugi}}`
