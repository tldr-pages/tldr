# halt

> Deté, apaga o reinicia la màquina.
> Més informació: <https://manned.org/halt.8>.

- Deté la màquina:

`halt`

- Apaga la màquina (el mateix que `poweroff`):

`halt {{[-p|--poweroff]}}`

- Reinicia la màquina (el mateix que `reboot`):

`halt --reboot`

- Deté la màquina inmediatament sense contactar l'administrador de sistemes:

`halt {{[-f|--force]}}`

- Escriu l'entrada de wtpm shutdown sense aturar el sistema:

`halt {{[-w|--wtmp-only]}}`
