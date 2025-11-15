# halt

> Detiene, apaga o reinicia la máquina.
> Ver también: `poweroff`, `reboot`.
> Más información: <https://manned.org/halt.8>.

- Detiene el sistema:

`halt`

- Apaga el sistema (igual que `poweroff`):

`halt {{[-p|--poweroff]}}`

- Reinicia el sistema (igual que `reboot`):

`halt --reboot`

- Apaga inmediatamente el sistema sin contactar al administrador:

`halt {{[-f|--force]}}`

- Escribe la entrada de apagado en wtmp sin apagar el sistema:

`halt {{[-w|--wtmp-only]}}`
