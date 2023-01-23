# scan-build

> Parancssori segédprogram statikus elemző futtatására egy kódbázison a rendszeres építés részeként. További információ: <https://clang-analyzer.llvm.org/scan-build.html>.

- Az aktuális könyvtárban lévő projekt építése és elemzése:

`scan-build {{make}}`

- Futtasson egy parancsot, és adja át az összes későbbi opciót:

`scan-build {{command}} {{command_arguments}}`

- Súgó megjelenítése:

`scan-build`
