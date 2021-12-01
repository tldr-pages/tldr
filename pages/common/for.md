# for

> Conditionally perform a command several times.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Iterate over range:

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do echo "Variable {{variable}} is ${{variable}} now"; done`

- Iterate over files:

`for {{variable}} in *; do echo "Variable {{variable}} is ${{variable}} now"; done`

- Iterate over directories:

`for {{variable}} in */; do echo "Variable {{variable}} is ${{variable}} now"; done`

- Perform a command in every directory:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{command}}) done`
