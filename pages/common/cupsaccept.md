# cupsaccept

> Accept jobs sent to one or more destinations.
> NOTE: destination is referred as a printer or a class of printers.
> See also: `cupsreject`, `cupsenable`, `cupsdisable`, `lpstat`.
> More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Accept print jobs to the specified destinations:

`cupsaccept {{destination1 destination2 ...}}`

- Specify a different server:

`cupsaccept -h {{server}} {{destination1 destination2 ...}}`
