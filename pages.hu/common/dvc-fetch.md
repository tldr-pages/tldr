# dvc fetch

> DVC nyomon követett fájlok és könyvtárak letöltése egy távoli tárolóból. További információ: <https://dvc.org/doc/command-reference/fetch>.

- A legfrissebb változtatások lekérése az alapértelmezett távoli upstream tárolóból (ha be van állítva):

`dvc fetch`

- Változások lekérése egy adott távoli upstream tárolóból:

`dvc fetch --remote {{remote_name}}`

- A legfrissebb módosítások lekérése egy adott célpont(ok)hoz:

`dvc fetch {{target/s}}`

- Az összes ág és címke változásainak lekérdezése:

`dvc fetch --all-branches --all-tags`

- Az összes commit változásainak lekérdezése:

`dvc fetch --all-commits`
