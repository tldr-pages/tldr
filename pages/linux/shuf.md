# shuf

> generate random permutations

- randomize the order of lines in a file and output the result

`shuf {{filename}}`

- only output the first n entries of the result

`shuf -n {{n}} {{filename}}`

- write output to another file

`shuf -o {{another_filename}} {{filename}}`

- generate random numbers in range

`shuf -i {{low}}-{{high}}`
