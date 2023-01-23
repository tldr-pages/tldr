# http-prompt

> Interaktív parancssori HTTP-kliens automatikus kitöltéssel és szintaxis-kiemeléssel. További információ: <https://github.com/httpie/http-prompt>.

- A http://localhost:8000 vagy az előző munkamenet alapértelmezett URL-címét megcélzó munkamenet indítása:

`http-prompt`

- Munkamenet indítása egy adott URL-címmel:

`http-prompt {{http://example.com}}`

- Munkamenet indítása néhány kezdeti beállítással:

`http-prompt {{localhost:8000/api}} --auth {{username:password}}`
