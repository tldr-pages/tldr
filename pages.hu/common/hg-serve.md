# hg serve

> Önálló Mercurial webszerver indítása a tárolók böngészéséhez. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#serve>.

- Indítson el egy webkiszolgáló példányt:

`hg serve`

- Webkiszolgáló-példány indítása a megadott porton:

`hg serve --port {{port}}`

- Webkiszolgáló példány indítása a megadott figyelő címen:

`hg serve --address {{address}}`

- Webkiszolgáló példány indítása egy adott azonosítóval:

`hg serve --name {{name}}`

- Webkiszolgáló-példány indítása a megadott téma használatával (lásd a sablonok könyvtárát):

`hg serve --style {{style}}`

- Webkiszolgáló példány indítása a megadott SSL-tanúsítványcsomag használatával:

`hg serve --certificate {{path/to/certificate}}`
