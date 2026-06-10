# մութhttpd

> Darkhttpd վեբ սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/emikulic/darkhttpd#how-to-run-darkhttpd>:.

- Սկսեք սերվերը սպասարկել նշված փաստաթղթի արմատը.:

`darkhttpd {{path/to/docroot}}`

- Գործարկեք սերվերը նշված նավահանգստում (նավահանգիստ 8080 լռելյայն, եթե այն աշխատում է որպես ոչ արմատային օգտվող).:

`darkhttpd {{path/to/docroot}} --port {{port}}`

- Լսեք միայն նշված IP հասցեով (լռելյայն, սերվերը լսում է բոլոր ինտերֆեյսներում).:

`darkhttpd {{path/to/docroot}} --addr {{ip_address}}`
