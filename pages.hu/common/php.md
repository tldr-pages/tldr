# php

> PHP parancssori felület. További információ: <https://php.net>.

- PHP-szkript elemzése és végrehajtása:

`php {{path/to/file}}`

- Egy PHP-szkript szintaxisának ellenőrzése (azaz lint):

`php -l {{path/to/file}}`

- A PHP interaktív futtatása:

`php -a`

- PHP-kód futtatása (Megjegyzések: Ne használjon <? ?> címkéket; a kettős idézőjeleket backslash-szel szüntesse meg):

`php -r "{{code}}"`

- PHP beépített webkiszolgáló indítása az aktuális könyvtárban:

`php -S {{host:port}}`

- A telepített PHP-bővítmények listájának lekérdezése:

`php -m`

- Információk megjelenítése az aktuális PHP-konfigurációról:

`php -i`

- Információk megjelenítése egy adott funkcióról:

`php --rf {{function_name}}`
