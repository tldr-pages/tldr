# clang-tidy

> Egy LLVM-alapú C/C++ linter, amely statikus elemzéssel keres stílustöréseket, hibákat és biztonsági hiányosságokat. További információ: <https://clang.llvm.org/extra/clang-tidy/>.

- Alapértelmezett ellenőrzések futtatása egy forrásfájlon:

`clang-tidy {{path/to/file.cpp}}`

- A `cppcoreguidelines` ellenőrzéseken kívül semmilyen más ellenőrzést ne futtasson egy fájlon:

`clang-tidy {{path/to/file.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- Az összes elérhető ellenőrzés listázása:

`clang-tidy -checks={{*}} -list-checks`

- Defines és includes megadása fordítási opcióként (a `--` után):

`clang-tidy {{path/to/file.cpp}} -- -I{{my_project/include}} -D{{definitions}}`
