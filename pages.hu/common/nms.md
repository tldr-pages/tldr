# nms

> Parancssoros eszköz, amely újraalkotja az 1992-es Sneakers from `stdin` című filmben látott híres adatfejtési effektust. További információ: <https://github.com/bartobri/no-more-secrets>.

- Szöveg visszafejtése egy billentyűleütés után:

`echo "{{Hello, World!}}" | nms`

- A kimenet azonnali visszafejtése, billentyűleütés megvárása nélkül:

`{{ls -la}} | nms -a`

- Egy fájl tartalmának visszafejtése, egyéni kimeneti színnel:

`cat {{path/to/file}} | nms -a -f {{blue|white|yellow|black|magenta|green|red}}`

- Törölje a képernyőt a dekódolás előtt:

`{{command}} | nms -a -c`
