# btrfs scrub

> Scrub dei filesystem btrfs per verificare l'integrità dei dati.
> Si consiglia di eseguire uno scrub una volta al mese.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-scrub.html>.

- Avvia uno scrub:

`sudo btrfs {{[sc|scrub]}} start {{percorso/al/mount_btrfs}}`

- Mostra lo stato di uno scrub in corso o dell'ultimo completato:

`sudo btrfs {{[sc|scrub]}} status {{percorso/al/mount_btrfs}}`

- Annulla uno scrub in corso:

`sudo btrfs {{[sc|scrub]}} {{[c|cancel]}} {{percorso/al/mount_btrfs}}`

- Riprende uno scrub precedentemente annullato:

`sudo btrfs {{[sc|scrub]}} {{[r|resume]}} {{percorso/al/mount_btrfs}}`

- Avvia uno scrub, ma non mette il programma in [B]ackground:

`sudo btrfs {{[sc|scrub]}} start -B {{percorso/al/mount_btrfs}}`

- Avvia uno scrub in modalità silenziosa (non stampa errori o statistiche):

`sudo btrfs {{[sc|scrub]}} start {{[-q|--quiet]}} {{percorso/al/mount_btrfs}}`
