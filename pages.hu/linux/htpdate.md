# htpdate

> A helyi dátum és idő szinkronizálása a webkiszolgálók HTTP fejlécein keresztül. További információ: <http://www.vervest.org/htp/>.

- A dátum és az idő szinkronizálása:

`sudo htpdate {{host}}`

- A szinkronizálás szimulációjának végrehajtása, mindenféle művelet nélkül:

`htpdate -q {{host}}`

- Kompenzálja a szisztematikus óraeltolódást:

`sudo htpdate -x {{host}}`

- Állítsa be az időt közvetlenül a szinkronizálás után:

`sudo htpdate -s {{host}}`
