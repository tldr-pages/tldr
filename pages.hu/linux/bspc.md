# bspc

> Egy eszköz a `bspwm` ellenőrzésére. További információ: <https://github.com/baskerville/bspwm>.

- Két virtuális asztal meghatározása:

`bspc monitor --reset-desktops {{1}} {{2}}`

- Fókuszálja az adott asztalt:

`bspc desktop --focus {{number}}`

- A kiválasztott csomópontban gyökerező ablakok bezárása:

`bspc node --close`

- A kijelölt csomópont átküldése az adott asztali gépre:

`bspc node --to-desktop {{number}}`

- Teljes képernyős mód átkapcsolása a kiválasztott csomóponthoz:

`bspc node --state ~fullscreen`
