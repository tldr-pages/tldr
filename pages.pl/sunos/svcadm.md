# svcadm

> Manipuluj instancjami usług.
> Więcej informacji: <https://www.unix.com/man-page/linux/1m/svcadm>.

- Włącz usługę w bazie danych usług:

`svcadm enable {{nazwa_usługi}}`

- Wyłącz usługę:

`svcadm disable {{nazwa_usługi}}`

- Ponownie uruchom aktywną usługę:

`svcadm restart {{nazwa_usługi}}`

- Ponownie odczytaj pliki konfiguracyjne:

`svcadm refresh {{nazwa_usługi}}`

- Usuń usługę ze stanu konserwacji i ją uruchom:

`svcadm clear {{nazwa_usługi}}`
