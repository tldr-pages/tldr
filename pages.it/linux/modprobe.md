# modprobe

> Aggiunge o rimuove moduli del kernel Linux.
> Maggiori informazioni: <https://manned.org/modprobe>.

- Fa finta di carica un modulo nel kernel, ma non lo fa veramente:

`sudo modprobe --dry-run {{nome_del_modulo}}`

- Carica un modulo nel kernel:

`sudo modprobe {{nome_del_modulo}}`

- Rimuove un modulo dal kernel:

`sudo modprobe --remove {{nome_del_modulo}}`

- Rimuove dal kernel un modulo e quelli che dipendono da quest'ultimo:

`sudo modprobe --remove-dependencies {{nome_del_modulo}}`

- Mostra le dipendenza di un modulo del kernel:

`sudo modprobe --show-depends {{nome_del_modulo}}`
