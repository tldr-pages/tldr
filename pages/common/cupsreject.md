# cupsreject

> Reject jobs sent to printers.
> Note: destination is referred as a printer or a class of printers.
> See also: `cupsaccept`, `cupsenable`, `cupsdisable`, `lpstat`.
> More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Reject print jobs to the specified destinations:

`cupsreject {{destination1 destination2 ...}}`

- Specify a different server:

`cupsreject -h {{server}} {{destination1 destination2 ...}}`

- Specify a reason string ("Reason Unknown" by default):

`cupsreject -r {{reason}} {{destination1 destination2 ...}}`
