# coproc

> Bash ingebouwd commando voor het maken van interactieve asynchrone subshells.
> Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- Voer een subshell asynchroon uit:

`coproc { {{commando1; commando2; ...}}; }`

- Maak een coprocess met een specifieke naam:

`coproc {{naam}} { {{commando1; commando2; ...}}; }`

- Schrijf naar de `stdin` van een specifiek coprocess:

`echo "{{invoer}}" >&"${{{naam}}[1]}"`

- Lees van de `stdout` van een specifiek coprocess:

`read {{variabele}} <&"${{{naam}}[0]}"`

- Maak een coprocess dat herhaaldelijk `stdin` leest en opdrachten op de invoer uitvoert:

`coproc {{naam}} { while read line; do {{commando1; commando2; ...}}; done }`

- Maak een coprocess dat herhaaldelijk `stdin` leest, voert een pipeline uit op de input en schrijf de output naar `stdout`:

`coproc {{naam}} { while read line; do echo "$line" | {{commando1 | commando2 | ...}} | cat /dev/fd/0; done }`

- Maak en gebruik een coprocess dat `bc` uitvoert:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
