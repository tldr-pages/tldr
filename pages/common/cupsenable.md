# cupsenable

> Start printers and classes.
> NOTE: destination is referred as a printer or a class of printers.
> See also: `cupsdisable`, `cupsaccept`, `cupsreject`, `lpstat`.
> More information: <https://www.cups.org/doc/man-cupsenable.html>.

- Start one or more destination(s):

`cupsenable {{destination1 destination2 ...}}`

- Resume printing of pending jobs of a destination (use after `cupsdisable` with `--hold`):

`cupsenable --release {{destination}}`

- Cancel all jobs of the specified destination(s):

`cupsenable -c {{destination1 destination2 ...}}`
