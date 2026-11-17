# e2fsck

> Controleer een Linux ext2/ext3/ext4-bestandssysteem. De partitie moet ontkoppeld zijn.
> Meer informatie: <https://manned.org/e2fsck>.

- Controleer het bestandssysteem en rapporteer beschadigde blokken:

`sudo e2fsck {{/dev/sdXN}}`

- Controleer het bestandssysteem en herstel beschadigde blokken automatisch ([p]reen):

`sudo e2fsck -p {{/dev/sdXN}}`

- Controleer het bestandssysteem in alleen-lezenmodus:

`sudo e2fsck -c {{/dev/sdXN}}`

- [f]orceer controle, zelfs als het bestandssysteem schoon lijkt:

`sudo e2fsck -f {{/dev/sdXN}}`

- Voer een uitgebreide, niet-destructieve lees-/schrijftest uit op slechte blokken en zet ze op de zwarte lijst:

`sudo e2fsck -fccky {{/dev/sdXN}}`
