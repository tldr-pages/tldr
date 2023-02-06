# xargs

> Parancs végrehajtása egy másik parancsból, fájlból stb. érkező piped argumentumokkal. A bemenetet egyetlen szövegtömbként kezeli, és szóközök, tabulátorok, újsorok és fájlvégek esetén különálló darabokra bontja. További információ: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/xargs.html>.

- Parancs futtatása a bemeneti adatokat argumentumként használva:

`{{arguments_source}} | xargs {{command}}`

- Több láncolt parancs futtatása a bemeneti adatokon:

`{{arguments_source}} | xargs sh -c "{{command1}} && {{command2}} | {{command3}}"`

- Törölje az összes `.backup` kiterjesztésű fájlt (`-print0` null karaktert használ a fájlnevek felosztására, a `-0` pedig elválasztóként):

`find . -name {{'*.backup'}} -print0 | xargs -0 rm -v`

- Futtassa a parancsot egyszer minden egyes bemeneti sorra, a helyőrző (itt `_`) minden előfordulását a bemeneti sorral helyettesítve:

`{{arguments_source}} | xargs -I _ {{command}} _ {{optional_extra_arguments}}`

- Egyszerre legfeljebb `max-procs` folyamatok párhuzamos futtatása; az alapértelmezett érték 1. Ha a `max-procs` értéke 0, a xargs egyszerre annyi folyamatot futtat, amennyit csak lehet:

`{{arguments_source}} | xargs -P {{max-procs}} {{command}}`
