# dvc checkout

> Adatfájlok és könyvtárak lekérdezése a gyorsítótárból. További információ: <https://dvc.org/doc/command-reference/checkout>.

- Az összes célfájl és könyvtár legújabb verziójának ellenőrzése:

`dvc checkout`

- Egy megadott célterület legfrissebb verziójának ellenőrzése:

`dvc checkout {{target}}`

- Egy célpont egy adott verziójának ellenőrzése egy másik Git commit/tag/ágból:

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`
