# crane registry

> Dit commando biedt een registry-implementatie op een automatisch gekozen poort (:0), $PORT of --address.
> Het commando blokkeert terwijl de server pushes en pulls accepteert en de inhoud kan worden opgeslagen in het geheugen en op de schijf.
> Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_registry_serve.md>.

- Dien een registry-implementatie:

`crane registry serve`

- Adres om naar te luisteren:

`crane registry serve --address {{address_naam}}`

- Pad naar een directory waar blobs worden opgeslagen:

`crane registry serve --disk {{pad/naar/store_dir}}`

- Toon de help voor `crane registry`:

`crane registry {{[-h|--help]}}`

- Toon de help voor `crane registry serve`:

`crane registry serve {{[-h|--help]}}`
