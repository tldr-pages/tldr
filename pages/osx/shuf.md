# shuf

> Generate random permutations.
> More information: <https://www.unix.com/man-page/linux/1/shuf/>.

- Randomize the order of lines in a file and output the result:

`shuf {{filename}}`

- Only output the first 5 entries of the result:

`shuf --head-count={{5}} {{filename}}`

- Write output to another file:

`shuf {{filename}} --output={{output_filename}}`

- Generate random numbers in range 1-10:

`shuf --input-range={{1-10}}`
