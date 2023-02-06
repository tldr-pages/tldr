# opt

> Olyan eszköz, amely LLVM forrásfájlokat vesz és meghatározott optimalizálásokat és/vagy elemzéseket futtat rajtuk. További információ: <https://llvm.org/docs/CommandGuide/opt.html>.

- Optimalizálás vagy elemzés futtatása egy bitkódfájlon:

`opt -{{passname}} {{path/to/file.bc}} -S -o {{file_opt.bc}}`

- Egy függvény vezérlésáramlási grafikonjának kiadása egy `.dot` fájlba:

`opt {{-dot-cfg}} -S {{path/to/file.bc}} -disable-output`

- A program optimalizálása a 2. szinten, és az eredmény kiadása egy másik fájlba:

`opt -O2 {{path/to/file.bc}} -S -o {{path/to/output_file.bc}}`
