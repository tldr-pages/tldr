# git init

> Új helyi Git-tárat inicializál. További információ: <https://git-scm.com/docs/git-init>.

- Új helyi tárolóhely inicializálása:

`git init`

- A megadott névvel inicializál egy tárolót a kezdeti ághoz:

`git init --initial-branch={{branch_name}}`

- Adattár inicializálása SHA256-ot használva az objektumok hash-jeihez (Git 2.29+ verzió szükséges):

`git init --object-format={{sha256}}`

- Barebones repository inicializálása, amely alkalmas ssh-n keresztül történő távoli használatra:

`git init --bare`
