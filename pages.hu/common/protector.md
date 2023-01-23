# protector

> A GitHub tárolók ágainak védelme vagy védelme feloldása. További információ: <https://github.com/jcgay/protector>.

- GitHub-repositórium ágainak védelme (ágvédelmi szabályok létrehozása):

`protector {{branches_regex}} -repos {{organization/repository}}`

- Használja a szárazonfutást, hogy lássa, mit védene (felszabadításhoz is használható):

`protector -dry-run {{branches_regex}} -repos {{organization/repository}}`

- Egy GitHub adattár ágainak felszabadítása (ágvédelmi szabályok törlése):

`protector -free {{branches_regex}} -repos {{organization/repository}}`
