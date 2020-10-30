# shutdown

> Detiene, apaga o reinicia la máquina.

- Detiene inmediatamente:

`shutdown -H now`

- Apaga inmediatamente:

`shutdown -h now`

- Reinicia inmediatamente:

`shutdown -r now`

- Reinicia dentro de 5 minutos:

`shutdown -r +{{5}} &`

- Apaga a la 1:00 PM (formato 24h):

`shutdown -h 13:00`

- Cancela una operación de apagado/reinicio pendiente:

`shutdown -c`
