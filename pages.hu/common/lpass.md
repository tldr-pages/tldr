# lpass

> Parancssori felület a LastPass jelszókezelőhöz. További információ: <https://github.com/lastpass/lastpass-cli>.

- Jelentkezzen be a LastPass-fiókjába a fő jelszó megadásával, amikor erre felszólítják:

`lpass login {{username}}`

- Bejelentkezési állapot megjelenítése:

`lpass status`

- Az összes webhely kategóriák szerinti csoportosításban történő felsorolása:

`lpass ls`

- Generáljon új jelszót a gmail.com-hoz a `myinbox` azonosítóval, és adja hozzá a LastPass-hoz:

`lpass generate --username {{username}} --url {{gmail.com}} {{myinbox}} {{password_length}}`

- Jelszó megjelenítése egy megadott bejegyzéshez:

`lpass show {{myinbox}} --password`
