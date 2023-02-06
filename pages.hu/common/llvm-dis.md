# llvm-dis

> LLVM bitkódfájlokat alakít át ember által olvasható LLVM Intermediate Representation (IR) formátumra. További információ: <https://www.llvm.org/docs/CommandGuide/llvm-dis.html>.

- Egy bitkódfájlt LLVM IR-ként konvertál, és az eredményt a `stdout` címre írja:

`llvm-dis {{path/to/input.bc}} -o -`

- Egy bitkódfájl átalakítása LLVM IR-fájllá ugyanazzal a fájlnévvel:

`llvm-dis {{path/to/file.bc}}`

- Egy bitkódfájl LLVM IR-é konvertálása, az eredményt a megadott fájlba írva:

`llvm-dis {{path/to/input.bc}} -o {{path/to/output.ll}}`
