# lvmdump

> Raccoglie informazioni diagnostiche su LVM2 (Logical Volume Manager).
> Per impostazione predefinita, genera un archivio `.tar` compresso con dati di sistema e configurazione nella directory home.
> Maggiori informazioni: <https://manned.org/lvmdump>.

- Genera un dump base:

`lvmdump`

- Genera un dump esteso con metadati e informazioni sui daemon:

`lvmdump -a -l -m`

- Salva le informazioni in una directory invece che in un tarball:

`lvmdump -d {{percorso/della/directory}}`

- Visualizza la guida:

`lvmdump -h`
