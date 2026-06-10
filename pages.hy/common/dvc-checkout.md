# dvc վճարում

> Ստուգեք տվյալների ֆայլերը և գրացուցակները քեշից:.
> Լրացուցիչ տեղեկություններ. <https://doc.dvc.org/command-reference/checkout>:.

- Ստուգեք բոլոր թիրախային ֆայլերի և գրացուցակների վերջին տարբերակը.:

`dvc checkout`

- Ստուգեք նշված թիրախի վերջին տարբերակը.:

`dvc checkout {{target}}`

- Ստուգեք թիրախի որոշակի տարբերակը մեկ այլ Git commit/tag/branch-ից.:

`git checkout {{commit_hash|tag|branch}} {{target}} && dvc checkout {{target}}`
