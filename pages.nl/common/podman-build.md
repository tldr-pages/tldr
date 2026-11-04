# podman build

> Daemonloze tool voor het bouwen van container-images.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Maak een image aan met behulp van een `Dockerfile` of `Containerfile` in de opgegeven map:

`podman build {{pad/naar/map}}`

- Maak een image aan met een opgegeven tag:

`podman build {{[-t|--tag]}} {{image_naam:versie}} {{pad/naar/map}}`

- Maak een image aan vanuit een niet-standaard bestand:

`podman build {{[-f|--file]}} {{Containerfile.anders}} .`

- Maak een image aan zonder eerder gecachte images te gebruiken:

`podman build --no-cache {{pad/naar/map}}`

- Maak een image aan waarbij alle uitvoer wordt onderdrukt:

`podman build {{[-q|--quiet]}} {{pad/naar/map}}`
