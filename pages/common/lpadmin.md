# lpadmin

> Configure CUPS printers and classes.
> See also: `lpoptions`.
> More information: <https://www.cups.org/doc/man-lpadmin.html>.

- Set the default printer:

`lpadmin -d {{printer}}`

- Delete a specific printer or class:

`lpadmin -x {{printer|class}}`

- Add a printer to a class:

`lpadmin -p {{printer}} -c {{class}}`

- Remove a printer from a class:

`lpadmin -p {{printer}} -r {{class}}`
