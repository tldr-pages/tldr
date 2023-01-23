# mutagen

> Valós idejű fájlszinkronizáló és hálózati továbbító eszköz. További információ: <https://mutagen.io>.

- Szinkronizálási munkamenet indítása egy helyi könyvtár és egy távoli állomás között:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} {{user}}@{{host}}:{{/path/to/remote/directory/}}`

- Szinkronizálási munkamenet indítása egy helyi könyvtár és egy Docker konténer között:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} docker://{{user}}@{{container_name}}{{/path/to/remote/directory/}}`

- Folyamatban lévő munkamenet leállítása:

`mutagen sync terminate {{session_name}}`

- Projekt indítása:

`mutagen project start`

- Egy projekt leállítása:

`mutagen project terminate`

- Az aktuális projekt futó munkameneteinek listázása:

`mutagen project list`
