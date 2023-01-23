# for

> Egy parancs többszöri végrehajtása. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- A megadott parancsok végrehajtása a megadott elemek mindegyikére:

`for {{variable}} in {{item1 item2 ...}}; do {{echo "Loop is executed"}}; done`

- Iteráljon egy adott számtartományon:

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "Loop is executed"}}; done`

- Iterálás egy adott fájllistán:

`for {{variable}} in {{path/to/file1 path/to/file2 ...}}; do {{echo "Loop is executed"}}; done`

- Iteráció a könyvtárak adott listáján:

`for {{variable}} in {{path/to/directory1/ path/to/directory2/ ...}}; do {{echo "Loop is executed"}}; done`

- Adott parancs végrehajtása minden könyvtárban:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "Loop is executed"}}) done`
