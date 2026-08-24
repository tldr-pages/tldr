# podman save

> Sla een image op in een lokaal bestand of map.
> Zie ook: `podman load`, `podman export`.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-save.1.html>.

- Sla een image op in een tar-bestand:

`podman save {{[-o|--output]}} {{pad/naar/bestand.tar}} {{image:tag}}`

- Sla een image op in `stdout`:

`podman save {{image:tag}} > {{pad/naar/bestand.tar}}`

- Sla een image op met compressie:

`podman save {{image:tag}} | {{[gzip|bzip2|xz|zstd|zstdchunked]}} > {{pad/naar/bestand.tar[.gz|.bz2|.xz|.zst|.zst]}}`

- Zet een image over naar een systeem op afstand met on-the-fly compressie en voortgangsbalk:

`podman save {{image:tag}} | zstd {{[-T|--threads]}} 0 --ultra | pv | ssh {{gebruikersnaam}}@{{remote_host}} podman load`
