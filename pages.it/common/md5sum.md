# md5sum

> Calcola i checksum crittografici di tipo MD5.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/md5sum>.

- Calcolare il checksum MD5 di un file:

`md5sum {{percorso/al/file}}`

- Calcola i checksum MD5 per più di un file:

`md5sum {{percorso/al/file1}} {{percorso/al/file2}}`

- Verifica che tutti i file abbiano checksum corrispondenti al file di MD5SUM:

`md5sum -c {{percorso/al/file.md5}}`

- Calcola il checksum MD5 dal standard input:

`echo "{{testo}}" | md5sum`
