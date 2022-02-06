# shutdown

> Deté, apaga o reinicia la màquina.
> Més informació: <https://manned.org/shutdown.8>.

- Deté inmediatament:

`shutdown -h now`

- Reinicia inmediatament:

`shutdown -r now`

- Reinicia després de 5 minuts:

`shutdown -r +{{5}} &`

- Apaga a la 1:00 PM (format 24h):

`shutdown -h 13:00`

- Cancel·la una operació d'apagat/reinici pendent:

`shutdown -c`
