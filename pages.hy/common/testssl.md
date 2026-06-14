# թեստսլ

> Ստուգեք SSL/TLS արձանագրությունները և սերվերի կողմից աջակցվող ծածկագրերը:.
> Լրացուցիչ տեղեկություններ. <https://testssl.sh/doc/testssl.1.html>:.

- Փորձարկեք սերվերը (գործարկեք յուրաքանչյուր ստուգում) 443 նավահանգստում.:

`testssl {{example.com}}`

- Փորձարկել մեկ այլ նավահանգիստ.:

`testssl {{example.com:465}}`

- Ստուգեք միայն առկա արձանագրությունները.:

`testssl --protocols {{example.com}}`

- Ստուգեք միայն խոցելիությունները.:

`testssl --vulnerable {{example.com}}`

- Ստուգեք միայն HTTP անվտանգության վերնագրերը.:

`testssl --headers {{example.com}}`

- Փորձեք STARTTLS միացված այլ արձանագրություններ.:

`testssl --starttls {{ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql}} {{example.com}}:{{port}}`
