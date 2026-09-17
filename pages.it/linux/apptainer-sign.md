# apptainer sign

> Aggiunge firme digitali a un'immagine container SIF.
> Vedi anche: `apptainer-verify`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_sign.html>.

- Firma un'immagine container utilizzando la chiave PGP predefinita:

`apptainer sign {{path/to/immagine.sif}}`

- Firma un'immagine container utilizzando un file di chiave privata specifico:

`apptainer sign --key {{path/to/privata.pem}} {{path/to/immagine.sif}}`

- Firma un'immagine container utilizzando un indice di chiave PGP specifico:

`apptainer sign {{[-k|--keyidx]}} {{indice_chiave}} {{path/to/immagine.sif}}`

- Firma un gruppo di oggetti specifico all'interno dell'immagine:

`apptainer sign {{[-g|--group-id]}} {{id_gruppo}} {{path/to/immagine.sif}}`

- Firma un oggetto specifico per ID all'interno dell'immagine:

`apptainer sign {{[-i|--sif-id]}} {{id_oggetto}} {{path/to/immagine.sif}}`

- Mostra aiuto:

`apptainer sign {{[-h|--help]}}`
