# find

> Vind bestanden of mappen onder een mappenboom, recursief.
> Zie ook: `fd`.
> Meer informatie: <https://manned.org/find>.

- Vind bestanden op basis van extensie:

`find {{pad/naar/map}} -name '{{*.ext}}'`

- Vind bestanden die overeenkomen met meerdere pad-/naampatronen:

`find {{pad/naar/map}} -path '{{*/path/*/*.ext}}' -or -name '{{*patroon*}}'`

- Vind mappen die overeenkomen met een gegeven naam, hoofdletterongevoelig:

`find {{pad/naar/map}} -type d -iname '{{*lib*}}'`

- Vind bestanden die overeenkomen met een gegeven patroon, met uitsluiting van specifieke paden:

`find {{pad/naar/map}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Vind bestanden die overeenkomen met een gegeven groottebereik, waarbij de recursieve diepte beperkt is tot "1":

`find {{pad/naar/map}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Voer een commando uit voor elk bestand (gebruik `{}` binnen het commando om toegang te krijgen tot de bestandsnaam):

`find {{pad/naar/map}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Vind alle bestanden die vandaag zijn gewijzigd en geef de resultaten door aan een enkel commando als argumenten:

`find {{pad/naar/map}} -daystart -mtime {{-1}} -exec {{tar -cvf archief.tar}} {} \+`

- Vind lege bestanden of mappen en verwijder ze uitvoerig:

`find {{pad/naar/map}} -type {{f|d}} -empty -delete -print`
