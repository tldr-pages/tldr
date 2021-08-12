# extundelete

> Recuperați fișierele șterse din partițiile ext3 sau ext4 analizând jurnalul.
> A se vedea, de asemenea, `date` pentru informații de timp Unix și `umount` pentru demontarea partițiilor.
> Mai multe informaţii: <http://extundelete.sourceforge.net>

- Restaurați toate fișierele șterse din interiorul partiției N pe dispozitivul X:

`sudo extundelete {{/dev/sdXN}} --restore-all`

- Restaurați un fișier dintr-o cale relativă la rădăcină (Nu porniți calea cu `/`):

`extundelete {{/dev/sdXN}} --restore-file {{path/to/file}}`

- Restaurați un director dintr-o cale relativă la rădăcină (Nu porniți calea cu `/`):

`extundelete {{/dev/sdXN}} --restore-directory {{path/to/directory}}`

- Restaurați toate fișierele șterse după 1 ianuarie 2020 (în timp Unix):

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`
