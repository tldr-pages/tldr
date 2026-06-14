# mongoexport

> Արտադրեք տվյալների արտահանում, որոնք պահվում են MongoDB օրինակում, որը ձևաչափված է որպես JSON կամ CSV:.
> Լրացուցիչ տեղեկություններ. <https://www.mongodb.com/docs/database-tools/mongoexport/>:.

- Արտահանել հավաքածուն `stdout`՝ JSON ձևաչափով.:

`mongoexport --uri={{connection_string}} --collection={{collection_name}}`

- Արտահանեք նշված հավաքածուի փաստաթղթերը, որոնք համապատասխանում են հարցումին JSON ֆայլ.:

`mongoexport --db={{database_name}} --collection={{collection_name}} --query="{{query_object}}" --out={{path/to/file.json}}`

- Արտահանել փաստաթղթերը որպես JSON զանգված՝ յուրաքանչյուր տողում մեկ օբյեկտի փոխարեն.:

`mongoexport --collection={{collection_name}} --jsonArray`

- Արտահանել փաստաթղթերը CSV ֆայլ.:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --out={{path/to/file.csv}}`

- Արտահանել փաստաթղթերը, որոնք համապատասխանում են նշված ֆայլի հարցումին CSV ֆայլի մեջ՝ բաց թողնելով դաշտերի անունների ցանկը առաջին տողում.:

`mongoexport --collection={{collection_name}} --type={{csv}} --fields="{{field1,field2,...}}" --queryFile={{path/to/file}} --noHeaderLine --out={{path/to/file.csv}}`

- Արտահանել փաստաթղթերը `stdout`՝ ձևաչափված որպես մարդու կողմից ընթեռնելի JSON:

`mongoexport --uri={{mongodb_uri}} --collection={{collection_name}} --pretty`

- Ցուցադրել օգնությունը.:

`mongoexport --help`
