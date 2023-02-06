# conky

> Könnyű rendszermonitor az X-hez. További információ: <https://github.com/brndnmtthws/conky>.

- Indítás alapértelmezett, beépített konfigurációval:

`conky`

- Új alapértelmezett konfiguráció létrehozása:

`conky -C > ~/.conkyrc`

- A Conky elindítása egy adott konfigfájllal:

`conky -c {{path/to/config}}`

- Indítás a háttérben (daemonizálás):

`conky -d`

- A Conky igazítása az asztalon:

`conky -a {{top|bottom|middle}}_{{left|right|middle}}`

- Indításkor 5 másodperc szünet indítás előtt:

`conky -p {{5}}`
