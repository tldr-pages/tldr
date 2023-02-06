# popd

> A pushd shell beépített parancsával a könyvtárak veremére helyezett könyvtár eltávolítása. Lásd még: `pushd` könyvtárak veremre helyezéséhez és `dirs` könyvtárak veremének tartalmának megjelenítéséhez. További információ: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Távolítsa el a legfelső könyvtárat a veremről, és cd-vel lépjen oda:

`popd`

- Az N-edik könyvtár eltávolítása (nullától balra kezdődően a `dirs` kiírt listából):

`popd +N`

- Az N-edik könyvtár eltávolítása (nullától kezdve jobbra a `dirs` segítségével kinyomtatott listából):

`popd -N`
