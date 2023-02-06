# top

> Dinamikus valós idejű információk megjelenítése a futó folyamatokról. További információ: <https://manned.org/top>.

- Start top:

`top`

- Ne jelenítsen meg üresjárati vagy zombi-folyamatokat:

`top -i`

- Csak az adott felhasználó tulajdonában lévő folyamatok megjelenítése:

`top -u {{username}}`

- Rendezze a folyamatokat egy mező alapján:

`top -o {{field_name}}`

- Egy adott folyamat egyes szálainak megjelenítése:

`top -Hp {{process_id}}`

- Csak a megadott PID(ek)-kel rendelkező folyamatok megjelenítése, vesszővel elválasztott listaként átadva. (Normális esetben a PID-eket nem tudod kézből. Ez a példa a folyamat nevéből választja ki a PID-eket):

`top -p $(pgrep -d ',' {{process_name}})`

- Segítség kérése az interaktív parancsokhoz:

`?`
