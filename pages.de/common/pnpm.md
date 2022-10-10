# pnpm

> Schneller, speicherplatzsparender Paketmanager für Node.js.
> Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
> Weitere Informationen: <https://pnpm.io>.

- Erstelle eine `package.json` Datei interaktiv:

`pnpm init`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`pnpm install`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`pnpm add {{modul_name}}@{{version}}`

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`pnpm add -D {{modul_name}}`

- Installiere ein Package global:

`pnpm add -g {{modul_name}}`

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`pnpm remove {{modul_name}}`

- Gib eine Liste aller lokal installierten Packages aus:

`pnpm list`

- Gib eine Liste aller global installierten Packages aus:

`pnpm list -g --depth={{0}}`
