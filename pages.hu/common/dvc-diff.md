# dvc diff

> A DVC által nyomon követett fájlok és könyvtárak változásainak megjelenítése. További információ: <https://dvc.org/doc/command-reference/diff>.

- Különböző Git commitokból, címkékből és ágakból származó DVC nyomon követett fájlok összehasonlítása az aktuális munkaterülettel:

`dvc diff {{commit_hash/tag/branch}}`

- A DVC követett fájlokban lévő változások összehasonlítása 1 Git commitból egy másikba:

`dvc diff {{revision_b}} {{revision_a}}`

- DVC nyomon követett fájlok összehasonlítása, a legutóbbi hash-jukkal együtt:

`dvc diff --show-hash {{commit}}`

- DVC nyomon követett fájlok összehasonlítása, a kimenet JSON-ként történő megjelenítésével:

`dvc diff --show-json --show-hash {{commit}}`

- DVC nyomon követett fájlok összehasonlítása, a kimenet Markdown-ként történő megjelenítésével:

`dvc diff --show-md --show-hash {{commit}}`
