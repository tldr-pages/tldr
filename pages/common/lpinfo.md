# lpinfo

> List connected printers and installed drivers for the CUPS print server.
> More information: <https://www.cups.org/doc/man-lpinfo.html>.

- List all the currently connected printers:

`lpinfo -v`

- List all the currently installed printer drivers:

`lpinfo -m`

- Search installed printer drivers by make and model:

`lpinfo --make-and-model "{{printer_model}}" -m`
