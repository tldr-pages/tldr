# qutebrowser

> Egy billentyűzetvezérelt, vim-szerű böngésző, amely PyQt5-re épül. További információ: <https://qutebrowser.org/>.

- A qutebrowser megnyitása egy megadott tárolási könyvtárral:

`qutebrowser --basedir {{path/to/directory}}`

- Megnyit egy qutebrowser példányt ideiglenes beállításokkal:

`qutebrowser --set {{content.geolocation}} {{true|false}}`

- Egy qutebrowser-példány megnevezett munkamenetének visszaállítása:

`qutebrowser --restore {{session_name}}`

- A qutebrowser elindítása, az összes URL megnyitása a megadott módszerrel:

`qutebrowser --target {{auto|tab|tab-bg|tab-silent|tab-bg-silent|window|private-window}}`

- A qutebrowser megnyitása egy ideiglenes alapkönyvtárral és a naplók JSON-ként történő kinyomtatása a `stdout` címre:

`qutebrowser --temp-basedir --json-logging`
