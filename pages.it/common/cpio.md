# cpio

> Copia file da/a archivi.
> Supporta i seguenti formati di archivio: cpio binario, vecchio ASCII, nuovo ASCII, crc, HPUX binario, HPUX vecchio ASCII, vecchio tar, e tar POSIX.1.
> Maggiori informazioni: <https://www.gnu.org/software/cpio>.

- Accetta una lista di nomi di file da standard input ed aggiungili ad un archivio in formato binario cpio:

`echo "{{file1}} {{file2}} {{file3}}" | cpio -o > {{archivio.cpio}}`

- Copia tutti i file e le directory in una directory ed aggiungili ad un archivio, in modalità verbosa:

`find {{percorso/della/directory}} | cpio -ov > {{archivio.cpio}}`

- Estrai file da un archivio, generando le directory necessarie, in modalità verbosa:

`cpio -idv < {{archivio.cpio}}`
