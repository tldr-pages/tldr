# md5sum

> Calcola i checksum crittografici di tipo MD5.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/md5sum>.

- Calcolare il checksum MD5 di un file:

`md5sum {{percorso/del/file}}`

- Calcola i checksum MD5 per più di un file:

`md5sum {{percorso/del/file1}} {{percorso/del/file2}}`

- Verifica che tutti i file abbiano checksum corrispondenti al file di MD5SUM:

`md5sum -c {{percorso/del/file.md5}}`

- Calcola il checksum MD5 dal standard input:

`echo "{{testo}}" | md5sum`
