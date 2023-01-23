# strings

> Nyomtatható karakterláncok keresése egy objektumfájlban vagy binárisban. További információ: <https://manned.org/strings>.

- Az összes karakterlánc kiírása egy binárisban:

`strings {{path/to/file}}`

- Az eredmények korlátozása a legalább karakter *hosszúságú* karakterláncokra:

`strings -n {{length}} {{path/to/file}}`

- Minden eredményt előtagozzon a fájlon belüli eltolással:

`strings -t d {{path/to/file}}`

- Minden eredményt a fájlon belüli eltolással előtagolhat hexadecimálisan:

`strings -t x {{path/to/file}}`
