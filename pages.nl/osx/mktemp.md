# mktemp

> Maak een tijdelijk bestand of een tijdelijke map aan.
> Meer informatie: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map (standaard is de uitvoer van `getconf DARWIN_USER_TEMP_DIR`, of `/tmp`):

`mktemp --tmpdir {{/pad/naar/tempdir}}`

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp {{/tmp/voorbeeld.XXXXXXXX}}`

- Gebruik een aangepaste bestandsnaam-prefix:

`mktemp -t {{voorbeeld}}`

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp --directory`
