# vacuumdb

> Աղբ հավաքեք և վերլուծեք PostgreSQL տվյալների բազան:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-vacuumdb.html>:.

- Վակուում հատուկ տվյալների բազա.:

`vacuumdb {{database_name}}`

- Վակուում է բոլոր տվյալների բազաները.:

`vacuumdb {{[-a|--all]}}`

- Վակուում հատուկ աղյուսակը տվյալների բազայում.:

`vacuumdb {{[-t|--table]}} {{table_name}} {{database_name}}`

- Վակուում և թարմացրեք վիճակագրությունը հարցումների պլանավորողի համար.:

`vacuumdb {{[-z|--analyze]}} {{database_name}}`

- Կատարել ամբողջական վակուում (ավելի ագրեսիվ, կողպում է աղյուսակները, վերաշարադրում է ամբողջ աղյուսակը).:

`vacuumdb {{[-f|--full]}} {{database_name}}`

- Վակուում` լայնածավալ ելքով.:

`vacuumdb {{[-v|--verbose]}} {{database_name}}`

- Վակուում է տվյալների բազան՝ օգտագործելով բազմաթիվ զուգահեռ աշխատանքներ.:

`vacuumdb --jobs {{number_of_jobs}} {{database_name}}`
