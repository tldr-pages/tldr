# PHP-CS-Fixer

> Automatikus kódolási stílusjavító PHP-hez. További információ: <https://github.com/FriendsOfPHP/PHP-CS-Fixer>.

- Kódolási stílusjavítás végrehajtása az aktuális könyvtárban:

`php-cs-fixer fix`

- Kódstílusjavítás végrehajtása egy adott könyvtárban:

`php-cs-fixer fix {{path/to/directory}}`

- Kódstílus-szűrés végrehajtása változtatások alkalmazása nélkül:

`php-cs-fixer fix --dry-run`

- Kódstílusjavítás végrehajtása meghatározott szabályok alapján:

`php-cs-fixer fix --rules={{rules}}`

- Az alkalmazott szabályok megjelenítése:

`php-cs-fixer fix --verbose`

- Az eredmények más formátumban történő kiadása:

`php-cs-fixer fix --format={{txt|json|xml|checkstyle|junit|gitlab}}`

- A javítást igénylő fájlok megjelenítése:

`php-cs-fixer list-files`

- Szabály vagy szabálykészlet leírása:

`php-cs-fixer describe {{rule}}`
