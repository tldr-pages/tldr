# rtcwake

> Introduceți o stare de repaus a sistemului până la ora de trezire specificată în raport cu ceasul bios.

- Arată dacă o alarmă este setată sau nu:

`sudo rtcwake -m show -v`

- Suspendați la berbec și trezire după 10 secunde:

`sudo rtcwake -m mem -s {{10}}`

- Suspendați pe disc (economie de energie mai mare) și trezire 15 minute mai târziu:

`sudo rtcwake -m disk --date +{{15}}min`

- Înghețați sistemul (mai eficient decât suspend-to-ram, dar linux > 3.9 necesar) și trezirea la o anumită dată și oră:

`sudo rtcwake -m freeze --date {{YYYYMMDDhhmm}}`

- Dezactivați o alarmă setată anterior:

`sudo rtcwake -m disable`

- Efectuați o funcționare uscată pentru a trezi computerul la un moment dat. (Apăsați Ctrl + C pentru a anula):

`sudo rtcwake -m on --date {{hh:ss}}`
