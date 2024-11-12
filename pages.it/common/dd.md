# dd

> Converti e copia un file.
> Maggiori informazioni: <https://manned.org/dd.1p>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if={{percorso/del/file.iso}} of={{/dev/disco_usb}} status=progress`

- Clona un disco su un altro disco a blocchi con grandezza di 4 MiB e scarica le scritture prima che il comando termini:

`dd bs=4194304 conv=fsync if={{/dev/disco_sorgente}} of={{/dev/disco_destinazione}}`

- Genera un file con un numero specifico di byte randomici utilizzando il driver random del kernel:

`dd bs={{100}} count={{1}} if=/dev/urandom of={{percorso/del/file_random}}`

- Testa la performance in scrittura di un disco:

`dd bs={{1024}} count={{1000000}} if=/dev/zero of={{percorso/del/file_1GB}}`

- Crea un backup di sistema, salvalo in un file IMG (può essere ripristinato in seguito scambiando `if` e `of`), e mostra il progresso:

`dd if={{/dev/disco}} of={{percorso/del/file.img}} status=progress`
