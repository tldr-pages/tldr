# utmpdump

> Dump and load btmp, utmp and wtmp accounting files.
> More information: <https://manned.org/utmpdump>.

- Dump the `/var/log/wtmp` file to `stdout` as plain text:

`utmpdump {{/var/log/wtmp}}`

- Load a previously dumped file into `/var/log/wtmp`:

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}}`
