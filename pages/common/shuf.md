# shuf

> Generate random permutations.
> More information: <https://www.gnu.org/software/coreutils/shuf>.

- Randomize the order of lines in a file and output the result:

`shuf {{path/to/file}}`

- Only output the first 5 entries of the result:

`shuf --head-count={{5}} {{path/to/file}}`

- Write the output to another file:

`shuf {{path/to/input}} --output={{path/to/output}}`

- Generate 3 random numbers in the range 1-10 (inclusive):

`shuf --head-count={{3}} --input-range={{1-10}} --repeat`
