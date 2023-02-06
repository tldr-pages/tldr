# kotlinc

> Kotlin fordító. További információ: <https://kotlinlang.org/docs/command-line.html>.

- Indítson el egy REPL-t (interaktív shell):

`kotlinc`

- Kotlin fájl fordítása:

`kotlinc {{path/to/file.kt}}`

- Több Kotlin fájl fordítása:

`kotlinc {{path/to/file1.kt path/to/file2.kt ...}}`

- Egy adott Kotlin Script fájl végrehajtása:

`kotlinc -script {{path/to/file.kts}}`

- Kotlin fájl fordítása egy önálló jar fájlba, amely tartalmazza a Kotlin futásidejű könyvtárat:

`kotlinc {{path/to/file.kt}} -include-runtime -d {{path/to/file.jar}}`
