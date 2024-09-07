# jq

> Ein JSON-Verarbeiter für die Kommandozeile mit einer domänenspezifischen Sprache.
> Weitere Informationen: <https://jqlang.github.io/jq/manual/>.

- Führe den angegebenen Ausdruck aus (gib farbiges und formatiertes JSON aus):

`{{cat pfad/zu/datei.json}} | jq '.'`

- Führe ein gegebenes Skript aus:

`{{cat pfad/zu/datei.json}} | jq --from-file {{pfad/zu/skript.jq}}`

- Übergib bestimmte Argumente:

`{{cat pfad/zu/datei.json}} | jq {{--arg "name1" "wert1" --arg "name2" "wert2" ...}} '{{. + $ARGS.named}}'`

- Gib bestimmte Schlüssel aus:

`{{cat pfad/zu/datei.json}} | jq '{{.schlüssel1, .schlüssel2, ...}}'`

- Gib bestimmte Listenelemente aus:

`{{cat pfad/zu/datei.json}} | jq '{{.[index1], .[index2], ...}}'`

- Gib alle Listenelemente/Objektschlüssel aus:

`{{cat pfad/zu/datei.json}} | jq '.[]'`

- Füge bestimmte Schlüssel hinzu/lösche bestimmte Schlüssel:

`{{cat pfad/zu/datei.json}} | jq '. {{+|-}} {{{"schlüssel1": "wert1", "schlüssel2": "wert2", ...}}}'`
