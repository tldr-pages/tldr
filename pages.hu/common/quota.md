# quota

> A felhasználók lemezterület-használatának és a kiosztott korlátoknak a megjelenítése. További információ: <https://manned.org/quota>.

- Lemezkvóták megjelenítése az aktuális felhasználó számára ember által olvasható egységekben:

`quota -s`

- Verbózus kimenet (olyan fájlrendszerek kvótáinak megjelenítése is, ahol nincs kiosztott tárhely):

`quota -v`

- Csendes kimenet (csak azokon a fájlrendszereken jeleníti meg a kvótákat, ahol a használat meghaladja a kvótát):

`quota -q`

- Kvóták nyomtatása azon csoportok számára, amelyeknek az aktuális felhasználó tagja:

`quota -g`

- Lemezkvóták megjelenítése egy másik felhasználó számára:

`sudo quota -u {{username}}`
