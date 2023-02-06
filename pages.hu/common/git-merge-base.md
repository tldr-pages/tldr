# git merge-base

> Két commit közös ősének keresése. További információ: <https://git-scm.com/docs/git-merge-base>.

- Két commit legjobb közös ősének kiírása:

`git merge-base {{commit_1}} {{commit_2}}`

- Két commit összes legjobb közös ősének kiadása:

`git merge-base --all {{commit_1}} {{commit_2}}`

- Annak ellenőrzése, hogy egy commit egy adott commit őse-e:

`git merge-base --is-ancestor {{ancestor_commit}} {{commit}}`
