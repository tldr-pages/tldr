# phpenv

> PHP verziókezelő fejlesztői célokra. További információ: <https://github.com/phpenv/phpenv>.

- A PHP verzió globális telepítése:

`phpenv install {{version}}`

- Frissítse a shim fájlokat a `phpenv` oldalon ismert összes PHP binárishoz:

`phpenv rehash`

- Az összes telepített PHP-verzió listázása:

`phpenv versions`

- Az aktuálisan aktív PHP-verzió megjelenítése:

`phpenv version`

- A globális PHP-verzió beállítása:

`phpenv global {{version}}`

- A helyi PHP-verzió beállítása, amely felülírja a globális verziót:

`phpenv local {{version}}`

- A helyi PHP-verzió visszaállítása:

`phpenv local --unset`
