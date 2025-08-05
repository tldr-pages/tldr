# minidlna

> ReadyMedia (formerly MiniDLNA) is a lightweight media server compatible with DLNA/UPnP-AV clients.
> Used to stream media to smart TVs, consoles, and other DLNA-compatible devices.
> Configuration is typically done via the `minidlna.conf` file.
> More information: <https://manned.org/minidlna>.

- Start the MiniDLNA daemon using the default configuration at `/etc/minidlna.conf`:

`minidlna`

- Start MiniDLNA with a specific configuration file:

`minidlna -f {{path/to/minidlna.conf}}`

- Force a database rescan on startup:

`minidlna -R`

- Run MiniDLNA in the foreground (useful for debugging):

`minidlna -d`

- Enable verbose debug output:

`minidlna -d -v`

- Specify a custom media directory (overrides config):

`minidlna -m {{path/to/media}}`

- Specify a custom database directory:

`minidlna -P {{path/to/pidfile}}`

- Specify a custom log file path:

`minidlna -l {{path/to/logfil.log}}`
