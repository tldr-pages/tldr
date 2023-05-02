# assimp

> Client da linea di comando per la Open Asset Import Library.
> Supporta il caricamento di 40+ formati di file per modelli 3D, e l'espoerazione di diversi formati 3D popolari.
> Maggiori informazioni: <https://assimp-docs.readthedocs.io/>.

- Elenca tutti i formati supportati:

`assimp listext`

- Elenca tutti i formati supportati per l'esportazione:

`assimp listexport`

- Converti un file a uno dei tipi supportati, utilizzando i parametri predefiniti:

`assimp export {{file_input.stl}} {{file_output.obj}}`

- Converti un file utilizzando parametri personalizzati (il file dox_cmd.h nel source code di assimp contiene una lista di parametri disponibili):

`assimp export {{file_input.stl}} {{file_output.obj}} {{parametri}}`

- Mostra un riepilogo del contenuto di un file:

`assimp info {{percorso/del/file}}`

- Elenca tutti i sottocomandi disponibili (detti "verbs"):

`assimp help`

- Chiedi aiuto per uno specifico sottocomando (ad esempio riguardo i suoi parametri):

`assimp {{sottocomando}} --help`
