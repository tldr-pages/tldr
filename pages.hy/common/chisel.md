#սայր

> Ստեղծեք TCP/UDP թունելներ, որոնք տեղափոխվում են HTTP-ով, ապահովված SSH-ի միջոցով:.
> Ներառում է և՛ հաճախորդը, և՛ սերվերը նույն `chisel` գործադիրում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/jpillora/chisel#usage>:.

- Գործարկել Chisel սերվերը.:

`chisel server`

- Գործարկեք Chisel սերվերը, որը լսում է որոշակի նավահանգիստ.:

`chisel server {{[-p|--port]}} {{server_port}}`

- Գործարկեք chisel սերվեր, որն ընդունում է վավերացված կապեր՝ օգտագործելով օգտվողի անունը և գաղտնաբառը.:

`chisel server --auth {{username}}:{{password}}`

- Միացեք Chisel սերվերին և թունելով որոշակի նավահանգիստ դեպի հեռավոր սերվեր և նավահանգիստ.:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Միացեք Chisel սերվերին և թունելեք որոշակի հոսթ և նավահանգիստ դեպի հեռավոր սերվեր և նավահանգիստ.:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- Միացեք Chisel սերվերին, օգտագործելով օգտվողի անվան և գաղտնաբառի իսկությունը.:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Նախաձեռնեք Chisel սերվերը հակադարձ ռեժիմով կոնկրետ նավահանգստի վրա՝ միացնելով նաև SOCKS5 վստահված անձի (1080 նավահանգստի վրա) գործառույթը.:

`chisel server {{[-p|--port]}} {{server_port}} --reverse --socks5`

- Միացեք Chisel սերվերին հատուկ IP-ով և նավահանգստով, ստեղծելով հակադարձ թունել, որը քարտեզագրված է տեղական SOCKS վստահված անձին.:

`chisel client {{server_ip}}:{{server_port}} R:socks`
