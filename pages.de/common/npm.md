# npm

> Ein Kommandozeilenwerkzeug für die Verwaltung von JavaScript und Node.js Paketen (Packages).
> Weitere Informationen: <https://docs.npmjs.com/cli/npm/>.

- Erstelle eine `package.json` Datei interaktiv:

`npm init {{[-y|--yes]}}`

- Installiere alle in der `package.json` Datei gelisteten Abhängigkeiten:

`npm {{[i|install]}}`

- Installiere eine spezifische Version eines Packages und füge es automatisch der `package.json` Datei hinzu:

`npm {{[i|install]}} {{package_name}}@{{version}}`

- Installiere ein Package und füge es als Entwicklungs-Abhängigkeit der `package.json` Datei hinzu:

`npm {{[i|install]}} {{package_name}} {{[-D|--save-dev]}}`

- Installiere ein Package global:

`npm {{[i|install]}} {{package_name}} {{[-g|--global]}}`

- Deinstalliere ein Package und entferne es automatisch aus der `package.json` Datei:

`npm {{[r|uninstall]}} {{package_name}}`

- Gib eine Liste aller lokal installierten Packages aus:

`npm {{[ls|list]}}`

- Gib eine Liste aller global installierten Packages aus:

`npm {{[ls|list]}} {{[-g|--global]}} --depth {{0}}`
