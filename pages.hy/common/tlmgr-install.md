# tlmgr տեղադրում

> Տեղադրեք TeX Live փաթեթներ:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#install-option...-pkg>:.

- Տեղադրեք փաթեթը և դրա կախվածությունները.:

`sudo tlmgr install {{package}}`

- Վերականգնեք փաթեթը.:

`sudo tlmgr install --reinstall {{package}}`

- Մոդելավորել փաթեթի տեղադրումը առանց որևէ փոփոխության.:

`tlmgr install --dry-run {{package}}`

- Տեղադրեք փաթեթ առանց դրա կախվածության.:

`sudo tlmgr install --no-depends {{package}}`

- Տեղադրեք փաթեթ հատուկ ֆայլից.:

`sudo tlmgr install --file {{path/to/package}}`
