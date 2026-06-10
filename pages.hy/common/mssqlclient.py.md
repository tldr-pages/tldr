# mssqlclient.py

> Միացեք Microsoft SQL Server-ի օրինակներին և կատարեք հարցումներ:.
> Impacket փաթեթի մի մասը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/fortra/impacket>:.

- Միացեք MSSQL սերվերին, օգտագործելով Windows նույնականացումը.:

`mssqlclient.py -windows-auth {{domain}}/{{username}}:{{password}}@{{target}}`

- Միացեք SQL սերվերի նույնականացման միջոցով.:

`mssqlclient.py {{username}}:{{password}}@{{target}}`

- Միացեք՝ օգտագործելով pass-the-hash վավերացում.:

`mssqlclient.py {{domain}}/{{username}}@{{target}} -hashes {{LM_Hash}}:{{NT_Hash}}`

- Միացեք Kerberos-ի նույնականացման միջոցով (պահանջում է վավեր տոմսեր).:

`mssqlclient.py -k {{domain}}/{{username}}@{{target}}`

- Միացման ժամանակ կատարեք հատուկ SQL հրաման.:

`mssqlclient.py {{username}}:{{password}}@{{target}} -query "{{SELECT user_name();}}"`

- Կատարեք մի քանի SQL հրամաններ ֆայլից.:

`mssqlclient.py {{username}}:{{password}}@{{target}} -file {{path/to/sql_file.sql}}`

- Միացեք տվյալների բազայի որոշակի օրինակին (կանխադրվածը `None` է):

`mssqlclient.py {{username}}:{{password}}@{{target}} -db {{database_name}}`

- Ցուցադրել SQL հարցումները նախքան կատարումը.:

`mssqlclient.py {{username}}:{{password}}@{{target}} -show`
