# mktemp

> Maak een tijdelijk bestand of een tijdelijke map aan.
> Meer informatie: <https://man.openbsd.org/mktemp.1>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map als `$TMPDIR` niet is ingesteld (de standaard is platformafhankelijk, maar meestal `/tmp`):

`mktemp -p /{{pad/naar/tempdir}}`

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp {{/tmp/voorbeeld.XXXXXXXX}}`

- Gebruik een aangepast bestandsnaam-sjabloon:

`mktemp -t {{voorbeeld.XXXXXXXX}}`

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp -d`
