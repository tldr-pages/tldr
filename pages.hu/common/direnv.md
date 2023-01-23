# direnv

> Shell kiterjesztés a környezeti változók betöltésére és eltávolítására az aktuális könyvtár függvényében. További információ: <https://github.com/direnv/direnv>.

- Adjon direnv engedélyt az aktuális könyvtárban található `.envrc` betöltésére:

`direnv allow {{.}}`

- Visszavonja a jogosultságot az aktuális könyvtárban található `.envrc` betöltésére:

`direnv deny {{.}}`

- Szerkessze a `.envrc` fájlt az alapértelmezett szövegszerkesztővel, és kilépéskor töltse be újra a környezetet:

`direnv edit {{.}}`

- A környezet újratöltésének kiváltása:

`direnv reload`

- Néhány hibakeresési állapotinformáció kiírása:

`direnv status`
