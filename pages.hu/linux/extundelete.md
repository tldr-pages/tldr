# extundelete

> Törölt fájlok visszaállítása ext3 vagy ext4 partíciókról a napló elemzése révén. Lásd még: `date` a Unix időinformációkért és `umount` a partíciók leválasztásáért. További információ: <http://extundelete.sourceforge.net>.

- Az X eszköz N partícióján található összes törölt fájl helyreállítása:

`sudo extundelete {{/dev/sdXN}} --restore-all`

- Egy fájl visszaállítása a root-hoz viszonyított elérési útvonalról (Ne kezdje az elérési utat a `/`):

`extundelete {{/dev/sdXN}} --restore-file {{path/to/file}}`

- Könyvtár visszaállítása a root-hoz viszonyított elérési útvonalról (ne kezdje az elérési utat a `/`):

`extundelete {{/dev/sdXN}} --restore-directory {{path/to/directory}}`

- A 2020. január 1. után (Unix-idő szerint) törölt összes fájl visszaállítása:

`extundelete {{/dev/sdXN}} --restore-all --after {{1577840400}}`
