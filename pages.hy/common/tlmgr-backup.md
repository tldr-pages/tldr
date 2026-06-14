# tlmgr կրկնօրինակում

> Կառավարեք TeX Live փաթեթների կրկնօրինակները:.
> Լռելյայն պահուստային գրացուցակը նշված է `backupdir` տարբերակով և կարելի է ձեռք բերել `tlmgr option`-ով:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#backup>:.

- Կատարեք մեկ կամ մի քանի փաթեթների կրկնօրինակում.:

`tlmgr backup {{package1 package2 ...}}`

- Կրկնօրինակեք բոլոր փաթեթները.:

`tlmgr backup --all`

- Կատարեք կրկնօրինակում հատուկ գրացուցակում.:

`tlmgr backup {{package}} --backupdir {{path/to/backup_directory}}`

- Հեռացրեք մեկ կամ մի քանի փաթեթների կրկնօրինակը.:

`tlmgr backup clean {{package1 package2 ...}}`

- Հեռացրեք բոլոր կրկնօրինակները.:

`tlmgr backup clean --all`
