# lp

> print files

- List printers present on the machine.

`lpstat -p | awk '{print $2}`

- List the default printer.

`lpstat -d`

- Print the output of a command.

`echo "test" | lp -d {{printer_name}}`

- Print to the default printer.

`lpstat {{filename}}`

- Print a file to a named printer. 

`lp -d {{printer_name}} {{path/to/filename}}`

- Print N copies to default printer (example used is 2).

`lp -n 2 {{path/to/filename}}`

- Print only certain pages to the default printer -m is not necessary in this case (print pages 1, 3-5, and 16).

`lp -P 1,3-5,16 {{path/to/filename}}`
