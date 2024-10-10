# dmesg

> Escriu els missatges del kernel a la sortida estàndar.
> Més informació: <https://manned.org/dmesg>.

- Mostra els missatges del kernel:

`sudo dmesg`

- Mostra els missatges d'error del kernel:

`sudo dmesg --level err`

- Mostra els missatges del kernel i segueix llegint els nous, similar a `tail -f` (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -w`

- Mostra quanta memòria física hi ha disponible en el sistema:

`sudo dmesg | grep -i memory`

- Mostra tots els missatges del kernel, pàgina a pàgina:

`sudo dmesg | less`

- Mostra els missatges del kernel amb una estampa temporal (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -T`

- Mostra els missatges del kernel de forma llegible per humans (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -H`

- Pinta la sortida (disponible en kernels 3.5.0 i posteriors):

`sudo dmesg -L`
