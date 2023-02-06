# mandb

> Az előre formázott kézikönyvoldalak adatbázisának kezelése. További információ: <https://man7.org/linux/man-pages/man8/mandb.8.html>.

- Kézikönyvoldalak törlése és feldolgozása:

`mandb`

- Egyetlen bejegyzés frissítése:

`mandb --filename {{path/to/file}}`

- Frissítés helyett bejegyzéseket hozhat létre a semmiből:

`mandb --create`

- Csak felhasználói adatbázisok feldolgozása:

`mandb --user-db`

- Ne törölje az elavult bejegyzéseket:

`mandb --no-purge`

- A kézikönyvoldalak érvényességének ellenőrzése:

`mandb --test`
