# parted

> Un program de manipulare a partițiilor.
> A se vedea, de asemenea,: „partprobe”.
> Mai multe informaţii: <https://www.gnu.org/software/parted/parted.html>

- Lista partițiilor pe toate dispozitivele bloc:

`sudo parted --list`

- Porniți modul interactiv cu discul specificat selectat:

`sudo parted {{/dev/sdX}}`

- Creați o nouă tabelă de partiții cu tipul de etichetă specificat:

`sudo parted --script {{/dev/sdX}} mklabel {{aix|amiga|bsd|dvh|gpt|loop|mac|msdos|pc98|sun}}`

- Afișează informațiile despre partiție în modul interactiv:

`print`

- Selectați un disc în modul interactiv:

`select {{/dev/sdX}}`

- Creați o partiție de 16 GB cu sistemul de fișiere specificat în modul interactiv:

`mkpart {{primary|logical|extended}} {{btrfs|ext2|ext3|ext4|fat16|fat32|hfs|hfs+|linux-swap|ntfs|reiserfs|udf|xfs}} {{0%}} {{16G}}`

- Redimensionarea unei partiții în modul interactiv:

`resizepart {{/dev/sdXN}} {{end_position_of_partition}}`

- Eliminați o partiție în modul interactiv:

`rm {{/dev/sdXN}}`
