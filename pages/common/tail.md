# tail

> Display the last part of a file.
> More information: <https://www.gnu.org/software/coreutils/tail>.

- Show last 'num' lines in file:

`tail -n {{num}} {{file}}`

- Show all file since line 'num':

`tail -n +{{num}} {{file}}`

- Show last 'num' bytes in file:

`tail -c {{num}} {{file}}`

- Keep reading file until `Ctrl + C`:

`tail -f {{file}}`

- Keep reading file until `Ctrl + C`, even if the file is rotated:

`tail -F {{file}}`

- Show last 'num' lines in 'file' and refresh every 'n' seconds:

`tail -n {{num}} -s {{n}} -f {{file}}`
