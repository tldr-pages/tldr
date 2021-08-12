# fdisk

> Un program pentru gestionarea tabelelor de partiții și a partițiilor pe un hard disk.
> A se vedea, de asemenea,: „partprobe”.
> Mai multe informaţii: <https://manned.org/fdisk>

- Lista partițiilor:

`sudo fdisk -l`

- Porniți manipulatorul de partiții:

`sudo fdisk {{/dev/sdX}}`

- După partiționarea unui disc, creați o partiție:

`n`

- După partiționarea unui disc, selectați o partiție pentru a șterge:

`d`

- După partiționarea unui disc, vizualizați tabela de partiții:

`p`

- După partiționarea unui disc, scrieți modificările efectuate:

`w`

- După partiționarea unui disc, aruncați modificările efectuate:

`q`

- După partiționarea unui disc, deschideți un meniu de ajutor:

`m`
