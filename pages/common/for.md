# for

> Conditionally perform a command several times.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Execute the specified commands for the specified set:

`for {{variable}} in item_a item_b item_c; do {{echo "Loop is executed"}}; done`

- Iterate over range:

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "Loop is executed"}}; done`

- Iterate over files:

`for {{variable}} in *; do {{echo "Loop is executed"}}; done`

- Iterate over directories:

`for {{variable}} in */; do {{echo "Loop is executed"}}; done`

- Perform a command in every directory:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "Loop is executed"}}) done`
