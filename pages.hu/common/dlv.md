# dlv

> Debugger a Go programozási nyelvhez. További információ: <https://github.com/go-delve/delve/blob/master/Documentation/usage/dlv.md>.

- A fő csomag lefordítása és hibakeresés megkezdése az aktuális könyvtárban (alapértelmezés szerint argumentumok nélkül):

`dlv debug`

- Egy adott csomag lefordítása és hibakeresés megkezdése:

`dlv debug {{package}} {{arguments}}`

- Egy teszt bináris program lefordítása és a lefordított program hibakeresésének megkezdése:

`dlv test`

- Csatlakozás egy headless hibakereséshez:

`dlv connect {{ip_address}}`

- Csatlakozás egy futó folyamathoz és a hibakeresés megkezdése:

`div attach {{pid}}`

- Egy program lefordítása és nyomon követésének megkezdése:

`dlv trace {{package}} --regexp '{{regular_expression}}'`
