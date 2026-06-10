# mariadb

> Mariadb հաճախորդի գործիքը:.
> Լրացուցիչ տեղեկություններ. <https://mariadb.com/docs/server/clients-and-utilities/mariadb-client/mariadb-command-line-client>:.

- Միացեք MariaDB-ին որպես ընթացիկ օգտվող.:

`mariadb`

- Միացեք կոնկրետ MariaDB տվյալների բազայի.:

`mariadb {{db_name}}`

- Միացեք կոնկրետ MariaDB տվյալների բազային, օգտագործելով օգտվողի անունը և գաղտնաբառը.:

`mariadb {{[-u|--user]}} {{user_name}} {{[-p|--password]}} {{your_password}} {{db_name}}`

- Ցույց տալ նախազգուշացումները յուրաքանչյուր հայտարարությունից հետո ինտերակտիվ և խմբաքանակի ռեժիմում.:

`mariadb --show-warning`

- Ցուցադրել ավելի քիչ ծավալուն արդյունքներ (կարելի է մի քանի անգամ օգտագործել ավելի քիչ արդյունք ստանալու համար).:

`mariadb {{-s|-ss|-sss|--silent}}`

- Կատարեք SQL հայտարարությունները սցենարի ֆայլից.:

`mariadb < {{path/to/script.sql}} {{db_name}} > {{path/to/output.tab}}`

- Ստուգեք հիշողությունը և բացեք ֆայլի օգտագործումը ելքի ժամանակ.:

`mariadb --debug-check`

- Միացեք տեղական միացումների համար վարդակից ֆայլի միջոցով.:

`mariadb {{[-S|--socket]}} {{path/to/socket_name}}`
