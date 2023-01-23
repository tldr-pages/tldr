# phpquery

> PHP kiterjesztéskezelő Debian-alapú operációs rendszerekhez. További információ: <https://helpmanual.io/help/phpquery/>.

- Az elérhető PHP-verziók listája:

`sudo phpquery -V`

- Az elérhető SAPI-k listája a PHP 7.3-hoz:

`sudo phpquery -v {{7.3}} -S`

- A PHP 7.3 engedélyezett bővítményeinek listája a cli SAPI-val:

`sudo phpquery -v {{7.3}} -s {{cli}} -M`

- Ellenőrizze, hogy a JSON kiterjesztés engedélyezve van-e a PHP 7.3 számára az apache2 SAPI-val:

`sudo phpquery -v {{7.3}} -s {{apache2}} -m {{json}}`
