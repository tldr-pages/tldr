# tc

> A forgalomirányítási beállítások megjelenítése/manipulálása. További információ: <https://manned.org/tc>.

- Állandó hálózati késleltetés hozzáadása a kimenő csomagokhoz:

`tc qdisc add dev {{eth0}} root netem delay {{delay_in_milliseconds}}ms`

- Normál elosztott hálózati késleltetés hozzáadása a kimenő csomagokhoz:

`tc qdisc add dev {{eth0}} root netem delay {{mean_delay_ms}}ms {{delay_std_ms}}ms`

- Csomagok egy részéhez korrupció/veszteség/duplikáció hozzáadása:

`tc qdisc add dev {{eth0}} root netem {{corruption|loss|duplication}} {{effect_percentage}}%`

- Sávszélesség, törésszám és maximális késleltetés korlátozása:

`tc qdisc add dev eth0 root tbf rate {{max_bandwith_mb}}mbit burst {{max_burst_rate_kb}}kbit latency {{max_latency_before_drop_ms}}ms`

- Aktív forgalomszabályozási irányelvek megjelenítése:

`tc qdisc show dev {{eth0}}`

- Az összes forgalomszabályozási szabály törlése:

`tc qdisc del dev {{eth0}}`

- Forgalomszabályozási szabály módosítása:

`tc qdisc change dev {{eth0}} root netem {{policy}} {{policy_parameters}}`
