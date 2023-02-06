# git obliterate

> Bizonyos fájlok törlése és előzményeik törlése egy Git-tárból. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-obliterate>.

- Bizonyos fájlok létezésének törlése:

`git obliterate {{file_1 file_2 ...}}`

- Törli bizonyos fájlok létezését 2 commit között:

`git obliterate {{file_1 file_2 ...}} -- {{commit_hash_1}}..{{commit_hash_2}}`
