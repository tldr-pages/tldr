# git-grep

> A fájlokban lévő karakterláncok keresése bárhol a tároló előzményeiben. Sok olyan jelzőt fogad el, mint a hagyományos `grep`. További információ: <https://git-scm.com/docs/git-grep>.

- Egy karakterlánc keresése a nyomon követett fájlokban:

`git grep {{search_string}}`

- A nyomon követett fájlokban lévő mintának megfelelő karakterlánc keresése a fájlokban:

`git grep {{search_string}} -- {{file_glob_pattern}}`

- Egy karakterlánc keresése a nyomon követett fájlokban, beleértve az almodulokat is:

`git grep --recurse-submodules {{search_string}}`

- Egy karakterlánc keresése az előzmények egy adott pontján:

`git grep {{search_string}} {{HEAD~2}}`

- Egy karakterlánc keresése az összes ágban:

`git grep {{search_string}} $(git rev-list --all)`
