# bgpgrep

> Filter and print BGP data within MRT dumps.
> Can read files compressed with `gzip`, `bzip2` and `xz`.
> More information: <https://codeberg.org/1414codeforge/ubgpsuite>.

- Output all routes:

`bgpgrep {{master6.mrt}}`

- Output all routes received from a specific peer, determined by the peer's AS number:

`bgpgrep {{master4.mrt}} -peer {{64498}}`

- Output all routes received from a specific peer, determined by the peer's IP address:

`bgpgrep {{master4.mrt.bz2}} -peer {{2001:db8:dead:cafe:acd::19e}}`

- Output all routes which have certain ASNs in their AS path:

`bgpgrep {{master6.mrt.bz2}} -aspath '{{64498 64510}}'`

- Output all routes that lead to a specific address:

`bgpgrep {{master6.mrt.bz2}} -supernet '{{2001:db8:dead:cafe:aef::5}}'`

- Output all routes that have communities from a specific AS:

`bgpgrep {{master4.mrt}} -communities \( '{{64497}}:*' \)`
