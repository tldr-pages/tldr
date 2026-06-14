# cypher-shell

> Բացեք ինտերակտիվ նիստ և գործարկեք Cypher հարցումները Neo4j օրինակի դեմ:.
> Տես նաև՝ `neo4j-admin`, `mysql`:.
> Լրացուցիչ տեղեկություններ. <https://neo4j.com/docs/operations-manual/current/cypher-shell/>:.

- Միացեք լռելյայն պորտի տեղական օրինակին (`neo4j://localhost:7687`):

`cypher-shell`

- Միացեք հեռավոր օրինակին.:

`cypher-shell --address neo4j://{{host}}:{{port}}`

- Միացրեք և տրամադրեք անվտանգության հավատարմագրերը.:

`cypher-shell --username {{username}} --password {{password}}`

- Միացեք որոշակի տվյալների բազայի.:

`cypher-shell --database {{database_name}}`

- Կատարեք Cypher հայտարարությունները ֆայլում և փակեք.:

`cypher-shell --file {{path/to/file.cypher}}`

- Միացնել ֆայլի մուտքագրումը.:

`cypher-shell --log {{path/to/file.log}}`

- Ցուցադրել օգնությունը.:

`cypher-shell --help`
