# apptainer pull

> Scarica immagini container da sorgenti remote.
> Vedi anche: `apptainer-push`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_pull.html>.

- Scarica un container da Docker Hub:

`apptainer pull {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Scarica un container dalla Container Library:

`apptainer pull {{path/to/immagine.sif}} library://{{utente/collezione/container}}:{{tag}}`

- Scarica un container da un registro OCI:

`apptainer pull {{path/to/immagine.sif}} oras://{{registry/namespace/immagine}}:{{tag}}`

- Scarica un container per un'architettura specifica:

`apptainer pull --arch {{amd64|arm64|ppc64le}} {{path/to/immagine.sif}} library://{{immagine}}:{{tag}}`

- Forza la sovrascrittura di un file immagine esistente:

`apptainer pull {{[-F|--force]}} {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Scarica un container come directory sandbox scrivibile:

`apptainer pull --sandbox {{path/to/directory}} docker://{{immagine}}:{{tag}}`

- Scarica un container senza utilizzare la cache:

`apptainer pull --disable-cache {{path/to/immagine.sif}} docker://{{immagine}}:{{tag}}`

- Mostra aiuto:

`apptainer pull {{[-h|--help]}}`
