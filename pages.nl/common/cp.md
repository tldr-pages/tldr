# cp

> Kopieer bestanden en directories.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html>.

- Kopieer een bestand naar een andere locatie:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doelbestand.ext}}`

- Kopieer een bestand naar een andere directory, met behoud van de bestandsnaam:

`cp {{pad/naar/bronbestand.ext}} {{pad/naar/doelmap}}`

- Kopieer de inhoud van een directory recursief naar een andere locatie (als de bestemming bestaat, wordt de directory erin gekopieerd):

`cp {{[-r|--recursive]}} {{pad/naar/bronmap}} {{pad/naar/doelmap}}`

- Kopieer een directory recursief, in verbose modus (toont bestanden terwijl ze worden gekopieerd):

`cp {{[-vr|--verbose --recursive]}} {{pad/naar/bronmap}} {{pad/naar/doelmap}}`

- Kopieer meerdere bestanden tegelijk naar een directory:

`cp {{[-t|--target-directory]}} {{pad/naar/doelmap}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Kopieer alle bestanden met een specifieke extensie naar een andere locatie, in interactieve modus (vraagt de gebruiker om bevestiging voordat overschrijven plaatsvindt):

`cp {{[-i|--interactive]}} {{*.ext}} {{pad/naar/doelmap}}`

- Volg symbolische links voordat je kopieert:

`cp {{[-L|--dereference]}} {{link}} {{pad/naar/doelmap}}`

- Gebruik het volledige pad van bronbestanden, maak eventuele missende tussenliggende mappen aan tijdens het kopiëren:

`cp --parents {{bron/pad/naar/bestand}} {{pad/naar/doel_bestand}}`
