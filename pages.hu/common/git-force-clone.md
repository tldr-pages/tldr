# git force-clone

> A `git clone` alapvető funkcionalitását biztosítja, de ha a cél git tároló már létezik, akkor a távoli tároló klónjához hasonlóan visszaállítja azt. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-force-clone>.

- Git-tárhely klónozása egy új könyvtárba:

`git force-clone {{remote_repository_location}} {{path/to/directory}}`

- Egy Git-tárház klónozása egy új könyvtárba, egy adott ág ellenőrzésével:

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`

- Egy Git-tárhely klónozása egy Git-tárhely meglévő könyvtárába, force-reset végrehajtása, hogy hasonlítson a távolihoz, és egy adott ág ellenőrzése:

`git force-clone -b {{branch_name}} {{remote_repository_location}} {{path/to/directory}}`
