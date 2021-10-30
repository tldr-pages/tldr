# borg

> Strumento di backup con deduplicazione.
> Crea backup locali o remoti che sono montabili come filesystem.
> Maggiori informazioni: <https://borgbackup.readthedocs.io/en/stable/usage/general.html>.

- Inizializza una repository (locale):

`borg init {{/percorso/a/repo_o_directory}}`

- Esegui il backup di una directory nella repository, creando un archivio chiamato "Lunedi":

`borg create --progress {{/percorso/a/repo_o_directory}}::{{Lunedi}} {{/percorso/a/directory_sorgente}}`

- Lista tutti gli archivi in una repository:

`borg list {{/percorso/a/repo_o_directory}}`

- Estrai una specifica directory dall'archivio "Lunedi" in una repository remota, escludendo tutti i file `.ext`:

`borg extract {{utente}}@{{host}}:{{/percorso/a/repo_o_directory}}::{{Lunedi}} {{percorso/a/cartella_destinazione}} --exclude '{{*.ext}}'`

- Riduci una repository eliminando tutti gli archivi più vecchi di 7 giorni, elencando i cambiamenti:

`borg prune --keep-within {{7d}} --list {{/percorso/a/repo_o_directory}}`

- Monta una repository come filesystem FUSE:

`borg mount {{/percorso/a/repo_o_directory}}::{{Lunedi}} {{/percorso/a/mountpoint}}`

- Mostra aiuto sul come creare archivi:

`borg create --help`
