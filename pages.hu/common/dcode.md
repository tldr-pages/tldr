# dcode

> A karakterláncok rekurzív felismerése és dekódolása, támogatja a hexa, decimális, bináris, base64, URL, FromChar kódolásokat, Caesar-kódolásokat, valamint az MD5, SHA1 és SHA2 hash-eket. Figyelem: az MD5, SHA1 és SHA2 hash-kereséshez harmadik féltől származó webes szolgáltatásokat használ. Érzékeny adatok esetén használja a `-s` címet, hogy elkerülje ezeket a szolgáltatásokat. További információ: <https://github.com/s0md3v/Decodify>.

- Egy karakterlánc rekurzív felismerése és dekódolása:

`dcode "{{NjM3YTQyNzQ1YTQ0NGUzMg==}}"`

- Egy karakterlánc elforgatása a megadott eltolással:

`dcode -rot {{11}} "{{spwwz hzcwo}}"`

- Egy karakterlánc elforgatása mind a 26 lehetséges eltolással:

`dcode -rot {{all}} "{{bpgkta xh qtiitg iwpc sr}}"`

- Egy karakterlánc megfordítása:

`dcode -rev "{{hello world}}"`
