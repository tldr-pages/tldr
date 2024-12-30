# declare

> Declareer variabelen en geef ze attributen.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Declareer een string variable met de gespecificeerde waarde:

`declare {{variable}}="{{waarde}}"`

- Declareer een integer variable met de gespecificeerde waarde:

`declare -i {{variable}}="{{waarde}}"`

- Declareer een array variable met de gespecificeerde waarde:

`declare -a {{variable}}=({{item_a item_b item_c}})`

- Declareer een associatieve array variable met de gespecificeerde waarde:

`declare -A {{variable}}=({{[sleutel_a]=item_a [sleutel_b]=item_b [sleutel_c]=item_c}})`

- Declareer a readonly string variable met de gespecificeerde waarde:

`declare -r {{variable}}="{{waarde}}"`

- Declareer een globale variable binnen een functie met de gespecificeerde waarde:

`declare -g {{variable}}="{{waarde}}"`
