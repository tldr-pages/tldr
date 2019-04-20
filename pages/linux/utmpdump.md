# utmpdump

> Dump and load btmp, utmp and wtmp accounting files.

- Dump the `/var/log/wtmp` file to the standard output as plain text:

`utmpdump {{/var/log/wtmp}}`

- Load a previously dumped file into `/var/log/wtmp`:

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}}`
