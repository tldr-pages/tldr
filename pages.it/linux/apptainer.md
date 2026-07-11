# apptainer

> Gestisce container per HPC e calcolo scientifico.
> Alcuni sottocomandi come `build`, `pull` e `push` hanno la propria documentazione d'uso.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli.html>.

- Scarica un container da Docker Hub:

`apptainer pull {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Scarica un container dalla Container Library:

`apptainer pull {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Costruisce un container da un file di definizione:

`apptainer build {{path/to/immagine.sif}} {{path/to/definizione.def}}`

- Avvia una shell interattiva all'interno di un container:

`apptainer shell {{path/to/immagine.sif}}`

- Esegue un comando all'interno di un container:

`apptainer exec {{path/to/immagine.sif}} {{comando}}`

- Esegue lo script di avvio predefinito di un container:

`apptainer run {{path/to/immagine.sif}}`

- Ispeziona i metadati di un container:

`apptainer inspect {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer {{[-h|--help]}}`
