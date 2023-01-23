# berks

> Chef szakácskönyv függőségi menedzser. További információ: <https://docs.chef.io/berkshelf.html>.

- Telepítse a szakácskönyv függőségeket egy helyi repóba:

`berks install`

- Egy adott szakácskönyv és függőségeinek frissítése:

`berks update {{cookbook}}`

- Szakácskönyv feltöltése a Chef szerverre:

`berks upload {{cookbook}}`

- Egy szakácskönyv függőségeinek megtekintése:

`berks contingent {{cookbook}}`
