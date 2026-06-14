# zeroclaw դարպաս

> Գործարկեք դարպասի սերվերը ZeroClaw-ի համար (վեբկեռիկներ և API):.
> Լրացուցիչ տեղեկություններ. <https://github.com/zeroclaw-labs/zeroclaw#quick-start>:.

- Գործարկեք դարպասը լռելյայն նավահանգստում (8080):

`zeroclaw gateway`

- Սկսեք դարպասը որոշակի նավահանգստի վրա.:

`zeroclaw gateway {{[-p|--port]}} {{8080}}`

- Սկսեք դարպասը պատահական հասանելի նավահանգստի վրա.:

`zeroclaw gateway {{[-p|--port]}} 0`

- Սկսեք դարպասը կոնկրետ հոսթի վրա.:

`zeroclaw gateway --host {{0.0.0.0}} {{[-p|--port]}} {{8080}}`

- Ցուցադրել օգնությունը.:

`zeroclaw gateway {{[-h|--help]}}`
