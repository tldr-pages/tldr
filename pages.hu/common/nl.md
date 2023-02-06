# nl

> Segédprogram a sorok számozására, akár fájlból, akár standard bemenetről. További információ: <https://www.gnu.org/software/coreutils/nl>.

- Nem üres sorok számozása egy fájlban:

`nl {{path/to/file}}`

- Olvassa be a szabványos kimenetről:

`cat {{path/to/file}} | nl {{options}} -`

- Csak a nyomtatható szöveget tartalmazó sorok számozása:

`nl -t {{path/to/file}}`

- Az összes sor számozása, beleértve az üres sorokat is:

`nl -b a {{path/to/file}}`

- Csak azokat a testsorokat számozza meg, amelyek megfelelnek egy alapvető szabályos kifejezés (BRE) mintának:

`nl -b p'FooBar[0-9]' {{path/to/file}}`
