# chromium

> Nyílt forráskódú webböngésző, amelyet alapvetően a Google fejleszt és tart fenn. További információ: <https://www.chromium.org/developers/how-tos/run-chromium-with-flags/>.

- Egy adott URL vagy fájl megnyitása:

`chromium {{https://example.com|path/to/file.html}}`

- Megnyitás inkognitó módban:

`chromium --incognito {{example.com}}`

- Megnyitás új ablakban:

`chromium --new-window {{example.com}}`

- Megnyitás alkalmazási módban (eszköztárak, URL-sáv, gombok stb. nélkül):

`chromium --app={{https://example.com}}`

- Proxy-kiszolgáló használata:

`chromium --proxy-server="{{socks5://hostname:66}}" {{example.com}}`

- Megnyitás egyéni profilkönyvtárral:

`chromium --user-data-dir={{path/to/directory}}`

- Megnyitás CORS-érvényesítés nélkül (hasznos egy API teszteléséhez):

`chromium --user-data-dir={{path/to/directory}} --disable-web-security`

- Megnyitás DevTools ablakkal minden egyes megnyitott laphoz:

`chromium --auto-open-devtools-for-tabs`
