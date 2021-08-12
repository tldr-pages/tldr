# read

> BASH builtin pentru regăsirea datelor din intrarea standard.

- Stocați datele pe care le tastați de la tastatură:

`read {{variable}}`

- Stocați fiecare dintre liniile următoare pe care le introduceți ca valori ale unui tablou:

`read -a {{array}}`

- Specificați numărul de caractere maxime care trebuie citite:

`read -n {{character_count}} {{variable}}`

- Utilizați un caracter specific ca delimitator în loc de o linie nouă:

`read -d {{new_delimiter}} {{variable}}`

- Nu lăsați backslash (\) să acționeze ca un personaj de evadare:

`read -r {{variable}}`

- Afișați un prompt înainte de intrare:

`read -p "{{Enter your input here: }}" {{variable}}`

- Nu ecou caractere tastate (modul silențios):

`read -s {{variable}}`

- Citiți stdin și efectuați o acțiune pe fiecare linie:

`while read line; do echo "$line"; done`
