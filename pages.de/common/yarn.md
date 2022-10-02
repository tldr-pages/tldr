# yarn

> JavaScript und Node.js Paket-Manager Alternative.
> Weitere Informationen: <https://yarnpkg.com>.

- Installiere ein Modul global:

`yarn global add {{modul_name}}`

- Installiere alle in der `package.json` Datei genannten Dependencies (`install` ist optional):

`yarn install`

- Installiere ein Modul und füge es als Dependency der `package.json` Datei hinzu (`--dev` um es als Dev-Dependency zu installieren):

`yarn add {{modul_name}}@{{version}}`

- Deinstalliere ein Modul und entferne es von der `package.json` Datei:

`yarn remove {{modul_name}}`

- Erstelle interaktiv eine `package.json` Datei:

`yarn init`

- Indentifiziere ob ein Modul eine Dependency ist und liste andere Module, die von diesem abhängen:

`yarn why {{modul_name}}`
