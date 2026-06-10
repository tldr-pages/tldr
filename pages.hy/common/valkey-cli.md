# valkey-cli

> Բացեք կապ Valkey սերվերի հետ:.
> Լրացուցիչ տեղեկություններ. <https://valkey.io/topics/cli/>:.

- Միացեք տեղական սերվերին.:

`valkey-cli`

- Միացեք հեռավոր սերվերին լռելյայն նավահանգստում (6379):

`valkey-cli -h {{host}}`

- Միացեք հեռավոր սերվերին, որը նշում է պորտի համարը.:

`valkey-cli -h {{host}} -p {{port}}`

- Միացեք հեռավոր սերվերին, որը նշում է URI.:

`valkey-cli -u {{uri}}`

- Նշեք գաղտնաբառ.:

`valkey-cli -a {{password}}`

- Կատարել valkey հրամանը.:

`valkey-cli {{valkey_command}}`

- Միացեք տեղական կլաստերին.:

`valkey-cli -c`
