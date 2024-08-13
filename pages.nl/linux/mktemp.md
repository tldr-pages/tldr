# mktemp

> Maak een tijdelijk bestand of een tijdelijke map aan.
> Meer informatie: <https://www.gnu.org/software/coreutils/mktemp>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map (standaard is `$TMPDIR`, of `/tmp`):

`mktemp --tmpdir={{/pad/naar/tempdir}}`

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp {{/tmp/voorbeeld.XXXXXXXX}}`

- Gebruik een aangepast bestandsnaam-sjabloon:

`mktemp -t {{voorbeeld.XXXXXXXX}}`

- Maak een leeg tijdelijk bestand met de opgegeven extensie en toon het absolute pad:

`mktemp --suffix {{.ext}}`

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp --directory`
