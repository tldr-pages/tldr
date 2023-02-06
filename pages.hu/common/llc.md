# llc

> LLVM Intermediate Representation vagy bitkódot fordít célspecifikus assembly nyelvre. További információ: <https://www.llvm.org/docs/CommandGuide/llc.html>.

- Egy bitkód vagy IR fájl lefordítása egy azonos alapnevű assembly fájlba:

`llc {{path/to/file.ll}}`

- Engedélyezze az összes optimalizálást:

`llc -O3 {{path/to/input.ll}}`

- Assembly kimenete egy adott fájlba:

`llc --output {{path/to/output.s}}`

- Teljesen áthelyezhető, pozíciófüggetlen kód kiadása:

`llc -relocation-model=pic {{path/to/input.ll}}`
