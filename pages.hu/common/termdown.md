# termdown

> Visszaszámláló és stopper a parancssorban. További információ: <https://github.com/trehn/termdown>.

- Stopperóra indítása:

`termdown`

- Indítson el egy 1 perces és 30 másodperces visszaszámlálást:

`termdown {{1m30s}}`

- 1 perc 30 másodperces visszaszámlálás indítása a terminál villogásával a végén:

`termdown {{1m30s}} --blink`

- A visszaszámlálás felett cím megjelenítése:

`termdown {{1m30s}} --title "{{Interesting title}}"`

- Jelenlegi idő megjelenítése:

`termdown --time`
