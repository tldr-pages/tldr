# tlmgr generate

> Remake configuration files from information stored locally.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Remake the configuration file storing into a specific location:

`tlmgr generate --dest {{path/to/file}}`

- Remake the configuration file using a local configuration file:

`tlmgr generate --localcfg {{path/to/file}}`

- Run necessary programs after rebuilding configuration files:

`tlmgr generate --rebuild-sys`
