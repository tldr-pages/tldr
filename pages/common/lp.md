# lp

> print files.

- List the default printer.  See tldr lpstat for more lpstat commands.

`lpstat -d`

- Print to the default printer.

`lp {{filename}}`

- Print a file to a named printer. 

`lp -d {{printer_name}} {{path/to/filename}}`

- Print the output of a command.

`echo "test" | lp -d {{printer_name}}`

- Print N copies to default printer.

`lp -n {{N}} {{path/to/filename}}`

- Print only certain pages to the default printer (print pages 1, 3-5, and 16).

`lp -P 1,3-5,16 {{path/to/filename}}`
