# tlmgr հեռացնել

> Տեղահանել TeX Live փաթեթները:.
> Լռելյայնորեն, հեռացված փաթեթները կպահուստավորվեն `./tlpkg/backups`-ով՝ TL տեղադրման գրացուցակում:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#remove-option...-pkg>:.

- Տեղահանեք TeX Live փաթեթը.:

`sudo tlmgr remove {{package}}`

- Մոդելավորեք փաթեթի հեռացումը առանց որևէ փոփոխության.:

`tlmgr remove --dry-run {{package}}`

- Տեղահանեք փաթեթը առանց դրա կախվածության.:

`sudo tlmgr remove --no-depends {{package}}`

- Տեղահանեք փաթեթը և կրկնօրինակեք այն որոշակի գրացուցակում.:

`sudo tlmgr remove --backupdir {{path/to/directory}} {{package}}`

- Տեղահանեք ամբողջ TeX Live-ը՝ խնդրելով հաստատում.:

`sudo tlmgr remove --all`
