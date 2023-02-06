# adscript

> Adscript fájlok fordítója. További információ: <https://github.com/Amplus2/Adscript>.

- Egy fájl objektumfájllá történő fordítása:

`adscript --output {{path/to/file.o}} {{path/to/input_file.adscript}}`

- Egy fájl lefordítása és összekapcsolása önálló futtatható fájlba:

`adscript --executable --output {{path/to/file}} {{path/to/input_file.adscript}}`

- Egy fájl lefordítása LLVM IR-be natív gépi kód helyett:

`adscript --llvm-ir --output {{path/to/file.ll}} {{path/to/input_file.adscript}}`

- Egy fájl keresztkompilálása objektumfájlba egy idegen CPU-architektúrához vagy operációs rendszerhez:

`adscript --target-triple {{i386-linux-elf}} --output {{path/to/file.o}} {{path/to/input_file.adscript}}`
