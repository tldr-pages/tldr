# choose

> A human-friendly and fast alternative to cut and (sometimes) awk
> More information: <https://github.com/theryangeary/choose>.

- Print the 5th item from a line (zero indexed):
`choose 5`

- Print the 0th, 3rd, and 5th item from a line, where items are separated by ':' instead of whitespace:

`choose -f ':' 0 3 5`

- Print everything from the 2nd to 5th item on the line, inclusive of the 5th:

`choose 2:5`

- print everything from the 2nd to 5th item on the line, exclusive of the 5th:

`choose -x 2:5`

- Print the beginning of the line to the 3rd item:

`choose :3`

- print the beginning of the line to the 3rd item, exclusive:

`choose -x :3`

- Print the third item to the end of the line:

`choose 3:`

- Print the last item from a line

`choose -1`
