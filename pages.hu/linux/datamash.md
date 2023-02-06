# datamash

> Alapvető numerikus, szöveges és statisztikai műveletek elvégzésére szolgáló eszköz szöveges adatfájlokon. További információ: <http://www.gnu.org/software/datamash/>.

- Egyetlen számoszlop maximumának, minimumának, átlagának és mediánjának lekérdezése:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- A lebegőszámok egyetlen oszlopának átlagának lekérdezése (a lebegőszámoknak "," és nem "." karaktert kell használniuk):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- Egyetlen számoszlop átlagának kinyerése adott tizedes pontossággal:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R {{number_of_decimals_wanted}} mean 1`

- Egyetlen számoszlop átlagának kinyerése a "Na" és "NaN" (szó szerinti) karakterláncok figyelmen kívül hagyásával:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
