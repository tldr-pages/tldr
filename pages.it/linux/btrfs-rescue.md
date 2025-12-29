# btrfs rescue

> Tenta di recuperare un filesystem btrfs danneggiato.
> Maggiori informazioni: <https://btrfs.readthedocs.io/en/latest/btrfs-rescue.html>.

- Ricostruisce l'albero dei metadati del filesystem (molto lento):

`sudo btrfs {{[resc|rescue]}} {{[ch|chunk-recover]}} {{percorso/alla/partizione}}`

- Corregge problemi di allineamento della dimensione del dispositivo (es. impossibilità di montare il filesystem con mismatch dei byte totali del superblock):

`sudo btrfs {{[resc|rescue]}} {{[fix-de|fix-device-size]}} {{percorso/alla/partizione}}`

- Recupera un superblock corrotto dalle copie corrette (recupera la radice dell'albero del filesystem):

`sudo btrfs {{[resc|rescue]}} {{[s|super-recover]}} {{percorso/alla/partizione}}`

- Recupera da transazioni interrotte (corregge problemi di replay del log):

`sudo btrfs {{[resc|rescue]}} {{[z|zero-log]}} {{percorso/alla/partizione}}`

- Crea un dispositivo di controllo `/dev/btrfs-control` quando `mknod` non è installato:

`sudo btrfs {{[resc|rescue]}} {{[c|create-control-device]}}`
