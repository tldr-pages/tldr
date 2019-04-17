# utmpdump

> Dump and load btmp, utmp and wtmp accounting files.

- Dump {{/var/log/wtmp}} file to standard out as plain text:

`utmpdump {{/var/log/wtmp}}`

- Load previously dumped {{dumpfile}} into {{/var/log/wtmp}:

`utmpdump -r {{dumpfile}} > {{/var/log/wtmp}`
