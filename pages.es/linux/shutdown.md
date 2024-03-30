# shutdown

> Apaga y reinicia el sistema.
> Más información: <https://manned.org/shutdown.8>.

- Apaga ([h]alt) inmediatamente:

`shutdown -h now`

- [r]einicia inmediatamente:

`shutdown -r now`

- [r]einicia en 5 minutos:

`shutdown -r +{{5}} &`

- Apaga a las 01:00 pm (Usa el reloj de 24[h]):

`shutdown -h 13:00`

- [c]ancela una operación pendiente de apagado/reinicio:

`shutdown -c`
