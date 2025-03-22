# local

> Declare local variables and give them attributes.
> See also: `declare`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-local>.

- Declare a string variable with the specified value:

`local {{variable}}="{{value}}"`

- Declare an integer variable with the specified value:

`local -i {{variable}}="{{value}}"`

- Declare an array variable with the specified value:

`local {{variable}}=({{item_a item_b item_c}})`

- Declare an associative array variable with the specified value:

`local -A {{variable}}=({{[key_a]=item_a [key_b]=item_b [key_c]=item_c}})`

- Declare a readonly variable with the specified value:

`local -r {{variable}}="{{value}}"`

- Display help:

`local --help`
