# shuf

> Generate random permutations.
> More information: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- Randomize the order of lines in a file and output the result:

`shuf {{path/to/file}}`

- Only output the first 5 entries of the result:

`shuf --head-count=5 {{path/to/file}}`

- Write output to another file:

`shuf {{path/to/input_file}} --output={{ath/to/output_file}}`

- Generate random numbers in the range 1 to 10:

`shuf --input-range=1-10`
