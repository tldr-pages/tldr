# git-grep

> Belirtilen söz dizisini bir deponun geçmişi dahil tüm dosyalarında ara.
> Sıradan `grep` komutundaki birçok ek bu komut için de aynen geçerlidir.
> Daha fazla bilgi için: <https://git-scm.com/docs/git-grep>.

- İzlenen dosyalarda belirtilen söz dizisini ara:

`git grep {{söz_dizisi}}`

- İzlenen dosyalarda belirtilen desene uygun, belirtilen söz dizisini ara:

`git grep {{söz_dizisi}} -- {{file_glob_pattern}}`

- Alt modüller de dahil olmak üzere izlenen dosyalarda belirtilen söz dizisini ara:

`git grep --recurse-submodules {{söz_dizisi}}`

- Belirtilen depo geçmişinde belirtilen söz dizisini ara:

`git grep {{söz_dizisi}} {{HEAD~2}}`

- Belirtilen söz dizisini tüm dallarda ara:

`git grep {{söz_dizisi}} $(git rev-list --all)`
