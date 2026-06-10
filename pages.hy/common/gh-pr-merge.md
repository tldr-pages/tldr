# gh pr միաձուլում

> Միավորել GitHub-ի ձգման հարցումը:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_pr_merge>:.

- Ինտերակտիվ կերպով միաձուլեք ընթացիկ մասնաճյուղի հետ կապված ձգման հարցումը.:

`gh pr merge`

- Միավորել ընթացիկ ճյուղը նշված ձգման հարցումին.:

`gh pr merge {{pr_number}} {{[-m|--merge]}}`

- Squash և միաձուլեք ձգման հարցումը, ապա ջնջեք մասնաճյուղը.:

`gh pr merge {{pr_number}} {{[-sd|--squash --delete-branch]}}`

- Վերահաստատել և միաձուլել.:

`gh pr merge {{pr_number}} {{[-r|--rebase]}}`

- Միացնել ավտոմատ միաձուլումը (squash):

`gh pr merge {{pr_number}} --auto {{[-s|--squash]}}`

- Միաձուլվել ադմինիստրատորի արտոնությունների հետ (եթե թույլատրվում է).:

`gh pr merge {{pr_number}} --admin`
