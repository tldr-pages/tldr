# systemd-hwdb

> Hardware database management tool.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-hwdb.html>.

- Update the binary hardware database in `/etc/udev`:

`sudo systemd-hwdb update`

- Query the hardware database and print the result for a specific modalias:

`systemd-hwdb query {{modalias}}`

- Update the binary hardware database, returning a non-zero exit value on any parsing error:

`sudo systemd-hwdb {{[-s|--strict]}} update`

- Update the binary hardware database in `/usr/lib/udev`:

`sudo systemd-hwdb --usr update`

- Update the binary hardware database in the specified root path:

`systemd-hwdb {{[-r|--root]}} {{path/to/root}} update`
