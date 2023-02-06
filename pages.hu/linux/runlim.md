# runlim

> A proc fájlrendszer segítségével Linuxon egy program és gyermekfolyamatai idő- és memóriahasználatának mintavételezésére és korlátozására szolgáló eszköz. További információ: <http://fmv.jku.at/runlim>.

- Kiírja egy parancs idejét és memóriahasználatát:

`runlim {{command}} {{command_arguments}}`

- Statisztikák naplózása egy fájlba a `stdout` helyett:

`runlim --output-file={{path/to/file}} {{command}} {{command_arguments}}`

- Az idő korlátozása egy felső határértékre (másodpercben):

`runlim --time-limit={{number}} {{command}} {{command_arguments}}`

- A valós idő korlátozása felső korlátra (másodpercben):

`runlim --real-time-limit={{number}} {{command}} {{command_arguments}}`

- A tárhely felső határértékre korlátozása (MB-ban):

`runlim --space-limit={{number}} {{command}} {{command_arguments}}`
