# git daemon

> Egy nagyon egyszerű szerver a Git tárolókhoz. További információ: <https://git-scm.com/docs/git-daemon>.

- Indítson el egy Git démont egy fehérlistás könyvtárkészlettel:

`git daemon --export-all {{path/to/directory1}} {{path/to/directory2}}`

- Indítson el egy Git démont egy adott alapkönyvtárral, és engedélyezze a Git-tárháznak látszó összes alkönyvtárból való lehívást:

`git daemon --base-path={{path/to/directory}} --export-all --reuseaddr`

- Indítson el egy Git-démont a megadott könyvtárhoz, bővebben kiírva a naplóüzeneteket, és engedélyezve a Git-kliensek számára, hogy írjanak rá:

`git daemon {{path/to/directory}} --enable=receive-pack --informative-errors --verbose`
