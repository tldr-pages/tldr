# for

> Conditionally perform a command several times.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Looping-Constructs>.

- Execute given commands for the specified set:

`for {{variable}} in {{item_a item_b item_c}}; do {{echo "Loop is executed"}}; done`

- Iterate over a given range of numbers:

`for {{variable}} in {{{from}}..{{to}}..{{step}}}; do {{echo "Loop is executed"}}; done`

- Iterate over a given list of files:

`for {{variable}} in {{file_a.ext file_b.ext file_c.ext}}; do {{echo "Loop is executed"}}; done`

- Iterate over a given list of directories:

`for {{variable}} in {{directory_a/ directory_b/ directory_c/}}; do {{echo "Loop is executed"}}; done`

- Perform a given command in every directory:

`for {{variable}} in */; do (cd "${{variable}}" || continue; {{echo "Loop is executed"}}) done`
