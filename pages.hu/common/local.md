# local

> Helyi változók deklarálása és attribútumok megadása. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Egy string változó deklarálása a megadott értékkel:

`local {{variable}}="{{value}}"`

- Egész szám változó deklarálása a megadott értékkel:

`local -i {{variable}}="{{value}}"`

- Tömbváltozó deklarálása a megadott értékkel:

`local {{variable}}=({{item_a item_b item_c}})`

- Asszociatív tömbváltozó deklarálása a megadott értékkel:

`local -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Readonly változó deklarálása a megadott értékkel:

`local -r {{variable}}="{{value}}"`
