# virtualboxvm

> A VirtualBox virtuális gépeket kezelő CLI. További információ: <https://www.virtualbox.org>.

- Indítson el egy virtuális gépet:

`virtualboxvm --startvm {{name|uuid}}`

- Virtuális gép indítása teljes képernyős módban:

`virtualboxvm --startvm {{name|uuid}} --fullscreen`

- A megadott DVD-képfájl csatlakoztatása:

`virtualboxvm --startvm {{name|uuid}} --dvd {{path/to/image_file}}`

- Parancssori ablak megjelenítése hibakeresési információkkal:

`virtualboxvm --startvm {{name|uuid}} --debug-command-line`

- Virtuális gép indítása szüneteltetett állapotban:

`virtualboxvm --startvm {{name|uuid}} --start-paused`
