# shuf

> Generate random permutations.

- Randomize the order of lines in a file and output the result:

`shuf {{filename}}`

- Only output the first n entries of the result:

`shuf -n {{n}} {{filename}}`

- Write output to another file:

`shuf -o {{another_filename}} {{filename}}`

- Generate random numbers in range:

`shuf -i {{low}}-{{high}}`
