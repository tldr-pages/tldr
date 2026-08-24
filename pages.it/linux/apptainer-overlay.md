# apptainer overlay

> Gestisce immagini overlay EXT3 scrivibili per container Apptainer.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_overlay.html>.

- Aggiunge un overlay scrivibile a un'immagine SIF esistente:

`apptainer overlay create {{[-s|--size]}} {{dimensione}} {{path/to/immagine.sif}}`

- Crea un'immagine overlay EXT3 scrivibile autonoma:

`apptainer overlay create {{[-s|--size]}} {{dimensione}} {{path/to/overlay.img}}`

- Crea un'immagine overlay sparse:

`apptainer overlay create {{[-s|--size]}} {{dimensione}} {{[-S|--sparse]}} {{path/to/overlay.img}}`

- Crea un overlay per l'uso con fakeroot:

`apptainer overlay create {{[-f|--fakeroot]}} {{[-s|--size]}} {{dimensione}} {{path/to/overlay.img}}`

- Crea un overlay con una directory specifica nel layout:

`apptainer overlay create --create-dir {{path/to/directory}} {{path/to/overlay.img}}`

- Mostra aiuto:

`apptainer overlay {{[-h|--help]}}`
