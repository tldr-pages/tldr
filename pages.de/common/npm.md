# npm

> Ein Kommandozeilenwerkzeug für die Verwaltung von Javascript und Node.js Paketen (Packages)
> Mehr Informationen und eine Liste aller verfügbaren Packages <https://www.npmjs.com/>

- Interaktives Erstellen einer `package.json` Datei:

`npm init`

- Installieren aller in der `package.json` Datei gelisteten Packages:

`npm install`

- Installieren eines Packages. Das Package wird automatisch der `package.json` Datei hinzugefügt. Der zweite Teil ist optional und wird nur verwendet, wenn eine spezifische Version installiert werden sollte:

`npm install {{package_name}}@{{version}}`

- Globales Installieren eines Packages. Auch hier kann, wie oben, bei der Installation eine Version definiert werden.

`npm install -g {{package_name}}`

- Deinstallieren eines Packages und automatisches Entfernen aus der `package.json` Datei:

`npm uninstall {{package_name}}`

- Ausgeben einer Liste, aller lokal installierten Packages:

`npm list`

- Ausgeben einer Liste, aller global installierten Packages.

`npm list -g --depth={{0}}`
