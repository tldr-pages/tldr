# git archive

> Fájlarchívum létrehozása egy megnevezett fából. További információ: <https://git-scm.com/docs/git-archive>.

- Tar-archívum létrehozása az aktuális HEAD tartalmából, és kiírása a standard kimenetre:

`git archive --verbose HEAD`

- Zip-archívum létrehozása az aktuális HEAD tartalmából és kinyomtatása a standard kimenetre:

`git archive --verbose --format=zip HEAD`

- Ugyanaz, mint fent, de a zip-archívumot írja ki a fájlba:

`git archive --verbose --output={{path/to/file.zip}} HEAD`

- Tar-archívum létrehozása egy adott ág legutóbbi commitjának tartalmából:

`git archive --output={{path/to/file.tar}} {{branch_name}}`

- Tar-archívum létrehozása egy adott könyvtár tartalmából:

`git archive --output={{path/to/file.tar}} HEAD:{{path/to/directory}}`

- Minden egyes fájlhoz egy elérési útvonal előtagja, hogy egy adott könyvtáron belül archiválja azt:

`git archive --output={{path/to/file.tar}} --prefix={{path/to/prepend}}/ HEAD`
