# lvm

> Gestionați volumele fizice, grupurile de volum și volumele logice utilizând componenta interactivă Logic Volume Manager (LVM).
> Mai multe informaţii: <https://man7.org/linux/man-pages/man8/lvm.8.html>

- Porniți Logic Volume Manager shell interactiv:

`sudo lvm`

- Lista comenzilor Logic Volume Manager:

`sudo lvm help`

- Inițializați o unitate sau o partiție pentru a fi utilizată ca volum fizic:

`sudo lvm pvcreate {{/dev/sdXY}}`

- Afișează informații despre volumele fizice:

`sudo lvm pvdisplay`

- Creați un grup de volum numit vg1 din volumul fizic pe `/dev/sdxy`:

`sudo lvm vgcreate {{vg1}} {{/dev/sdXY}}`

- Afișați informații despre grupurile de volum:

`sudo lvm vgdisplay`

- Creați un volum logic cu dimensiunea 10G din grupul de volum vg1:

`sudo lvm lvcreate -L {{10G}} {{vg1}}`

- Afișați informații despre volumele logice:

`sudo lvm lvdisplay`
