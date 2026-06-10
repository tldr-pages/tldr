# tlmgr թարմացում

> Թարմացրեք TeX Live փաթեթները:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#update-option...-pkg>:.

- Թարմացրեք բոլոր TeX Live փաթեթները.:

`sudo tlmgr update --all`

- Թարմացրեք tlmgr ինքնին.:

`sudo tlmgr update --self`

- Թարմացրեք որոշակի փաթեթ.:

`sudo tlmgr update {{package}}`

- Թարմացրեք բոլորը, բացառությամբ հատուկ փաթեթի.:

`sudo tlmgr update --all --exclude {{package}}`

- Թարմացրեք բոլոր փաթեթները՝ կատարելով ընթացիկ փաթեթների կրկնօրինակում.:

`sudo tlmgr update --all --backup`

- Թարմացրեք որոշակի փաթեթ՝ առանց դրա կախվածությունները թարմացնելու.:

`sudo tlmgr update --no-depends {{package}}`

- Մոդելավորել բոլոր փաթեթների թարմացումը՝ առանց որևէ փոփոխության.:

`sudo tlmgr update --all --dry-run`
