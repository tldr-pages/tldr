# cpio

> Copia file da/a archivi.
> Supporta i seguenti formati di archivio: cpio binario, vecchio ASCII, nuovo ASCII, crc, HPUX binario, HPUX vecchio ASCII, vecchio tar, e tar POSIX.1.
> Maggiori informazioni: <https://www.gnu.org/software/cpio/manual/cpio.html#Invoking-cpio>.

- Accetta una lista di nomi di file da `stdin` ed aggiungili ad un archivio (copy-[o]ut) in formato binario cpio:

`echo "{{percorso/del/file1 percorso/del/file2 ...}}" | cpio {{[-o|--create]}} > {{archivio.cpio}}`

- Copia tutti i file e le directory in una directory ed aggiungili ad un archivio (copy-[o]ut), in modalità verbosa:

`find {{percorso/della/directory}} | cpio {{[-ov|--create --verbose]}} > {{archivio.cpio}}`

- Estrai file da un archivio (copy-[i]n), generando le directory necessarie, in modalità verbosa:

`cpio < {{archivio.cpio}} {{[-idv|--extract --make-directories --verbose]}}`
