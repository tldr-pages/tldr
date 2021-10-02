# git

> Distribuirani sistem kontrole verzija.
> Neke podkomande kao što je `git commit` imaju svoj primer u dokumentaciji.
> More information: <https://git-scm.com/>.

- Proverava Git verziju:

`git --version`

- Prikazuje opštu pomoć:

`git --help`

- Prikazuje pomoć o Git podkomandi (npr. `commit`, `log`, itd.):

`git help {{subcommand}}`

- Izvršava Git podkomandu:

`git {{subcommand}}`

- Izvršava Git podkomandu u zadatoj početnoj lokaciji repozitorijuma:

`git -C {{path/to/repo}} {{subcommand}}`

- Izvršava Git podkomandu sa zadatim setom konfiguracija:

`git -c '{{config.key}}={{value}}' {{subcommand}}`
