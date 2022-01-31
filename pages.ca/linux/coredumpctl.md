# coredumpctl

> Recupera i processa volcats de memòria i les seves metadades.
> Més informació: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- Llista tots els volcats de memòria capturats:

`coredumpctl list`

- Llista tots els volcats de memòria capturats per un programa:

`coredumpctl list {{programa}}`

- Mostra informació sobre els volcats de memòria que coincideixin amb el `PID` d'un programa:

`coredumpctl info {{PID}}`

- Invoca el depurador fent servir l'últim volcat de memòria per un programa:

`coredumpctl debug {{programa}}`

- Extreu l'últim volcat de memòria a un fitxer:

`coredumpctl --output={{ruta/al/arxiu}} dump {{programa}}`
