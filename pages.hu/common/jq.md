# jq

> Egy parancssori JSON-feldolgozó, amely egy domain-specifikus nyelvet használ. További információ: <https://stedolan.github.io/jq/manual/>.

- Egy adott kifejezés végrehajtása (színes és formázott json nyomtatása):

`{{cat path/to/file.json}} | jq '.'`

- Egy adott szkript végrehajtása:

`{{cat path/to/file.json}} | jq --from-file {{path/to/script.jq}}`

- Konkrét argumentumok átadása:

`{{cat path/to/file.json}} | jq {{--arg "name1" "value1" --arg "name2" "value2" ...}} '{{. + $ARGS.named}}'`

- Konkrét kulcsok nyomtatása:

`{{cat path/to/file.json}} | jq '{{.key1, .key2, ...}}'`

- Konkrét tömbelemek nyomtatása:

`{{cat path/to/file.json}} | jq '{{.[index1], .[index2], ...}}'`

- Az összes tömbelem/tárgykulcs kiírása:

`{{cat path/to/file.json}} | jq '.[]'`

- Adott kulcsok hozzáadása/eltávolítása:

`{{cat path/to/file.json}} | jq '. {{+|-}} {{{"key1": "value1", "key2": "value2", ...}}}'`
