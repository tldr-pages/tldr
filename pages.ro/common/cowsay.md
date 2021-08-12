# cowsay

> Print ASCII art (în mod implicit o vacă) spunând sau de gândire ceva.
> Mai multe informaţii: <https://github.com/tnalpgge/rank-amateur-cowsay>

- Imprimați o vacă ASCII spunând „salut, lume”:

`cowsay "{{hello, world}}"`

- Imprimați o vacă ASCII spunând text de la stdin:

`echo "{{hello, world}}" | cowsay`

- Listează toate tipurile de artă disponibile:

`cowsay -l`

- Imprima arta ASCII specificată spunând „salut, lume”:

`cowsay -f {{art}} "{{hello, world}}"`

- Imprima o vacă de gândire mort ASCII:

`cowthink -d "{{I'm just a cow, not a great thinker...}}"`

- Imprima o vaca ASCII cu ochii personalizati spunând „salut, lume”:

`cowsay -e {{characters}} "{{hello, world}}"`
