# parted

> Een programma voor het manipuleren van partities.
> Zie ook: `partprobe`.
> Meer informatie: <https://www.gnu.org/software/parted/parted.html>.

- Start interactieve modus met de gespecificeerde schijf geselecteerd:

`sudo parted {{/dev/sdX}}`

- [Interactief] Toon partitie-informatie in interactieve modus:

`print`

- [Interactief] Selecteer een schijf in interactieve modus:

`select {{/dev/sdX}}`

- [Interactief] Maak een partitie van 16 GB aan met het gespecificeerde bestandssysteem in interactieve modus (`GPT`-partitietabel):

`mkpart {{partitie_naam}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- [Interactief] Maak een partitie van 16 GB aan met het gespecificeerde bestandssysteem in interactieve modus (`MBR`-partitietabel):

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- [Interactief] Wijzig de grootte van een partitie in interactieve modus:

`resizepart {{/dev/sdXN}} {{eindpositie_van_partitie}}`

- [Interactief] Verwijder een partitie in interactieve modus:

`rm {{/dev/sdXN}}`

- [Interactief] Toon de help:

`?`
