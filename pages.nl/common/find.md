# find

> Vind bestanden of mappen onder een mappenboom, recursief.
> Meer informatie: <https://manned.org/find>.

- Vind bestanden op basis van extensie:

`find {{root_pad}} -name '{{*.ext}}'`

- Vind bestanden die overeenkomen met meerdere pad-/naam patronen:

`find {{root_pad}} -path '{{**/path/**/*.ext}}' -or -name '{{*patroon*}}'`

- Vind mappen die overeenkomen met een gegeven naam, hoofdletterongevoelig:

`find {{root_pad}} -type d -iname '{{*lib*}}'`

- Vind bestanden die overeenkomen met een gegeven patroon, met uitsluiting van specifieke paden:

`find {{root_pad}} -name '{{*.py}}' -not -path '{{*/site-packages/*}}'`

- Vind bestanden die overeenkomen met een gegeven groottebereik, waarbij de recursieve diepte beperkt is tot "1":

`find {{root_pad}} -maxdepth 1 -size {{+500k}} -size {{-10M}}`

- Voer een commando uit voor elk bestand (gebruik `{}` binnen het commando om de bestandsnaam te openen):

`find {{root_pad}} -name '{{*.ext}}' -exec {{wc -l}} {} \;`

- Vind alle bestanden die vandaag zijn gewijzigd en geef de resultaten door aan een enkel commando als argumenten:

`find {{root_pad}} -daystart -mtime {{-1}} -exec {{tar -cvf archief.tar}} {} \+`

- Vind lege bestanden (0 bytes) of mappen en verwijder ze uitvoerig:

`find {{root_pad}} -type {{f|d}} -empty -delete -print`
