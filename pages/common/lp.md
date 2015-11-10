# lp

> print files

- List printers present on the machine.

`lpstat -p | awk '{print $2}`

- Print the output of a command to the default printer.

`echo "test" | lp`

- Print a file to the default printer.

`lpstat {{filename}}`

- Print a file to a named printer. 

`lp -d {{printer_name}} {{path/to/filename}}`

- Print N copies of file to default printer (replace N with desired number of copies).

`lp -n {{N}} {{path/to/filename}}`

- Print only certain pages to the default printer (print pages 1, 3-5, and 16).

`lp -P 1,3-5,16 {{path/to/filename}}`
