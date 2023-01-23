# cewl

> URL pókhálósító eszköz, amellyel webes tartalmakból készíthetünk tördelő szólistát. További információ: <https://digi.ninja/projects/cewl.php>.

- Szólista fájl létrehozása a megadott URL-ből 2 link mélységig:

`cewl --depth {{2}} --write {{path/to/wordlist.txt}} {{url}}`

- Kibocsát egy alfanumerikus szólistát az adott URL-ből, legalább 5 karakteres szavakkal:

`cewl --with-numbers --min_word_length {{5}} {{url}}`

- Szólista kimenete az adott URL-ből hibakeresési módban, beleértve az e-mail címeket is:

`cewl --debug --email {{url}}`

- Szólista kimenete az adott URL-címről HTTP Basic vagy Digest hitelesítéssel:

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- Szólista kiadása az adott URL-címről proxy-n keresztül:

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`
