# coproc

> BASH builtin for creating interactive asynchronous subshells.
> More information: https://www.gnu.org/software/bash/manual/bash.html#Coprocesses

- Run a command asynchronously:

`coproc { {{command}}; }`

- Create a named coprocess:

`coproc {{name}} { {{command}}; }`

- Write to a named coprocess stdin:

`echo "{{input}}" >&"${{{name}}[1]}"`

- Read from a named coprocess stdout:

`read {{variable}} <&"${{{name}}[0]}"`

- Create a coprocess which repeatedly reads stdin, and runs some commands on the input:

`coproc {{name}} {  while read line; do {{commands}}; done }`

- Create a coprocess which repeatedly reads stdin, runs a pipeline on the input, and writes the output to stdout:

`coproc {{name}} { while read line; do echo "$line" | {{commands}} | cat /dev/fd/0; done }`

- Create and use a coprocess running `bc`:

`coproc BC { bc -l; }; echo "1/3" >&"${BC[1]}"; read output <&"${BC[0]}"; echo "$output"`
