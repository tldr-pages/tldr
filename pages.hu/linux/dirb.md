# dirb

> A HTTP-alapú webkiszolgálók könyvtárak és fájlok keresése. További információ: <http://dirb.sourceforge.net>.

- Webkiszolgáló vizsgálata az alapértelmezett szólista használatával:

`dirb {{https://example.org}}`

- Webkiszolgáló vizsgálata egyéni szólista használatával:

`dirb {{https://example.org}} {{path/to/wordlist.txt}}`

- Webkiszolgáló nem rekurzív szkennelése:

`dirb {{https://example.org}} -r`

- Webkiszolgáló átvizsgálása megadott felhasználói ügynök és cookie használatával HTTP-kérések esetén:

`dirb {{https://example.org}} -a {{user_agent_string}} -c {{cookie_string}}`
