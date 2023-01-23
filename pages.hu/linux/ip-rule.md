# ip rule

> IP útválasztási irányelvek adatbázisának kezelése. További információ: <https://man7.org/linux/man-pages/man8/ip-rule.8.html>.

- Az útválasztási házirend megjelenítése:

`ip rule {{show|list}}`

- Új szabály hozzáadása a csomagok forráscímei alapján:

`sudo ip rule add from {{192.168.178.2/32}}`

- Új szabály hozzáadása a csomagok célcímei alapján:

`sudo ip rule add to {{192.168.178.2/32}}`

- Szabály törlése a csomagok forráscímei alapján:

`sudo ip rule delete from {{192.168.178.2/32}}`

- Csomagok célcímén alapuló szabály törlése:

`sudo ip rule delete to {{192.168.178.2/32}}`

- Az összes törölt szabály törlése:

`ip rule flush`

- Az összes szabály mentése egy fájlba:

`ip rule save > {{path/to/ip_rules.dat}}`

- Az összes szabály visszaállítása fájlból:

`ip rule restore < {{path/to/ip_rules.dat}}`
