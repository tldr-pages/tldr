# mongoinport

> Ներմուծում է բովանդակություն JSON, CSV կամ TSV ֆայլից MongoDB տվյալների բազա:.
> Լրացուցիչ տեղեկություններ. <https://www.mongodb.com/docs/database-tools/mongoimport/>:.

- Ներմուծեք JSON ֆայլ հատուկ հավաքածու.:

`mongoimport --file {{path/to/file.json}} --uri {{mongodb_uri}} {{[-c|--collection]}} {{collection_name}}`

- Ներմուծեք CSV ֆայլ՝ օգտագործելով ֆայլի առաջին տողը դաշտերի անունները որոշելու համար.:

`mongoimport --type {{csv}} --file {{path/to/file.csv}} {{[-d|--db]}} {{database_name}} {{[-c|--collection]}} {{collection_name}}`

- Ներմուծեք JSON զանգված՝ օգտագործելով յուրաքանչյուր տարր որպես առանձին փաստաթուղթ.:

`mongoimport --jsonArray --file {{path/to/file.json}}`

- Ներմուծեք JSON ֆայլ՝ օգտագործելով հատուկ ռեժիմ և հարցում՝ առկա փաստաթղթերին համապատասխանելու համար.:

`mongoimport --file {{path/to/file.json}} --mode {{delete|merge|upsert}} --upsertFields "{{field1,field2,...}}"`

- Ներմուծեք CSV ֆայլ՝ կարդալով դաշտերի անունները առանձին CSV ֆայլից և անտեսելով դատարկ արժեքներով դաշտերը.:

`mongoimport --type {{csv}} --file {{path/to/file.csv}} --fieldFile {{path/to/field_file.csv}} --ignoreBlanks`

- Ցուցադրել օգնությունը.:

`mongoimport --help`
