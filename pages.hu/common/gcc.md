# gcc

> C és C++ forrásfájlok előfeldolgozása és lefordítása, majd összeszerelése és összekapcsolása. További információ: <https://gcc.gnu.org>.

- Több forrásfájl fordítása végrehajthatóvá:

`gcc {{path/to/source1.c path/to/source2.c ...}} -o {{path/to/output_executable}}`

- Közös figyelmeztetések megjelenítése, hibakereső szimbólumok megjelenítése a kimeneten, és optimalizálás a hibakeresés befolyásolása nélkül:

`gcc {{path/to/source.c}} -Wall -g -Og -o {{path/to/output_executable}}`

- Könyvtárak bevonása más elérési útvonalról:

`gcc {{path/to/source.c}} -o {{path/to/output_executable}} -I{{path/to/header}} -L{{path/to/library}} -l{{library_name}}`

- A forráskód fordítása Assembler utasításokká:

`gcc -S {{path/to/source.c}}`

- A forráskód lefordítása objektumfájlba linkelés nélkül:

`gcc -c {{path/to/source.c}}`
