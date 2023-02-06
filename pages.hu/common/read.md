# read

> BASH beépített program a standard bemenetről történő adatlekérdezéshez. További információ: <https://manned.org/read.1p>.

- A billentyűzetről beírt adatok tárolása:

`read {{variable}}`

- Tárolja a következő beírt sorok mindegyikét egy tömb értékeiként:

`read -a {{array}}`

- Adja meg a maximálisan beolvasandó karakterek számát:

`read -n {{character_count}} {{variable}}`

- Új sor helyett egy adott karaktert használhat elhatárolóként:

`read -d {{new_delimiter}} {{variable}}`

- Ne hagyja, hogy a backslash () menekülő karakterként működjön:

`read -r {{variable}}`

- A bevitel előtt jelenítsen meg egy promptot:

`read -p "{{Enter your input here: }}" {{variable}}`

- Ne visszhangozza a beírt karaktereket (néma üzemmód):

`read -s {{variable}}`

- Olvassa be a `stdin` címet, és minden sorban hajtson végre egy műveletet:

`while read line; do echo "$line"; done`
