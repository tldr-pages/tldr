# dd

> Converti e copia un file.
> Maggiori informazioni: <https://manned.org/man/dd.1p>.

- Crea un disco USB avviabile da un file ISO e mostra il progresso:

`dd if={{file.iso}} of=/dev/{{disco_usb}} status=progress`

- Clona un disco in un altro a blocchi di 4MB, ignora gli errori e mostra il progresso:

`dd if=/dev/{{disco_sorgente}} of=/dev/{{disco_destinazione}} bs=4M conv=noerror status=progress`

- Genera un file di 100 byte randomici utilizzando il driver random del kernel:

`dd if=/dev/urandom of={{file_random}} bs=100 count=1`

- Testa la performance in scrittura di un disco:

`dd if=/dev/zero of={{file_1GB}} bs=1024 count=1000000`

- Mostra il progresso di un'operazione dd in corso (comando da eseguire in un'altra shell):

`kill -USR1 $(pgrep -x dd)`
