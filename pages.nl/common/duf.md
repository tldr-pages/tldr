# duf

> Hulpprogramma voor schijfgebruik en vrije ruimte.
> Zie ook: `ncdu`, `df`.
> Meer informatie: <https://github.com/muesli/duf#usage>.

- Toon toegankelijke apparaten:

`duf`

- Toon alles (zoals pseudo, dubbele of ontoegankelijke bestandssystemen):

`duf --all`

- Toon alleen de gespecificeerde apparaten of mountpoints:

`duf {{pad/naar/map1 pad/naar/map2 ...}}`

- Sorteer de uitvoer op een gespecificeerd criterium:

`duf --sort {{size|used|avail|usage}}`

- Toon of verberg specifieke bestandssystemen:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- Sorteer de uitvoer op sleutel:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- Wijzig het thema (als `duf` het verkeerde thema gebruikt):

`duf --theme {{dark|light}}`
