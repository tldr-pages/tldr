# docker container cp

> Kopieer bestanden of mappen tussen host- en containerbestandssystemen.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/cp/>.

- Kopieer een bestand of map van de host naar een container:

`docker {{[cp|container cp]}} {{pad/naar/bestand_of_map_op_host}} {{container_naam}}:{{pad/naar/bestand_of_map_in_container}}`

- Kopieer een bestand of map van een container naar de host:

`docker {{[cp|container cp]}} {{container_naam}}:{{pad/naar/bestand_of_map_in_container}} {{pad/naar/bestand_of_map_op_host}}`

- Kopieer een bestand of map van de host naar een container, symlinks volgend (kopieert de symlinked bestanden direct, niet de symlinks zelf):

`docker {{[cp|container cp]}} {{[-L|--follow-link]}} {{path/to/symlink_on_host}} {{container_naam}}:{{pad/naar/bestand_of_map_in_container}}`
