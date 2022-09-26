# halt

> Deté, apaga o reinicia la màquina.
> Més informació: <https://www.man7.org/linux/man-pages/man8/halt.8.html>.

- Deté la màquina:

`halt`

- Apaga la màquina (el mateix que `poweroff`):

`halt --poweroff`

- Reinicia la màquina (el mateix que `reboot`):

`halt --reboot`

- Deté la màquina inmediatament sense contactar l'administrador de sistemes:

`halt --force --force`

- Escriu l'entrada de wtpm shutdown sense aturar el sistema:

`halt --wtmp-only`
