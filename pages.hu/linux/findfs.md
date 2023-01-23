# findfs

> Megkeres egy fájlrendszert címke vagy UUID alapján. További információ: <https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>.

- Blokkeszközök keresése fájlrendszercímke alapján:

`findfs LABEL={{label}}`

- Keresés fájlrendszer UUID alapján:

`findfs UUID={{uuid}}`

- Keresés partíciócímke alapján (GPT vagy MAC partíciós tábla):

`findfs PARTLABEL={{partition_label}}`

- Keresés a partíció UUID-je alapján (csak GPT partíciós tábla):

`findfs PARTUUID={{partition_uuid}}`
