# git

> Distribuirani sistem kontrole verzija.
> Neke podkomande kao što je `git commit` imaju svoj primer u dokumentaciji.
> Više informacija na: <https://git-scm.com/>.

- Proverava Git verziju:

`git --version`

- Prikazuje opštu pomoć:

`git --help`

- Prikazuje pomoć o Git podkomandi (npr. `commit`, `log`, itd.):

`git help {{podkomanda}}`

- Izvršava Git podkomandu:

`git {{podkomanda}}`

- Izvršava Git podkomandu u zadatoj početnoj lokaciji repozitorijuma:

`git -C {{putanja/do/repozitorijuma}} {{podkomanda}}`

- Izvršava Git podkomandu sa zadatim setom konfiguracija:

`git -c '{{config.key}}={{value}}' {{podkomanda}}`
