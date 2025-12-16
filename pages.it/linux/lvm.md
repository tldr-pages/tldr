# lvm

> Gestisci volumi fisici, gruppi di volumi e volumi logici utilizzando la shell interattiva Logical Volume Manager (LVM).
> Maggiori informazioni: <https://manned.org/lvm>.

- Avvia la shell interattiva Logical Volume Manager:

`sudo lvm`

- Inizializza un'unità o partizione da utilizzare come volume fisico:

`sudo lvm pvcreate {{/dev/sdXY}}`

- Visualizza informazioni sui volumi fisici:

`sudo lvm pvdisplay`

- Crea un gruppo di volumi chiamato vg1 dal volume fisico su `/dev/sdXY`:

`sudo lvm vgcreate vg1 {{/dev/sdXY}}`

- Visualizza informazioni sui gruppi di volumi:

`sudo lvm vgdisplay`

- Crea un volume logico con dimensione 10G dal gruppo di volumi vg1:

`sudo lvm lvcreate {{[-L|--size]}} 10G vg1`

- Visualizza informazioni sui volumi logici:

`sudo lvm lvdisplay`

- Visualizza la guida per un comando specifico:

`lvm help {{command}}`
