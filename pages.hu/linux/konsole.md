# konsole

> A KDE terminál emulátor. További információ: <https://docs.kde.org/trunk5/en/konsole/konsole/command-line-options.html>.

- Nyissa meg a terminált egy adott könyvtárban:

`konsole --workdir {{path/to/directory}}`

- \[e\]xecute egy adott parancsot, és ne zárja be az ablakot a kilépés után:

`konsole --noclose -e "{{command}}"`

- Új lap megnyitása:

`konsole --new-tab`

- A terminál megnyitása a háttérben és előtérbe hozása a `Ctrl+Shift+F12` megnyomásakor:

`konsole --background-mode`
