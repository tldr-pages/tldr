# git show-index

> Afișați indexul de arhivă ambalat al unui depozit Git.
> Mai multe informaţii: <https://git-scm.com/docs/git-show-index>

- Citiți un fișier IDX pentru un pachet Git și dump conținutul său la stdout:

`git show-index {{path/to/file.idx}}`

- Specificați algoritmul hash pentru fișierul index (experimental):

`git show-index --object-format={{sha1|sha256}} {{path/to/file}}`
