# cut

> Cut out fields from `stdin` or files.
> More information: <https://keith.github.io/xcode-man-pages/cut.1.html>.

- Print the fifth [c]haracter on each line:

`{{command}} | cut -c 5`

- Print the fifth to tenth [c]haracter of each line of the specified file:

`cut -c 5-10 {{path/to/file}}`

- Split each line in a file by a delimiter into fields and print [f]ields two and six (default delimiter is `TAB`):

`cut -f 2,6 {{path/to/file}}`

- Split each line by the specified [d]elimiter and print all from the second [f]ield onward:

`{{command}} | cut -d "{{delimiter}}" -f 2-`

- Use space as a [d]elimiter and print only the first 3 [f]ields:

`{{command}} | cut -d " " -f -3`
