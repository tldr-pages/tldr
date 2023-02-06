# typeset

> Változók deklarálása és attribútumok megadása. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Bash-Builtins>.

- Egy string változó deklarálása a megadott értékkel:

`typeset {{variable}}="{{value}}"`

- Egész szám változó deklarálása a megadott értékkel:

`typeset -i {{variable}}="{{value}}"`

- Tömbváltozó deklarálása a megadott értékkel:

`typeset {{variable}}=({{item_a item_b item_c}})`

- Asszociatív tömbváltozó deklarálása a megadott értékkel:

`typeset -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Readonly változó deklarálása a megadott értékkel:

`typeset -r {{variable}}="{{value}}"`

- Globális változó deklarálása függvényen belül a megadott értékkel:

`typeset -g {{variable}}="{{value}}"`
