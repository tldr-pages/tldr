# declare

> Declareer variabelen en geef ze attributen.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-declare>.

- Declareer een string variabele met de gespecificeerde waarde:

`declare {{variabele}}="{{waarde}}"`

- Declareer een integer variabele met de gespecificeerde waarde:

`declare -i {{variabele}}="{{waarde}}"`

- Declareer een array variabele met de gespecificeerde waarde:

`declare -a {{variabele}}=({{item_a item_b item_c}})`

- Declareer een associatieve array variabele met de gespecificeerde waarde:

`declare -A {{variabele}}=({{[sleutel_a]=item_a [sleutel_b]=item_b [sleutel_c]=item_c}})`

- Declareer a readonly string variabele met de gespecificeerde waarde:

`declare -r {{variabele}}="{{waarde}}"`

- Declareer een globale variabele binnen een functie met de gespecificeerde waarde:

`declare -g {{variabele}}="{{waarde}}"`

- Print een functie-definitie:

`declare -f {{functie_naam}}`

- Print een variabele-definitie:

`declare -p {{variabele_naam}}`
