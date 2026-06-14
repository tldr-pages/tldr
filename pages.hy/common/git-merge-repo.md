# git միաձուլում-ռեպո

> Միավորել երկու պահեստային պատմություններ:.
> `git-extras`-ի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/tj/git-extras/blob/main/Commands.md#git-merge-repo>:.

- Միավորել պահեստի մասնաճյուղը ընթացիկ պահոցի գրացուցակում.:

`git merge-repo {{path/to/repo}} {{branch_name}} {{path/to/directory}}`

- Միավորել հեռավոր պահեստի ճյուղը ընթացիկ պահոցի գրացուցակի մեջ՝ չպահպանելով պատմությունը.:

`git merge-repo {{path/to/remote_repo}} {{branch_name}} .`
