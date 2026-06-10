# az պահեստային միավոր

> Կառավարեք Azure Table պահեստավորման օբյեկտները:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/storage/entity>:.

- Տեղադրեք էությունը աղյուսակում.:

`az storage entity insert {{[-e|--entity]}} {{space_separated_key_value_pairs}} {{[-t|--table-name]}} {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Ջնջել առկա էությունը աղյուսակից.:

`az storage entity delete --partition-key {{partition_key}} --row-key {{row_key}} {{[-t|--table-name]}} {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Թարմացրեք գոյություն ունեցող կազմակերպությունը՝ միացնելով դրա հատկությունները.:

`az storage entity merge {{[-e|--entity]}} {{space_separated_key_value_pairs}} {{[-t|--table-name]}} {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Թվարկեք այն կազմակերպությունները, որոնք բավարարում են հարցումը.:

`az storage entity query --filter {{query_filter}} {{[-t|--table-name]}} {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Ստացեք սուբյեկտ նշված աղյուսակից.:

`az storage entity show --partition-key {{partition_key}} --row-key {{row_key}} {{[-t|--table-name]}} {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`
