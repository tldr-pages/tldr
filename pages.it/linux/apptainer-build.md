# apptainer build

> Costruisce immagini container Apptainer.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_build.html>.

- Costruisce un container da un file di definizione:

`apptainer build {{path/to/immagine.sif}} {{path/to/definizione.def}}`

- Costruisce un container da Docker Hub:

`apptainer build {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Costruisce un container dalla Container Library:

`apptainer build {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Costruisce una directory sandbox scrivibile invece di un file immagine:

`apptainer build {{[-s|--sandbox]}} {{path/to/directory}} docker://{{immagine}}:{{tag}}`

- Costruisce un container senza utilizzare la cache:

`apptainer build --disable-cache {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Forza la sovrascrittura di un file immagine esistente:

`apptainer build {{[-F|--force]}} {{path/to/immagine.sif}} {{path/to/definizione.def}}`

- Costruisce utilizzando fakeroot per build non privilegiate:

`apptainer build {{[-f|--fakeroot]}} {{path/to/immagine.sif}} {{path/to/definizione.def}}`

- Mostra aiuto:

`apptainer build {{[-h|--help]}}`
