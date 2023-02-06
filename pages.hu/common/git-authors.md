# git authors

> Egy Git tároló committereinek listájának generálása. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-authors>.

- A committerek teljes listájának kiírása a `stdout` címre a `AUTHORS` fájl helyett:

`git authors --list`

- A committerek listájának csatolása a `AUTHORS` fájlhoz, és megnyitás az alapértelmezett szerkesztővel:

`git authors`

- A committerek listájának csatolása az e-mailek kivételével a `AUTHORS` fájlhoz, és megnyitása az alapértelmezett szerkesztővel:

`git authors --no-email`
