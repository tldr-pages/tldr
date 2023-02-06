# rofi

> Alkalmazásindító és ablakváltó. További információ: <https://github.com/davatorium/rofi>.

- Az alkalmazások listájának megjelenítése:

`rofi -show drun`

- Az összes parancs listájának megjelenítése:

`rofi -show run`

- Váltás az ablakok között:

`rofi -show window`

- Az elemek listáját a `stdin` címre továbbítja, és a kiválasztott elemet kinyomtatja a `stdout` címre:

`printf "{{Choice1\nChoice2\nChoice3}}" | rofi -dmenu`
