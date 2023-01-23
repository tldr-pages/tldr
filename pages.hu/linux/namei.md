# namei

> Követi az elérési utat (ami lehet szimbolikus link is), amíg egy végpontot nem talál (fájl/könyvtár/char eszköz stb.) Ez a program hasznos a "túl sok szintű szimbolikus link" problémák megtalálásához. További információ: <https://manned.org/namei>.

- Feloldja az argumentum paraméterként megadott elérési utakat:

`namei {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Az eredmények megjelenítése hosszú listás formátumban:

`namei --long {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Megjeleníti az egyes fájltípusok üzemmódbitjeit a `ls` stílusában:

`namei --modes {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Az egyes fájlok tulajdonosának és csoportnevének megjelenítése:

`namei --owners {{path/to/a}} {{path/to/b}} {{path/to/c}}`

- Feloldás közben ne kövesse a szimlinkeket:

`namei --nosymlinks {{path/to/a}} {{path/to/b}} {{path/to/c}}`
