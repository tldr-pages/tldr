# shuf

> Generate random permutations.
> More information: <https://www.unix.com/man-page/linux/1/shuf/>.

- Randomize the order of lines in a file and output the result:

`shuf {{path/to/file}}`

- Only output the first 5 entries of the result:

`shuf --head-count={{5}} {{path/to/file}}`

- Write output to another file:

`shuf {{path/to/file}} --output={{path/to/file}}`

- Generate random numbers in range 1-10:

`shuf --input-range={{1-10}}`
