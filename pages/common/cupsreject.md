# cupsreject

> Reject jobs sent to one or more printers.
> See also: `cupsaccept`.
> More information: <https://www.cups.org/doc/man-cupsaccept.html>.

- Reject print jobs to the specified destinations:

`cupsaccept {{destination1 destination2 ...}}`

- Specify a reason string ("Reason Unknown" by default):

`cupsaccept -r {{reason}} {{destination1 destination2 ...}}`
