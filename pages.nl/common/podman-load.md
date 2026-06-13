# podman load

> Laad een image uit een oci-archief of een docker-archief gemaakt met `podman save`.
> Zie ook: `podman save`, `podman import`.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-load.1.html>.

- Laad een image vanuit een tar-bestand:

`podman load {{[-i|--input]}} {{pad/naar/bestand.tar}}`

- Laad een image vanuit een gecomprimeerd tar-bestand:

`podman load {{[-i|--input]}} {{pad/naar/bestand.tar[.gz|.bz2|.xz|.zst]}}`

- Laad een image en toon stille uitvoer (toon alleen de image-ID):

`podman load {{[-q|--quiet]}} {{[-i|--input]}} {{pad/naar/bestand.tar}}`

- Laad een image van `stdin`:

`podman < {{pad/naar/bestand.tar}} load`
