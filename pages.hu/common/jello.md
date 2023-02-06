# jello

> A Python szintaxist használó parancssori JSON-feldolgozó. További információ: <https://github.com/kellyjonbrazil/jello>.

- JSON vagy JSON-soros adatok szépen nyomtatása a `stdin` és a `stdout` között:

`cat {{file.json}} | jello`

- A JSON vagy JSON Lines adatok sémájának kiadása a `stdin` és a `stdout` között (hasznos a grep számára):

`cat {{file.json}} | jello -s`

- JSON vagy JSON-Lines adatok összes elemének (vagy objektumok összes értékének) kimenete a `stdin` és `stdout` közötti JSON vagy JSON-Lines adatokban:

`cat {{file.json}} | jello -l`

- Az első elem kimenete a JSON vagy JSON-Lines adatokban a `stdin` és a `stdout` között:

`cat {{file.json}} | jello _[0]`

- A JSON vagy JSON-Lines adatok minden egyes elemének adott kulcsának értékének kiadása a `stdin` és a `stdout` között:

`cat {{file.json}} | jello '[i.{{key_name}} for i in _]'`

- Több kulcs értékének új JSON-objektumként történő kiadása (feltételezve, hogy a bemeneti JSON tartalmazza a `key_name` és a `other_key_name` kulcsokat):

`cat {{file.json}} | jello '{"{{my_new_key}}": _.{{key_name}}, "{{my_other_key}}": _.{{other_key_name}}}'`

- Egy adott kulcs értékének stringként történő kiadása (és a JSON-kimenet letiltása):

`cat {{file.json}} | jello -r '"{{some text}}: " + _.{{key_name}}'`
