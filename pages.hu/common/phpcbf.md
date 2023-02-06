# phpcbf

> A phpcs által észlelt jogsértések javítása. További információ: <https://github.com/squizlabs/PHP_CodeSniffer>.

- A megadott könyvtárban (alapértelmezés szerint a PEAR szabványban) lévő hibák javítása:

`phpcbf {{path/to/directory}}`

- A telepített kódolási szabványok listájának megjelenítése:

`phpcbf -i`

- Megad egy kódolási szabványt, amellyel szemben érvényesíteni kívánja:

`phpcbf {{path/to/directory}} --standard {{standard}}`

- Megadni a szimatoláskor figyelembe veendő, vesszővel elválasztott fájlkiterjesztéseket:

`phpcbf {{path/to/directory}} --extensions {{file_extension(s)}}`

- A feldolgozás előtt betöltendő fájlok vesszővel elválasztott listája:

`phpcbf {{path/to/directory}} --bootstrap {{file(s)}}`

- Ne keressen vissza alkönyvtárakba:

`phpcbf {{path/to/directory}} -l`
