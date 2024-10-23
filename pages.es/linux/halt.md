# halt

> Detiene, apaga o reinicia la máquina.
> Ver también: `poweroff`, `reboot`.
> Más información: <https://manned.org/halt.8>.

- Detiene el sistema:

`halt`

- Apaga el sistema (igual que `poweroff`):

`halt --poweroff`

- Reinicia el sistema (igual que `reboot`):

`halt --reboot`

- Apaga inmediatamente el sistema sin contactar al administrador:

`halt --force`

- Escribe la entrada de apagado en wtmp sin apagar el sistema:

`halt --wtmp-only`
