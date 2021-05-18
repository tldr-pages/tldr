# shuf

> Generate random permutations.
> More information: <https://www.gnu.org/software/coreutils/shuf>.

- Randomize the order of lines in a file and output the result:

`shuf {{filename}}`

- Only output the first 5 entries of the result:

`shuf -n {{5}} {{filename}}`

- Write the output to another file:

`shuf {{filename}} -o {{output_filename}}`

- Generate 3 random numbers in the range 1-10:

`shuf -n {{3}} -i {{1-10}}`
