# apptainer verify

> Verifica le firme digitali delle immagini container SIF.
> Vedi anche: `apptainer-sign`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_verify.html>.

- Verifica un'immagine container utilizzando il portachiavi PGP predefinito:

`apptainer verify {{path/to/immagine.sif}}`

- Verifica un'immagine container utilizzando un file di chiave pubblica specifico:

`apptainer verify --key {{path/to/pubblica.pem}} {{path/to/immagine.sif}}`

- Verifica un'immagine container utilizzando un file certificato:

`apptainer verify --certificate {{path/to/certificato.pem}} {{path/to/immagine.sif}}`

- Verifica tutti gli oggetti nell'immagine:

`apptainer verify {{[-a|--all]}} {{path/to/immagine.sif}}`

- Verifica un gruppo di oggetti specifico all'interno dell'immagine:

`apptainer verify {{[-g|--group-id]}} {{id_gruppo}} {{path/to/immagine.sif}}`

- Verifica un oggetto specifico per ID all'interno dell'immagine:

`apptainer verify {{[-i|--sif-id]}} {{id_oggetto}} {{path/to/immagine.sif}}`

- Mostra i risultati della verifica in formato JSON:

`apptainer verify {{[-j|--json]}} {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer verify {{[-h|--help]}}`
