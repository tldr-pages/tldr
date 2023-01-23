# csplit

> Egy fájl darabokra osztása. Ez "xx00", "xx01" stb. nevű fájlokat hoz létre. További információ: <https://www.gnu.org/software/coreutils/csplit>.

- Egy fájl felosztása az 5. és 23. sorban:

`csplit {{path/to/file}} {{5}} {{23}}`

- A fájl 5 soronként történő felosztása (ez sikertelen, ha a sorok száma nem osztható 5-tel):

`csplit {{path/to/file}} {{5}} {*}`

- A fájl 5 soronként történő felosztása, figyelmen kívül hagyva a pontos osztás hibáját:

`csplit -k {{path/to/file}} {{5}} {*}`

- A fájl felosztása az 5. sorban, és egyéni előtag használata a kimeneti fájlokhoz:

`csplit {{path/to/file}} {{5}} -f {{prefix}}`

- A fájl felosztása egy sorban, amely megfelel egy reguláris kifejezésnek:

`csplit {{path/to/file}} /{{regular_expression}}/`
