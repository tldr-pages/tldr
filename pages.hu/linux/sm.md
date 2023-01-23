# sm

> Rövid üzenet megjelenítése teljes képernyőn. További információ: <https://github.com/nomeata/screen-message>.

- Üzenet megjelenítése teljes képernyőn:

`sm "{{Hello World!}}"`

- Üzenet megjelenítése invertált színekkel:

`sm -i "{{Hello World!}}"`

- Üzenet megjelenítése egyéni előtérszínnel:

`sm -f {{blue}} "{{Hello World!}}"`

- Üzenet megjelenítése egyéni háttérszínnel:

`sm -b {{#008888}} "{{Hello World!}}"`

- Üzenet megjelenítése 3-szor elforgatva (90 fokos lépésekben, az óramutató járásával ellentétesen):

`sm -r {{3}} "{{Hello World!}}"`

- Üzenet megjelenítése egy másik parancs kimenetének felhasználásával:

`{{echo "Hello World!"}} | sm -`
