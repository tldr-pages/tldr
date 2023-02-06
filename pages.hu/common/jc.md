# jc

> Egy segédprogram több parancs kimenetének JSON-ba való átalakítására. További információ: <https://github.com/kellyjonbrazil/jc>.

- Parancsok kimenetének átalakítása JSON-ba pipe-on keresztül:

`{{ifconfig}} | jc {{--ifconfig}}`

- A parancsok kimenetének átalakítása JSON-ba varázslatos szintaxissal:

`jc {{ifconfig}}`

- Szép JSON kimenet pipán keresztül:

`{{ifconfig}} | jc {{--ifconfig}} -p`

- Szép JSON kiadása mágikus szintaxissal:

`jc -p {{ifconfig}}`
