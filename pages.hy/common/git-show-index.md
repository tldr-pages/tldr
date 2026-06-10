# git show-index

> Ցույց տալ Git պահեստի փաթեթավորված արխիվային ինդեքսը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-show-index>:.

- Կարդացեք IDX ֆայլը Git փաթեթի համար և թափեք դրա բովանդակությունը `stdout`:

`git show-index {{path/to/file.idx}}`

- Նշեք հաշ ալգորիթմը ինդեքսային ֆայլի համար (փորձնական).:

`git show-index --object-format {{sha1|sha256}} {{path/to/file}}`
