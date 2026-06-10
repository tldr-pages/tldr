# git lfs

> Աշխատեք մեծ ֆայլերի հետ Git-ի պահոցներում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/git-lfs/git-lfs/tree/main/docs>:.

- Նախաձեռնել Git LFS:

`git lfs install`

- Հետևեք ֆայլերին, որոնք համապատասխանում են աշխարհին.:

`git lfs track '{{*.bin}}'`

- Փոխեք Git LFS վերջնակետի URL-ը (օգտակար է, եթե LFS սերվերը առանձին է Git սերվերից).:

`git config {{[-f|--file]}} .lfsconfig lfs.url {{lfs_endpoint_url}}`

- Ցուցակեք հետևված նախշերը.:

`git lfs track`

- Ցուցակեք հետևված ֆայլերը, որոնք կատարվել են.:

`git lfs ls-files`

- Բոլոր Git LFS օբյեկտները մղեք հեռավոր սերվերին (օգտակար է, եթե սխալներ են հանդիպում).:

`git lfs push --all {{remote_name}} {{branch_name}}`

- Վերցրեք բոլոր Git LFS օբյեկտները.:

`git lfs fetch`

- Փոխարինեք ցուցիչի ֆայլերը իրական Git LFS օբյեկտներով.:

`git lfs checkout`
