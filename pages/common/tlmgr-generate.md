# tlmgr generate

> Remake configuration files from information stored locally.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Remake the configuration file storing into a specific location:

`tlmgr generate --dest {{output_file}}`

- Remake the configuration file using a local configuration file:

`tlmgr generate --localcfg {{local_configuration_file}}`

- Run necessary programs after rebuilding configuration files:

`tlmgr generate --rebuild-sys`
