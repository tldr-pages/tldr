# hg pull

> A megadott tárolóból a helyi tárolóba való áthúzás. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#pull>.

- Húzás az "alapértelmezett" forrás elérési útvonalról:

`hg pull`

- Húzás egy megadott forrásadattárból:

`hg pull {{path/to/source_repository}}`

- A helyi adattár frissítése a távoli fejlécre:

`hg pull --update`

- Húzza a változtatásokat akkor is, ha a távoli tároló nem kapcsolódik:

`hg pull --force`

- Adjon meg egy adott revíziós módosításkészletet, ameddig fel lehet húzni:

`hg pull --rev {{revision}}`

- Egy adott ág megadása a húzáshoz:

`hg pull --branch {{branch}}`

- Egy adott könyvjelző megadása a húzáshoz:

`hg pull --bookmark {{bookmark}}`
