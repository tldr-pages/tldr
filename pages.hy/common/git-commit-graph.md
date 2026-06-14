# git commit-graph

> Գրեք և հաստատեք Git commit-graph ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-commit-graph>:.

- Գրեք commit-graph ֆայլ փաթեթավորված պարտավորությունների համար պահեստի տեղական `.git` գրացուցակում.:

`git commit-graph write`

- Գրեք commit-graph ֆայլ, որը պարունակում է բոլոր հասանելի պարտավորությունները.:

`git show-ref {{[-s|--hash]}} | git commit-graph write --stdin-commits`

- Գրեք commit-graph ֆայլ, որը պարունակում է բոլոր commit-ները ընթացիկ commit-graph ֆայլում՝ նրանց հետ միասին, որոնք հասանելի են `HEAD`-ից:

`git rev-parse {{HEAD}} | git commit-graph write --stdin-commits --append`
