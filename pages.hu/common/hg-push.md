# hg push

> A helyi adattárból a változtatások áthelyezése egy megadott célállomásra. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#push>.

- Változások átvitele az "alapértelmezett" távoli elérési útvonalra:

`hg push`

- Változások átirányítása egy megadott távoli tárolóhelyre:

`hg push {{path/to/destination_repository}}`

- Új ág áthelyezése, ha nem létezik (alapértelmezés szerint kikapcsolva):

`hg push --new-branch`

- Egy adott revíziós módosításkészlet megadása a push-hoz:

`hg push --rev {{revision}}`

- Egy adott ág megadása a push-hoz:

`hg push --branch {{branch}}`

- Egy adott könyvjelző megadása:

`hg push --bookmark {{bookmark}}`
