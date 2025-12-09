# reboot

> Reinicia el sistema.
> Vea también: `halt`, `poweroff`.
> Más información: <https://manned.org/reboot.8>.

- Reinicia inmediatamente:

`reboot`

- Apaga el sistema (igual que `poweroff`):

`reboot {{[-p|--poweroff]}}`

- Detiene (termina todos los procesos y apaga la CPU) el sistema (igual que `halt`):

`reboot --halt`

- Reinicia inmediatamente sin contactar al administrador del sistema:

`reboot {{[-f|--force]}}`

- Escribe la entrada wtmp de apagado sin reiniciar el sistema:

`reboot {{[-w|--wtmp-only]}}`
