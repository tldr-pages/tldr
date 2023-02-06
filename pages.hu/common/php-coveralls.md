# php-coveralls

> PHP kliens a Coveralls-hoz. További információ: <https://php-coveralls.github.io/php-coveralls>.

- Küldje el a lefedettségi információkat a Coverallsnak:

`php-coveralls`

- Fedettségi információk küldése a Coverallsnak egy adott könyvtárhoz:

`php-coveralls --root_dir {{path/to/directory}}`

- Fedettségi információk küldése a Coverallsnak egy adott konfigurációval:

`php-coveralls --config {{path/to/.coveralls.yml}}`

- Fedettségi információk küldése a Coverallsnak verbózus kimenettel:

`php-coveralls --verbose`

- Fedettségi információk küldése a Coverallsnak a futtatható utasításokkal nem rendelkező forrásfájlok kivételével:

`php-coveralls --exclude-no-stmt`

- Coverall-nak lefedettségi információk küldése egy adott környezetnévvel:

`php-coveralls --env {{test|dev|prod}}`

- Több Coverage Clover XML fájl megadása a feltöltéshez:

`php-coveralls --coverage_clover {{path/to/first_clover.xml}} --coverage_clover {{path/to/second_clover.xml}}`

- A Coverallsnak küldendő JSON kimenete egy adott fájlba:

`php-coveralls --json_path {{path/to/coveralls-upload.json}}`
