# cp

> Kopieer bestanden en directories.
> Meer informatie: <https://www.gnu.org/software/coreutils/cp>.

- Kopieer een bestand naar een andere locatie:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doelbestand.ext}}`

- Kopieer een bestand naar een andere directory, met behoud van de bestandsnaam:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doelmap}}`

- Kopieer de inhoud van een directory recursief naar een andere locatie (als de bestemming bestaat, wordt de directory erin gekopieerd):

`cp -R {{pad/naar/bronmap}} {{pad/naar/doelmap}}`

- Kopieer een directory recursief, in verbose modus (toont bestanden terwijl ze worden gekopieerd):

`cp -vR {{pad/naar/bronmap}} {{pad/naar/doelmap}}`

- Kopieer meerdere bestanden tegelijk naar een directory:

`cp -t {{pad/naar/doelmap}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Kopieer tekstbestanden naar een andere locatie, in interactieve modus (vraagt de gebruiker om bevestiging voordat overschrijven plaatsvindt):

`cp -i {{*.txt}} {{pad/naar/doelmap}}`

- Volg symbolische links voordat je kopieert:

`cp -L {{link}} {{pad/naar/doelmap}}`

- Gebruik het eerste argument als de doelmap (handig voor `xargs ... | cp -t <DEST_DIR>`):

`cp -t {{pad/naar/doelmap}} {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`
