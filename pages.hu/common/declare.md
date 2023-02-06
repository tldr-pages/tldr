# declare

> Változók deklarálása és attribútumok megadása. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Egy string változó deklarálása a megadott értékkel:

`declare {{variable}}="{{value}}"`

- Egész szám változó deklarálása a megadott értékkel:

`declare -i {{variable}}="{{value}}"`

- Tömbváltozó deklarálása a megadott értékkel:

`declare -a {{variable}}=({{item_a item_b item_c}})`

- Asszociatív tömbváltozó deklarálása a megadott értékkel:

`declare -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Readonly string változó deklarálása a megadott értékkel:

`declare -r {{variable}}="{{value}}"`

- Globális változó deklarálása függvényen belül a megadott értékkel:

`declare -g {{variable}}="{{value}}"`
