# adscript

> Compiler für Adscript Dateien.
> Weitere Informationen: <https://github.com/Amplus2/Adscript>.

- Kompiliere eine Datei zu einer Objektdatei:

`adscript --output {{pfad/zu/datei.o}} {{pfad/zu/quelldatei.adscript}}`

- Kompiliere eine Datei zu einer ausführbaren Binärdatei:

`adscript --executable --output {{pfad/zu/datei}} {{pfad/zu/quelldatei.adscript}}`

- Kompiliere eine Datei zu LLVM IR anstelle von nativem Maschinencode:

`adscript --llvm-ir --output {{pfad/zu/datei.ll}} {{pfad/zu/quelldatei.adscript}}`

- Cross-kompiliere eine Datei zu einer Objektdatei für eine fremde CPU Architektur oder ein fremdes Betriebssystem:

`adscript --target-triple {{i386-linux-elf}} --output {{pfad/zu/datei.o}} {{pfad/zu/quelldatei.adscript}}`
