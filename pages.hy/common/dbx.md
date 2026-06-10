# dbx

> Փոխազդել Databricks հարթակի հետ:.
> Նշում. այս գործիքը հեռացվել է, և դրա փոխարեն խորհուրդ է տրվում օգտագործել Databricks Asset Bundles-ը:.
> Լրացուցիչ տեղեկություններ. <https://dbx.readthedocs.io/en/latest/reference/cli/#dbx>:.

- Ստեղծեք նոր `dbx` նախագիծ ընթացիկ աշխատանքային գրացուցակում.:

`dbx configure --profile {{DEFAULT}}`

- Համաժամացրեք տեղական ֆայլերը նշված ուղուց դեպի DBFS և հետևեք փոփոխություններին.:

`dbx sync dbfs --source {{path/to/directory}} --dest {{path/to/remote_directory}}`

- Տեղադրեք նշված աշխատանքային հոսքը արտեֆակտ պահելու համար.:

`dbx deploy {{workflow_name}}`

- Գործարկել նշված աշխատանքային հոսքը այն տեղակայելուց հետո.:

`dbx launch {{workflow_name}}`
