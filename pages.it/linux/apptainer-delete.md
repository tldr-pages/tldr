# apptainer delete

> Elimina immagini container da un repository remoto.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_delete.html>.

- Elimina un'immagine dalla Container Library:

`apptainer delete library://{{utente/collezione/container}}:{{tag}}`

- Elimina un'immagine per un'architettura specifica:

`apptainer delete {{[-A|--arch]}} {{amd64|arm64|ppc64le}} library://{{utente/collezione/container}}:{{tag}}`

- Forza l'eliminazione di un'immagine senza conferma:

`apptainer delete {{[-F|--force]}} library://{{utente/collezione/container}}:{{tag}}`

- Elimina un'immagine da un server library specifico:

`apptainer delete --library {{https://library.example.com}} library://{{utente/collezione/container}}:{{tag}}`

- Elimina un'immagine utilizzando HTTP invece di HTTPS:

`apptainer delete --no-https library://{{hostname/utente/collezione/container}}:{{tag}}`

- Mostra aiuto:

`apptainer delete {{[-h|--help]}}`
