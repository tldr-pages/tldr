# reboot

> Reinicia la màquina.
> Més informació: <https://www.man7.org/linux/man-pages/man8/reboot.8.html>.

- Reinicia inmediatament:

`reboot`

- Apaga el sistema (el mateix que `poweroff`):

`reboot --poweroff`

- Atura el sistema (el mateix que halt):

`reboot --halt`

- Reinicia inmediatament sense contactar l'adminstrador del sistema:

`reboot --force --force`

- Escriu l'entrada wtmp shutdown sense reiniciar el sistema:

`reboot --wtmp-only`
