# cake

> A CakePHP keretrendszer parancssori processzora. További információ: <https://cakephp.org>.

- Alapvető információk megjelenítése az aktuális alkalmazásról és az elérhető parancsokról:

`cake`

- Az elérhető útvonalak listájának megjelenítése:

`cake routes`

- Konfigurációs gyorsítótárak törlése:

`cake cache clear_all`

- A metaadatok gyorsítótárának felépítése:

`cake schema_cache build --connection {{connection}}`

- A metaadatok gyorsítótárának törlése:

`cake schema_cache clear`

- Egyetlen gyorsítótár tábla törlése:

`cake schema_cache clear {{table_name}}`

- Fejlesztői webkiszolgáló indítása (alapértelmezés szerint a 8765-ös porton):

`cake server`

- REPL (interaktív shell) indítása:

`cake console`
