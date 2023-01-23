# timeout

> Egy parancs futtatása időkorlátozással. További információ: <https://www.gnu.org/software/coreutils/timeout>.

- Futtassa le a `sleep 10` címet, és fejezze be, ha 3 másodpercnél tovább fut:

`timeout {{3s}} {{sleep 10}}`

- Adja meg a parancsnak az időkorlát lejárta után küldendő jelet. (Alapértelmezés szerint a TERM jelzés kerül elküldésre):

`timeout --signal {{INT}} {{5s}} {{sleep 10}}`
