# lpq

> Show printer queue status.
> More information: <https://openprinting.github.io/cups/doc/man-lpq.html>.

- Show the queued jobs of the default destination:

`lpq`

- Show the queued jobs of all printers enforcing encryption:

`lpq -a -E`

- Show the queued jobs in a long format:

`lpq -l`

- Show the queued jobs of a specific printer or class:

`lpq -P {{destination[/instance]}}`

- Show the queued jobs once every n seconds until the queue is empty:

`lpq +{{interval}}`
