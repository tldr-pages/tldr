# shuf

> Generate random permutations.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/shuf-invocation.html>.

- Randomize the order of lines in a file and output the result:

`shuf {{path/to/file}}`

- Only output the first 5 entries of the result:

`shuf {{[-n|--head-count]}} 5 {{path/to/file}}`

- Write the output to another file:

`shuf {{path/to/input_file}} {{[-o|--output]}} {{path/to/output_file}}`

- Generate 3 random numbers in the range 1-10 (inclusive):

`shuf {{[-n|--head-count]}} 3 {{[-i|--input-range]}} 1-10 {{[-r|--repeat]}}`
