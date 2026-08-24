# adscript

> Compilatore per file Adscript.
> Maggiori informazioni: <https://github.com/Amplus2/Adscript>.

- Compila un file in un file oggetto:

`adscript --output {{percorso/del/file.o}} {{percorso/del/file_input.adscript}}`

- Compila e linka un file in un eseguibile standalone:

`adscript --executable --output {{percorso/del/file}} {{percorso/del/file_input.adscript}}`

- Compila un file in LLVM IR invece che in codice macchina nativo:

`adscript --llvm-ir --output {{percorso/del/file.ll}} {{percorso/del/file_input.adscript}}`

- Cross-compila un file in un file oggetto per un'architettura CPU o sistema operativo straniero:

`adscript --target-triple {{i386-linux-elf}} --output {{percorso/del/file.o}} {{percorso/del/file_input.adscript}}`
