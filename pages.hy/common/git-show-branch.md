# git շոու-մասնաճյուղ

> Ցուցադրել մասնաճյուղերը և դրանց պարտավորությունները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-show-branch>:.

- Ցույց տվեք մասնաճյուղի վերջին պարտավորությունների ամփոփագիրը.:

`git show-branch {{branch_name|ref|commit}}`

- Համեմատեք պարտավորությունները բազմաթիվ պարտավորությունների կամ ճյուղերի պատմության մեջ.:

`git show-branch {{branch_name1|ref1|commit1 branch_name2|ref2|commit2 ...}}`

- Համեմատեք բոլոր հեռակա հետևող մասնաճյուղերը.:

`git show-branch {{[-r|--remotes]}}`

- Համեմատեք ինչպես տեղական, այնպես էլ հեռավոր հետևման մասնաճյուղերը.:

`git show-branch {{[-a|--all]}}`

- Թվարկեք բոլոր ճյուղերի վերջին պարտավորությունները.:

`git show-branch {{[-a|--all]}} --list`

- Համեմատե՛ք տվյալ ճյուղը ընթացիկ ճյուղի հետ.:

`git show-branch --current {{commit|branch_name|ref}}`

- Ցուցադրել կատարման անունը հարաբերական անվան փոխարեն.:

`git show-branch --sha1-name --current {{current|branch_name|ref}}`

- Շարունակեք շարունակել ընդհանուր նախահայրից անցած որոշակի թվով պարտավորություններ.:

`git show-branch --more {{5}} {{branch_name1|ref1|commit1 branch_name2|ref2|commit2 ...}}`
