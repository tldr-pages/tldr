# tlmgr generate

> Remake configuration files from information stored locally.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- Specify output file:

`tlmgr generate --dest {{output_file}}`

- Specify local additions:

`tlmgr generate --localcfg {{local_conf_file}}`

- Run necessary programs after rebuilding config files:

`tlmgr generate --rebuild-sys`
