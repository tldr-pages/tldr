# podman import

> Importeer een tarball sla op als een bestandssysteem image.
> Zie ook: `podman export`, `podman save`.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-import.1.html>.

- Importeer een tarball van een lokaal bestand en maak een image:

`podman import {{pad/naar/tarball.tar}} {{image:tag}}`

- Importeer een tarball vanaf een URL:

`podman import {{https://example.com/image.tar}} {{image:tag}}`

- Importeer een tarball en voeg een commit bericht toe:

`podman import {{[-m|--message]}} "{{commit_bericht}}" {{pad/naar/tarball.tar}} {{image:tag}}`

- Importeer een tarball en stel een standaard commando in (nodig voor het uitvoeren van de container):

`podman import {{[-c|--change]}} CMD={{/bin/bash}} {{pad/naar/tarball.tar}} {{image:tag}}`
