# lpadmin

> Configure cups printers and classes.
> See also: `lpoptions`.
> More information: <https://www.cups.org/doc/man-lpadmin.html>.

- Set the default printer:

`lpadmin -d {{printer}}`

- [d]elete a specific printer or class:

`lpadmin -x {{printer|class}}`

- Add a printer to a [c]lass:

`lpadmin -p {{printer}} -c {{class}}`

- [r]emove a printer from a class:

`lpadmin -p {{printer}} -r {{class}}`
