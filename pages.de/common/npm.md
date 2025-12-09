# npm

> Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
> Weitere Informationen: <https://docs.npmjs.com/cli/npm>.

- Erstelle eine `package.json` Datei interaktiv:

`npm init`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`npm install`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`npm install {{package_name}}@{{version}}`

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`npm install {{package_name}} {{[-D|--save-dev]}}`

- Installiere ein Package global:

`npm install {{[-g|--global]}} {{package_name}}`

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`npm uninstall {{package_name}}`

- Gib eine Liste aller lokal installierten Packages aus:

`npm list`

- Gib eine Liste aller global installierten Packages aus:

`npm list {{[-g|--global]}} --depth {{0}}`
