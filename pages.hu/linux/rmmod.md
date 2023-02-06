# rmmod

> Modulok eltávolítása a Linux kernelből. További információ: <https://manned.org/rmmod>.

- Modul eltávolítása a rendszermagból:

`sudo rmmod {{module_name}}`

- Egy modul eltávolítása a rendszermagból és a részletes információk megjelenítése:

`sudo rmmod --verbose {{module_name}}`

- Egy modul eltávolítása a rendszermagból és a hibák küldése a syslogba a standard hiba helyett:

`sudo rmmod --syslog {{module_name}}`

- Súgó megjelenítése:

`rmmod --help`

- Verzió megjelenítése:

`rmmod --version`
