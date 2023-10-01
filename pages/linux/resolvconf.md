# resolvconf

> Manage nameserver information.
> More information: <https://manpages.ubuntu.com/manpages/resolvconf.8.html>

- Add or override a record (IFACE.PROG) and run the update scripts if updating is enabled:

`resolvconf -a {{IFACE.PROG}}`

- Delete the record IFACE.PROG amd run the update scripts if updating is enabled:

`resolvconf -d {{IFACR.PROG}}`

- Just run the update scripts if updating is enabled:

`resolvconf -u`

- Set the flag indicating whether resolvconf should run update scripts when invoked with -a, -d or -u:

`resolvconf --enable-updates`

- Clear the flag indicating whether to run updates:

`resolvconf --disable-updates`

- Check whether updates are enabled:

`resolvconf --updates-are-enabled`
