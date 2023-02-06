# env

> A környezet megjelenítése vagy egy program futtatása módosított környezetben. További információ: <https://www.gnu.org/software/coreutils/env>.

- A környezet megjelenítése:

`env`

- Egy program futtatása. Gyakran használják szkriptekben a shebang (#!) után a program elérési útvonalának megkeresésére:

`env {{program}}`

- A környezet törlése és egy program futtatása:

`env -i {{program}}`

- Változó eltávolítása a környezetből és egy program futtatása:

`env -u {{variable}} {{program}}`

- Egy változó beállítása és egy program futtatása:

`env {{variable}}={{value}} {{program}}`

- Több változó beállítása és egy program futtatása:

`env {{variable1}}={{value}} {{variable2}}={{value}} {{variable3}}={{value}} {{program}}`
