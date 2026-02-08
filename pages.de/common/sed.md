# sed

> Bearbeite Text auf eine skriptfähige Weise.
> Siehe auch: `awk`, `ed`.
> Weitere Informationen: <https://manned.org/sed.1posix>.

- Ersetze alle Vorkommen von `apple` (einfaches `regex`) durch `mango` (einfaches `regex`) in allen Eingabezeilen und gib das Ergebnis auf `stdout` aus:

`{{befehl}} | sed 's/apple/mango/g'`

- Führe eine bestimmte Skript[f] datei aus und gib das Ergebnis auf `stdout` aus:

`{{befehl}} | sed -f {{pfad/zu/skript.sed}}`

- Gib nur die erste Zeile auf `stdout` aus:

`{{befehl}} | sed -n '1p'`
