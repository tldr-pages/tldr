# apptainer search

> Cerca immagini container in una Container Library.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_search.html>.

- Cerca immagini container che corrispondono a una query:

`apptainer search {{query}}`

- Cerca immagini container per un'architettura specifica:

`apptainer search --arch {{amd64|arm64|386|ppc64le|s390x}} {{query}}`

- Cerca solo immagini container firmate:

`apptainer search --signed {{query}}`

- Cerca in una Container Library specifica:

`apptainer search --library {{url_library}} {{query}}`

- Mostra aiuto:

`apptainer search {{[-h|--help]}}`
