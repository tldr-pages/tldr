# llvm-config

> Az LLVM-et használó programok fordításához szükséges különböző konfigurációs információk lekérdezése. Általában a build rendszerekből hívják, például a Makefiles vagy a configure szkriptek. További információ: <https://llvm.org/docs/CommandGuide/llvm-config.html>.

- LLVM alapú program fordítása és linkelése:

`clang++ $(llvm-config --cxxflags --ldflags --libs) --output {{path/to/output_executable}} {{path/to/source.cc}}`

- Az LLVM telepítés `PREFIX` oldalának kinyomtatása:

`llvm-config --prefix`

- Az LLVM build által támogatott összes célpont kinyomtatása:

`llvm-config --targets-built`
