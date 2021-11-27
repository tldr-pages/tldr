# for

> Conditionally perform a command several times.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Iterate over range:

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{commands}}; done`

- Iterate over files:

`for {{variable}} in *; do {{commands}}; done`

- Iterate over directories:

`for {{variable}} in */; do {{commands}}; done`

- Perform a command with different arguments:

`for {{variable}} in {{arguments}}; do {{command}} "${{variable}}"; done`

- Perform a command in every directory:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{command}}) done`
