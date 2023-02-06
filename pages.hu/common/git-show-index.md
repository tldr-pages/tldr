# git show-index

> Megjeleníti egy Git-tárház csomagolt archívumának indexét. További információ: <https://git-scm.com/docs/git-show-index>.

- IDX fájl olvasása egy Git csomagfájlhoz, és a tartalmának dumpolása a `stdout` címre:

`git show-index {{path/to/file.idx}}`

- Az indexfájl hash-algoritmusának megadása (kísérleti):

`git show-index --object-format={{sha1|sha256}} {{path/to/file}}`
