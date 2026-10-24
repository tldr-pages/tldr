# crane index append

> Voeg een manifest toe aan een remote index.
> Dit subcommando pusht een index op basis van een (optionele) basisindex, met toegevoegde manifests.
> Het platform voor toegevoegde manifests wordt afgeleid van het configuratiebestand of weggelaten als dat niet haalbaar is.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_append.md>.

- Voeg een manifest toe aan een remote index:

`crane index append`

- Voeg specifieke manifests toe aan de basisindex:

`crane index append {{[-m|--manifest]}} {{manifest_naam1 manifest_naam2 ...}}`

- Pas een tag toe op de resulterende image:

`crane index append {{[-t|--tag]}} {{tag_naam}}`

- Gebruik Docker-media in plaats van OCI voor een lege basisindex:

`crane index append --docker-empty-base`

- Voeg elk van zijn kinderen toe in plaats van de index zelf (standaard waar):

`crane index append --flatten`

- Toon de help:

`crane index append {{[-h|--help]}}`
