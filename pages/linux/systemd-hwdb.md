# systemd-hwdb

> Hardware database management tool.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-hwdb.html>.

- Update the binary hardware database:

`systemd-hwdb update`

- Query the hardware database and print the result for a specific modalias:

`systemd-hwdb query {{modalias}}`

- Update the binary hardware database, but return a non-zero exit value on any parsing error:

`systemd-hwdb --strict update`

- Update the binary hardware database, and generate it in /usr/lib/udev instead of /etc/udev:

`systemd-hwdb --usr update`

- Update the binary hardware database, specifying an alternate root path in the filesystem:

`systemd-hwdb --root={{path/to/root}} update`
