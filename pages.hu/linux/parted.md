# parted

> Partíciókezelő program. Lásd még: `partprobe`. További információ: <https://www.gnu.org/software/parted/parted.html>.

- Az összes blokkeszköz partícióinak listázása:

`sudo parted --list`

- Interaktív mód indítása a megadott lemez kijelölésével:

`sudo parted {{/dev/sdX}}`

- Új partíciós tábla létrehozása a megadott címke-típusban:

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Partíciós információk megjelenítése interaktív módban:

`print`

- Lemez kiválasztása interaktív módban:

`select {{/dev/sdX}}`

- 16 GB-os partíció létrehozása a megadott fájlrendszerrel interaktív módban:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- Egy partíció átméretezése interaktív módban:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Partíció eltávolítása interaktív módban:

`rm {{/dev/sdXN}}`
