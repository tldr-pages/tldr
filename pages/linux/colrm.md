# colrm

> Remove columns from stdin.
> More information: <https://github.com/karelzak/util-linux>.

- Remove first column of stdin:

`colrm {{1 1}}`

- Remove from 3rd column till the end of each line:

`colrm {{3}}`

- Remove from the 3rd column till the 5th column of each line:

`colrm {{3 5}}`
