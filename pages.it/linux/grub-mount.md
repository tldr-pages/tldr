# grub-mount

> Monta un filesystem o un'immagine di filesystem in sola lettura usando i driver GRUB.
> Maggiori informazioni: <https://www.gnu.org/software/grub/manual/grub/grub.html#Invoking-grub_002dmount>.

- Monta un dispositivo a blocchi o un'immagine di filesystem su un punto di mount:

`grub-mount {{/dev/sdXY}} {{/mnt}}`

- Monta la seconda partizione di un'immagine disco completa, `-r` specifica il numero di partizione nell'immagine:

`grub-mount {{[-r|--root]}} {{2}} {{disk.img}} {{/mnt}}`

- Monta un dispositivo crittografato e richiede una passphrase:

`grub-mount {{[-C|--crypto]}} {{/dev/sdXY}} {{/mnt}}`

- Carica una chiave di crittografia ZFS da un file:

`grub-mount {{[-K|--zfs-key]}} /{{path/to/zfs.key}} {{/dev/sdX}} {{/mnt}}`

- Mostra output di debug per una categoria corrispondente:

`grub-mount {{[-d|--debug]}} {{string}} {{image}} {{/mnt}}`

- Abilita output verboso:

`grub-mount {{[-v|--verbose]}} {{image}} {{/mnt}}`

- Mostra aiuto:

`grub-mount {{[-?|--help]}}`

- Mostra versione:

`grub-mount --version`
