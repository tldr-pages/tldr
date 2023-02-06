# git utimes

> A fájlok módosítási idejének módosítása az utolsó commit dátumára. Nem érinti a munkafában vagy indexben lévő fájlokat. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-utimes>.

- Az összes fájl módosítási idejének módosítása az utolsó commit dátumára:

`git utimes`

- A legutóbbi commit dátumánál újabb módosítási idejű fájlok módosítási idejének módosítása, a helyi tárolóból átvett fájlok eredeti módosítási idejének megőrzése mellett:

`git utimes --newer`
