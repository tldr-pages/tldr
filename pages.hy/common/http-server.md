# http-սերվեր

> Պարզ ստատիկ HTTP սերվեր՝ ստատիկ ֆայլեր սպասարկելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/http-party/http-server>:.

- Սկսեք HTTP սերվերը, որը լսում է լռելյայն նավահանգիստը՝ ընթացիկ գրացուցակը սպասարկելու համար.:

`http-server`

- Սկսեք HTTP սերվեր որոշակի նավահանգստի վրա՝ որոշակի գրացուցակ սպասարկելու համար.:

`http-server {{path/to/directory}} {{[-p|--port]}} {{port}}`

- Սկսեք HTTP սերվեր՝ օգտագործելով հիմնական նույնականացումը.:

`http-server --username {{username}} --password {{password}}`

- Գործարկեք HTTP սերվեր, որտեղ գրացուցակների ցուցակներն անջատված են.:

`http-server -d {{false}}`

- Սկսեք HTTPS սերվերը լռելյայն նավահանգստի վրա՝ օգտագործելով նշված վկայագիրը.:

`http-server {{[-S|--ssl]}} {{[-C|--cert]}} {{path/to/cert.pem}} {{[-K|--key]}} {{path/to/key.pem}}`

- Սկսեք HTTP սերվեր և ներառեք հաճախորդի IP հասցեն ելքային գրանցման մեջ.:

`http-server --log-ip`

- Սկսեք HTTP սերվերը CORS-ով միացված՝ ներառելով `Access-Control-Allow-Origin: *` վերնագիրը բոլոր պատասխաններում.:

`http-server --cors`

- Սկսեք HTTP սերվեր, որտեղ գրանցումն անջատված է.:

`http-server {{[-s|--silent]}}`
