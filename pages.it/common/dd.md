# dd

> Converti e copia un file.
> Maggiori informazioni: <https://manned.org/man/dd.1p>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if={{percorso/del/file.iso}} of={{/dev/disco_usb}} status=progress`

- Clona un disco in un altro a blocchi di 4MB, ignora gli errori e mostra il progresso:

`dd bs=4M conv=noerror status=progress if={{/dev/disco_sorgente}} of={{/dev/disco_destinazione}}`

- Genera un file di 100 byte randomici utilizzando il driver random del kernel:

`dd bs=100 count={{1}} if=/dev/urandom of={{percorso/del/file_random}}`

- Testa la performance in scrittura di un disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{percorso/del/file_1GB}}`
