# pabcnetcclear

> PascalABC.NET forrásfájlok előfeldolgozása és lefordítása. További információ: <http://pascalabc.net>.

- A megadott forrásfájl lefordítása egy azonos nevű futtatható fájlba:

`pabcnetcclear {{path/to/source_file.pas}}`

- A megadott forrásfájl lefordítása a megadott nevű végrehajtható fájlba:

`pabcnetcclear /Output:{{path/to/file.exe}} {{path/to/source_file.pas}}`

- A megadott forrásfájl lefordítása azonos nevű futtatható állományba hibakeresési információkkal együtt/ anélkül:

`pabcnetcclear /Debug:{{0|1}} {{path/to/source_file.pas}}`

- Engedélyezi az egységek keresését a megadott elérési útvonalon, miközben a forrásfájlt azonos nevű végrehajtható fájlba fordítja:

`pabcnetcclear /SearchDir:{{path/to/dir}} {{path/to/source_file.pas}}`

- A megadott forrásfájl lefordítása végrehajthatóvá, szimbólumot definiálva:

`pabcnetcclear /Define:{{symbol}} {{path/to/source_file.pas}}`
