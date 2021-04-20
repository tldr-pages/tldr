# fold

> Wraps each line in an input file to fit a specified width and prints it to the standard output.
> More information: <https://www.gnu.org/software/coreutils/fold>.

- Wrap each line to default width (80 characters):

`fold {{file}}`

- Wrap each line to width "30":

`fold -w30 {{file}}`

- Wrap each line to width "5" and break the line at spaces (puts each space separated word in a new line, words with length > 5 are wrapped):

`fold -w5 -s {{file}}`
