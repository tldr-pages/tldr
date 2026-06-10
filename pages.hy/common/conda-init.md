# conda init

> Նախաձեռնել կոնդա կեղևի փոխազդեցության համար:.
> Փոփոխությունների ուժի մեջ մտնելու համար վահանակների մեծ մասը պետք է փակվի և վերագործարկվի:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/latest/commands/init.html>:.

- Նախաձեռնեք որոշակի շերտ (եթե ոչ մեկը նշված չէ, UNIX-ի համար նախադրված է `bash` և Windows-ի համար `powershell`):

`conda init {{zsh|bash|powershell|fish|tcsh|xonsh}}`

- Նախաձեռնել բոլոր հասանելի պատյանները.:

`conda init --all`

- Նախաձեռնել conda համակարգի բոլոր օգտվողների համար.:

`conda init --system`

- Մի նախաստորագրեք conda ընթացիկ օգտագործողի համար.:

`conda init --no-user`

- Ավելացնել `condabin/` գրացուցակը `$PATH`-ին:

`conda init --condabin`

- Հետարկել վերջին `conda init` էֆեկտները.:

`conda init --reverse`
