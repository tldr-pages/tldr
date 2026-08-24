# btrfs

> Un filesystem basato sul principio copy-on-write (COW) per Linux.
> Alcuni sottocomandi come `device` hanno la propria documentazione di utilizzo.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs.html>.

- Crea sottovolume:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{percorso/al/sottovolume}}`

- Elenca sottovolumi:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{percorso/al/mount_point}}`

- Mostra informazioni sull'utilizzo dello spazio:

`sudo btrfs {{[f|filesystem]}} df {{percorso/al/mount_point}}`

- Abilita quota:

`sudo btrfs {{[qu|quota]}} {{[e|enable]}} {{percorso/al/sottovolume}}`

- Mostra quota:

`sudo btrfs {{[qg|qgroup]}} {{[s|show]}} {{percorso/al/sottovolume}}`
