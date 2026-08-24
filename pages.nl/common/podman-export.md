# podman export

> Exporteer het bestandssysteem van een container en sla het op als een tarball op de lokale machine.
> Zie ook: `podman import`, `podman save`.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-export.1.html>.

- Exporteer het bestandssysteem van een container naar een tar-bestand:

`podman export {{[-o|--output]}} {{pad/naar/bestand.tar}} {{container_naam_of_id}}`

- Exporteer het bestandssysteem van een container naar `stdout`:

`podman export {{container_naam_of_id}} > {{pad/naar/bestand.tar}}`
