# sic

> Egyszerű IRC kliens. A suckless tools része. További információ: <https://tools.suckless.org/sic/>.

- Csatlakozzon az alapértelmezett hosthoz (irc.ofct.net) a `$USER` környezeti változóban beállított becenévvel:

`sic`

- Csatlakozás egy adott állomáshoz, egy adott becenévvel:

`sic -h {{host}} -n {{nickname}}`

- Csatlakozás egy adott állomáshoz egy adott becenév és jelszó használatával:

`sic -h {{host}} -n {{nickname}} -k {{password}}`

- Csatlakozás egy csatornához:

`:j #{{channel}}<Enter>`

- Üzenet küldése egy csatornának vagy felhasználónak:

`:m #{{channel|user}}<Enter>`

- Alapértelmezett csatorna vagy felhasználó beállítása:

`:s #{{channel|user}}<Enter>`
