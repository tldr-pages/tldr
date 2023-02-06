# lastb

> Az utoljára bejelentkezett felhasználók listájának megjelenítése. További információ: <https://manned.org/lastb>.

- A legutóbb bejelentkezett felhasználók listájának megjelenítése:

`sudo lastb`

- Az összes utoljára bejelentkezett felhasználó listájának megjelenítése egy adott időpont óta:

`sudo lastb --since {{YYYY-MM-DD}}`

- Az összes utoljára bejelentkezett felhasználó listájának megjelenítése egy adott időpontig:

`sudo lastb --until {{YYYY-MM-DD}}`

- Egy adott időpontban bejelentkezett felhasználók listájának megjelenítése:

`sudo lastb --present {{hh:mm}}`

- Az összes utoljára bejelentkezett felhasználó listájának megjelenítése és az IP-nek hostnévre való lefordítása:

`sudo lastb --dns`
