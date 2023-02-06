# zmv

> A megadott kiterjesztett glob-mintának megfelelő fájlok áthelyezése vagy átnevezése. Lásd még: `zcp` és `zln`. További információ: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Fájlok áthelyezése reguláris kifejezés-szerű mintát használva:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- A mozgatás eredményének előnézete, anélkül, hogy tényleges változtatásokat végezne:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Fájlok interaktív áthelyezése, minden változtatás előtt felszólítással:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- Minden egyes művelet részletes kiírása végrehajtás közben:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`
