# git p4

> Ներմուծեք և ներկայացրեք Perforce պահեստարաններ:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-p4>:.

- Կլոնավորեք Perforce պահեստը նոր Git պահոցում.:

`git p4 clone {{path/to/p4_depot}}`

- Համաժամացրեք փոփոխությունները Perforce-ից ընթացիկ Git պահոցում.:

`git p4 sync {{path/to/p4_depot}}`

- Վերահաստատեք տեղական պարտավորությունները՝ ի լրումն վերջին Perforce փոփոխությունների.:

`git p4 rebase`

- Վերադարձեք Git-ի փոփոխությունները Perforce-ին.:

`git p4 submit`

- Կլոնավորեք Perforce-ի ամբողջական պատմությունը միայն վերջին փոփոխությունների ցանկի փոխարեն.:

`git p4 clone {{path/to/p4_depot}}@all`
