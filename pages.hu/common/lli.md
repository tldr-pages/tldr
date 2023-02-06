# lli

> Programok közvetlen futtatása LLVM bitkódból. További információ: <https://www.llvm.org/docs/CommandGuide/lli.html>.

- Bitkód vagy IR fájl végrehajtása:

`lli {{path/to/file.ll}}`

- Végrehajtás parancssori argumentumokkal:

`lli {{path/to/file.ll}} {{argument1 argument2 ...}}`

- Minden optimalizálás engedélyezése:

`lli -O3 {{path/to/file.ll}}`

- Dinamikus könyvtár betöltése linkelés előtt:

`lli --dlopen={{path/to/library.dll}} {{path/to/file.ll}}`
