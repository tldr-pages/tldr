# shutdown

> Apaga y reinicia el sistema.
> Más información: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

- Apaga (detiene) inmediatamente:

`shutdown -h now`

- Pone en suspensión de manera inmediatamente:

`shutdown -s now`

- Reinicia inmediatamente:

`shutdown -r now`

- Reinicia en 5 minutos:

`shutdown -r «+{{5}}»`

- Apaga (detiene) a las 13:00 (utiliza el formato de 24 horas):

`shutdown -h {{1300}}`

- Reinicia el 10 de mayo de 2042 a las 11:30 h (formato de entrada: AAAAMMDDHHMM):

`shutdown -r {{4205101130}}`
