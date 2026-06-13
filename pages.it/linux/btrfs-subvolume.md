# btrfs subvolume

> Gestisce sottovolumi e snapshot btrfs.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-subvolume.html>.

- Crea un nuovo sottovolume vuoto:

`sudo btrfs {{[su|subvolume]}} {{[c|create]}} {{percorso/al/nuovo_sottovolume}}`

- Elenca tutti i sottovolumi e snapshot nel filesystem specificato:

`sudo btrfs {{[su|subvolume]}} {{[l|list]}} {{percorso/al/filesystem_btrfs}}`

- Elimina un sottovolume:

`sudo btrfs {{[su|subvolume]}} {{[d|delete]}} {{percorso/al/sottovolume}}`

- Crea uno snapshot [r]ead-only di un sottovolume esistente:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} -r {{percorso/al/sottovolume_sorgente}} {{percorso/al/target}}`

- Crea uno snapshot read-write di un sottovolume esistente:

`sudo btrfs {{[su|subvolume]}} {{[sn|snapshot]}} {{percorso/al/sottovolume_sorgente}} {{percorso/al/target}}`

- Mostra informazioni dettagliate su un sottovolume:

`sudo btrfs {{[su|subvolume]}} {{[sh|show]}} {{percorso/al/sottovolume}}`
