# shutdown

> Apaga y reinicia el sistema.
> Más información: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- Apaga ([h]alt) inmediatamente:

`shutdown -h now`

- Pone en reposo inmediatamente:

`shutdown -s now`

- [r]einicia inmediatamente:

`shutdown -r now`

- [r]einicia en 5 minutos:

`shutdown -r "+{{5}}"`

- Apaga a las 01:00 pm (Usa el reloj de 24 hs):

`shutdown -h {{1300}}`

- Reinicia el 10 de mayo de 2042 a las 11:30 am (Formato de ingreso: YYMMDDHHMM):

`shutdown -r {{4205101130}}`
