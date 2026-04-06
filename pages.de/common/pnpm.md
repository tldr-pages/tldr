# pnpm

> Schneller, speicherplatzsparender Paketmanager für Node.js.
> Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
> Weitere Informationen: <https://pnpm.io/pnpm-cli>.

- Erstelle eine `package.json` Datei interaktiv:

`pnpm init`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`pnpm {{[i|install]}}`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`pnpm add {{modul_name}}@{{version}}`

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`pnpm add {{modul_name}} {{[-D|--save-dev]}}`

- Installiere ein Package global:

`pnpm add {{modul_name}} {{[-g|--global]}}`

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`pnpm {{[rm|remove]}} {{modul_name}}`

- Gib eine Liste aller lokal installierten Packages aus:

`pnpm {{[ls|list]}}`

- Gib eine Liste aller global installierten Packages aus:

`pnpm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
