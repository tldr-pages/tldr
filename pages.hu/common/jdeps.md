# jdeps

> Java osztályfüggőség-elemző. További információ: <https://docs.oracle.com/en/java/javase/18/docs/specs/man/jdeps.html>.

- A `.jar` vagy a `.class` fájl függőségeinek elemzése:

`jdeps {{path/to/filename.class}}`

- Egy adott `.jar` fájl összes függőségének összefoglalóját nyomtatja ki:

`jdeps {{path/to/filename.jar}} -summary`

- Egy `.jar` fájl összes osztályszintű függőségének kinyomtatása:

`jdeps {{path/to/filename.jar}} -verbose`

- Az elemzés eredményeinek kiadása egy DOT fájlban egy adott könyvtárba:

`jdeps {{path/to/filename.jar}} -dotoutput {{path/to/directory}}`

- Súgó megjelenítése:

`jdeps --help`
