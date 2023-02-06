# rtmpdump

> Az RTMP protokollon keresztül streamelt médiatartalmak dumpolására szolgáló eszköz. További információ: <http://rtmpdump.mplayerhq.hu/>.

- Fájl letöltése:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} -o {{file.ext}}`

- Egy fájl letöltése egy Flash-lejátszóból:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --swfVfy {{http://example.com/player}} --flashVer "{{LNX 10,0,32,18}}" -o {{file.ext}}`

- Adja meg a kapcsolati paramétereket, ha azok nem megfelelően kerülnek felismerésre:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --app {{app_name}} --playpath {{path/to/video}} -o {{file.ext}}`

- Fájl letöltése olyan kiszolgálóról, amely hivatkozót igényel:

`rtmpdump --rtmp {{rtmp://example.com/path/to/video}} --pageUrl {{http://example.com/webpage}} -o {{file.ext}}`
