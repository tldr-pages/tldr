# pg_createsubscriber

> Փոխակերպեք ֆիզիկական կրկնօրինակը նոր տրամաբանական կրկնօրինակի:.
> Լրացուցիչ տեղեկություններ. <https://www.postgresql.org/docs/current/app-pgcreatesubscriber.html>:.

- Փոխակերպեք ֆիզիկական կրկնօրինակը տրամաբանական կրկնօրինակի հատուկ տվյալների բազայի համար.:

`pg_createsubscriber {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Կատարեք չոր գործարկում՝ առանց նպատակային գրացուցակը փոփոխելու.:

`pg_createsubscriber {{[-n|--dry-run]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Բաժանորդագրության համար միացնել երկփուլային կատարումը.:

`pg_createsubscriber {{[-T|--enable-two-phase]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Փոխակերպեք բառացի ելքով.:

`pg_createsubscriber {{[-v|--verbose]}} {{[-d|--database]}} {{dbname}} {{[-D|--pgdata]}} {{path/to/data}} {{[-P|--publisher-server]}} {{connstr}}`

- Ցուցադրել օգնությունը.:

`pg_createsubscriber {{[-?|--help]}}`
