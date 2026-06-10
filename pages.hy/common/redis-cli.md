# redis-cli

> Բացեք կապ Redis սերվերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://redis.io/docs/latest/develop/>:.

- Միացեք տեղական սերվերին.:

`redis-cli`

- Միացեք հեռավոր սերվերին լռելյայն նավահանգստում (6379):

`redis-cli -h {{host}}`

- Միացեք հեռավոր սերվերին, որը նշում է պորտի համարը.:

`redis-cli -h {{host}} -p {{port}}`

- Միացեք հեռավոր սերվերին, որը նշում է URI.:

`redis-cli -u {{uri}}`

- Նշեք գաղտնաբառ.:

`redis-cli -a {{password}}`

- Կատարեք Redis հրամանը.:

`redis-cli {{redis_command}}`

- Միացեք տեղական կլաստերին.:

`redis-cli -c`
