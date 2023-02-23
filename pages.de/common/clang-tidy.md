# clang-tidy

> Ein LLVM-basierter C/C++ Linter zum Finden von Stilverletzungen, Bugs und Sicherheitsmängeln durch statische Codeanalyse.
> Weitere Information: <https://clang.llvm.org/extra/clang-tidy/>.

- Führe die Standard-Checks für eine Quelldatei aus:

`clang-tidy {{pfad/zu/quelldatei.cpp}}`

- Prüfe nur ob eine Datei den `cppcoreguidelines` Checks entspricht:

`clang-tidy {{pfad/zu/quelldatei.cpp}} -checks={{-*,cppcoreguidelines-*}}`

- Liste alle verfügbaren Checks auf:

`clang-tidy -checks={{*}} -list-checks`

- Lege defines und includes als Kompilierungsoptionen fest (nach `--`):

`clang-tidy {{pfad/zu/quelldatei.cpp}} -- -I{{mein_projekt/include}} -D{{definitions}}`
