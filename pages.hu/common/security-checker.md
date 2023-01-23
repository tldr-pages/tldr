# security-checker

> Ellenőrizze, hogy egy PHP-alkalmazás használ-e olyan függőségeket, amelyekben ismert biztonsági rések vannak. További információ: <https://github.com/sensiolabs/security-checker>.

- Biztonsági problémák keresése a projekt függőségeiben (az aktuális könyvtárban található `composer.lock` fájl alapján):

`security-checker security:check`

- Egy adott `composer.lock` fájl használata:

`security-checker security:check {{path/to/composer.lock}}`

- Az eredményeket JSON objektumként adja vissza:

`security-checker security:check --format=json`
