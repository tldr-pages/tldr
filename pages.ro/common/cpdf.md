# cpdf

> CLI pentru a manipula fișierele PDF existente într-o varietate de moduri.
> Mai multe informaţii: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>

- Selectați paginile 1, 2, 3 și 6 dintr-un document sursă și scrieți-le într-un document de destinație:

`cpdf {{path/to/source_document.pdf}} {{1-3,6}} -o {{path/to/destination_document.pdf}}`

- Îmbinați două documente într-unul nou:

`cpdf -merge {{path/to/source_document_one.pdf}} {{path/to/source_document_two.pdf}} -o {{path/to/destination_document.pdf}}`

- Afișați marcajele unui document:

`cpdf -list-bookmarks {{path/to/document.pdf}}`

- Împărțiți un document în bucăți de zece pagini, scriindu-le în `chunk001.pdf`, `chunk002.pdf`, etc:

`cpdf -split {{path/to/document.pdf}} -o {{path/to/chunk%%%.pdf}} -chunk {{10}}`

- Criptați un document utilizând criptarea pe 128 biți, furnizând `fred` ca parolă de proprietar și `joe` ca parolă de utilizator:

`cpdf -encrypt {{128bit}} {{fred}} {{joe}} {{path/to/source_document.pdf}} -o {{path/to/encrypted_document.pdf}}`

- Decripta un document folosind parola proprietarului `fred`:

`cpdf -decrypt {{path/to/encrypted_document.pdf}} owner={{fred}} -o {{path/to/decrypted_document.pdf}}`

- Afișați adnotările unui document:

`cpdf -list-annotations {{path/to/document.pdf}}`

- Creați un document nou dintr-un document existent cu metadate suplimentare:

`cpdf -set-metadata {{path/to/metadata.xml}} {{path/to/source_document.pdf}} -o {{path/to/destination_document.pdf}}`
