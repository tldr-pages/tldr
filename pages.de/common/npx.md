# npx

> Führt Binärdateien von `npm` Paketen aus.
> Weitere Informationen: <https://github.com/npm/npx>.

- Führe die Binärdatei eines bestimmten npm Pakets aus:

`npx {{modulname}} {{befehlsargumente}}`

- Übergib den konkreten Namen, falls das Paket mehrere Binärdateien besitzt:

`npx --package {{paketname}} {{modulname}}`

- Führe einen Befehl aus, wenn er im aktuellen Verzeichnis oder in `node_modules/.bin` gefunden wird:

`npx --no-install {{befehl}} {{befehlsargumente}}`

- Führe die Binärdatei eines bestimmten npm Moduls aus und unterdrücke jede Ausgabe von `npx` selbst:

`npx --quiet {{modulname}} {{befehlsargumente}}`

- Zeige eine Hilfe an:

`npx --help`
