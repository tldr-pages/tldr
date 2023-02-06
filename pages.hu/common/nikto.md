# nikto

> Webkiszolgáló-olvasó, amely több elemre vonatkozóan végez teszteket webkiszolgálókkal szemben. További információ: <https://cirt.net/Nikto2>.

- Alapvető Nikto vizsgálat elvégzése egy célállomáson:

`perl nikto.pl -h {{192.168.0.1}}`

- Adja meg a portszámot, amikor alapszintű vizsgálatot végez:

`perl nikto.pl -h {{192.168.0.1}} -p {{443}}`

- Portok és protokollok vizsgálata teljes URL-szintaxissal:

`perl nikto.pl -h {{https://192.168.0.1:443/}}`

- Több port vizsgálatát végezze el ugyanabban a vizsgálati munkamenetben:

`perl nikto.pl -h {{192.168.0.1}} -p {{80,88,443}}`

- Frissítés a legújabb bővítményekre és adatbázisokra:

`perl nikto.pl -update`
