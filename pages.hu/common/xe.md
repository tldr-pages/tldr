# xe

> Egy parancs egyszeri végrehajtása egy másik parancsból vagy fájlból átvett minden egyes sor után. További információ: <https://github.com/leahneukirchen/xe>.

- Egy parancs egyszeri futtatása a bemeneti adatok minden egyes argumentumként megadott sorára:

`{{arguments_source}} | xe {{command}}`

- A parancsok végrehajtása, a helyőrző ( `{}` jelű) minden előfordulását a bemeneti sorral helyettesítve:

`{{arguments_source}} | xe {{command}} {} {{optional_extra_arguments}}`

- Futtasson egy héjszkriptet, minden `N` sort egyetlen hívássá egyesítve:

`echo -e 'a\nb' | xe -N{{2}} -s 'echo $2 $1'`

- Törölje az összes `.backup` kiterjesztésű fájlt:

`find . -name {{'*.backup'}} | xe rm -v`

- Legfeljebb `max-jobs` folyamatok párhuzamos futtatása; az alapértelmezett érték 1. Ha a `max-jobs` értéke 0, akkor az xe annyi folyamatot futtat, ahány processzormag van:

`{{arguments_source}} | xe -j {{max-jobs}} {{command}}`
