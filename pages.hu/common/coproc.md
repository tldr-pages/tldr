# coproc

> Bash beépített program interaktív aszinkron alhéjak létrehozására. További információ: <https://www.gnu.org/software/bash/manual/bash.html#Coprocesses>.

- Egy alhéj aszinkron futtatása:

`coproc { {{command1; command2; ...}}; }`

- Hozzon létre egy adott nevű koprocesszt:

`coproc {{name}} { {{command1; command2; ...}}; }`

- Írás egy adott koprocesszbe `stdin`:

`echo "{{input}}" >&"${{{name}}[1]}"`

- Olvasás egy adott koprocesszből `stdout`:

`read {{variable}} <&"${{{name}}[0]}"`

- Hozzon létre egy koprocesszt, amely ismételten beolvassa a `stdin` és lefuttat néhány parancsot a bemeneten:

`coproc {{name}} { while read line; do {{command1; command2; ...}}; done }`

- Létrehozni és használni egy koprocesszt, amely a `bc`:

`coproc BC { bc --mathlib; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
