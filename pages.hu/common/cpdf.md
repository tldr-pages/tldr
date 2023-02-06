# cpdf

> CLI a meglévő PDF-fájlok különböző módokon történő manipulálásához. További információ: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- Válassza ki az 1., 2., 3. és 6. oldalt egy forrásdokumentumból, és írja azokat egy céldokumentumba:

`cpdf {{path/to/source_document.pdf}} {{1-3,6}} -o {{path/to/destination_document.pdf}}`

- Két dokumentum összevonása egy új dokumentumba:

`cpdf -merge {{path/to/source_document_one.pdf}} {{path/to/source_document_two.pdf}} -o {{path/to/destination_document.pdf}}`

- Egy dokumentum könyvjelzőinek megjelenítése:

`cpdf -list-bookmarks {{path/to/document.pdf}}`

- Egy dokumentum felosztása tízoldalas részekre, és ezek kiírása a `chunk001.pdf`, `chunk002.pdf`, stb. címre:

`cpdf -split {{path/to/document.pdf}} -o {{path/to/chunk%%%.pdf}} -chunk {{10}}`

- Egy dokumentum titkosítása 128 bites titkosítással, megadva a `fred` címet tulajdonos jelszóként és a `joe` címet felhasználó jelszóként:

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{path/to/source_document.pdf}} -o {{path/to/encrypted_document.pdf}}`

- A dokumentum visszafejtése a tulajdonos jelszavával `fred`:

`cpdf -decrypt {{path/to/encrypted_document.pdf}} owner={{fred}} -o {{path/to/decrypted_document.pdf}}`

- Egy dokumentum megjegyzéseinek megjelenítése:

`cpdf -list-annotations {{path/to/document.pdf}}`

- Új dokumentum létrehozása egy meglévő dokumentumból további metaadatokkal:

`cpdf -set-metadata {{path/to/metadata.xml}} {{path/to/source_document.pdf}} -o {{path/to/destination_document.pdf}}`
