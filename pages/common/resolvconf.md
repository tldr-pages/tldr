# resolvconf

> Manage nameserver information.
> Acts as an intermediary between programs that supply nameserver information and applications that use this information.
> This page documents Debian's implementation of `resolvconf`.
> More information: <https://manned.org/resolvconf.8>.

- Add or override the IFACE.PROG record and run the update scripts if updating is enabled:

`resolvconf -a {{IFACE.PROG}}`

- Delete the IFACE.PROG record and run the update scripts if updating is enabled:

`resolvconf -d {{IFACR.PROG}}`

- Just run the update scripts if updating is enabled:

`resolvconf -u`

- Set the flag indicating whether `resolvconf` should run update scripts when invoked with `-a`, `-d` or `-u`:

`resolvconf --enable-updates`

- Clear the flag indicating whether to run updates:

`resolvconf --disable-updates`

- Check whether updates are enabled:

`resolvconf --updates-are-enabled`
