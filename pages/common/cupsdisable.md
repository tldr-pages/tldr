# cupsdisable

> Stop printers and classes.
> NOTE: destination is referred as a printer or a class of printers.
> See also: `cupsenable`, `cupsaccept`, `cupsreject`, `lpstat`.
> More information: <https://openprinting.github.io/cups/doc/man-cupsenable.html>.

- Stop one or more destination(s):

`cupsdisable {{destination1 destination2 ...}}`

- Cancel all jobs of the specified destination(s):

`cupsdisable -c {{destination1 destination2 ...}}`
