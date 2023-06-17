# adscript

> Compiler voor Adscript-bestanden.
> Meer informatie: <https://github.com/Amplus2/Adscript>.

- Compileer een bestand naar een objectbestand:

`adscript --output {{pad/naar/bestand.o}} {{pad/naar/input_file.adscript}}`

- Compileer en koppel een bestand aan een zelfstandig uitvoerbaar bestand:

`adscript --executable --output {{pad/naar/bestand}} {{pad/naar/invoer_bestand.adscript}}`

- Compileer een bestand naar LLVM IR in plaats van native machinecode:

`adscript --llvm-ir --output {{pad/naar/bestand.ll}} {{pad/naar/invoer_bestand.adscript}}`

- Cross-compileer een bestand naar een objectbestand voor een buitenlandse CPU-architectuur of besturingssysteem:

`adscript --target-triple {{i386-linux-elf}} --output {{pad/naar/bestand.o}} {{pad/naar/invoer_bestand.adscript}}`
