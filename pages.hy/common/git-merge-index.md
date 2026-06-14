# git միաձուլման ինդեքս

> Գործարկել միաձուլման ծրագիր ֆայլերի վրա, որոնք միաձուլման կարիք ունեն:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-merge-index>:.

- Միավորել լուծում պահանջող բոլոր ֆայլերը՝ օգտագործելով ստանդարտ օգնականը.:

`git merge-index git-merge-one-file -a`

- Միավորել որոշակի ֆայլ.:

`git merge-index git-merge-one-file -- {{path/to/file}}`

- Միավորել բազմաթիվ ֆայլեր՝ շարունակելով ձախողումները.:

`git merge-index -o git-merge-one-file -- {{path/to/file1 path/to/file2 ...}}`

- Հանգիստ միաձուլեք բոլոր ֆայլերը հատուկ ծրագրի հետ.:

`git merge-index -q {{merge-program}} -a`

- Ստուգեք ֆայլի միաձուլման մուտքերը՝ օգտագործելով `cat`:

`git merge-index cat -- {{path}}`
