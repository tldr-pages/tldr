# apptainer inspect

> Mostra i metadati delle immagini container Apptainer.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_inspect.html>.

- Mostra le etichette di un'immagine (predefinito):

`apptainer inspect {{path/to/immagine.sif}}`

- Mostra il file di definizione utilizzato per costruire l'immagine:

`apptainer inspect {{[-d|--deffile]}} {{path/to/immagine.sif}}`

- Mostra lo script di avvio per l'immagine:

`apptainer inspect {{[-r|--runscript]}} {{path/to/immagine.sif}}`

- Mostra le variabili d'ambiente dell'immagine:

`apptainer inspect {{[-e|--environment]}} {{path/to/immagine.sif}}`

- Elenca tutte le app nel container:

`apptainer inspect --list-apps {{path/to/immagine.sif}}`

- Mostra tutti i dati disponibili in formato JSON:

`apptainer inspect --all {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer inspect {{[-h|--help]}}`
