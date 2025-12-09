# bgpgrep

> Filtert und gibt BGP-Daten in einem MRT-Dump aus.
> Kann mit gzip, bzip2 und xz komprimierte Dateien lesen.
> Weitere Informationen: <https://codeberg.org/1414codeforge/ubgpsuite>.

- Gib alle Routen aus:

`bgpgrep {{master6.mrt}}`

- Gib alle von einem bestimmten Peer empfangenen Routen aus, bestimmt durch die AS-Nummer des Peers:

`bgpgrep {{master4.mrt}} -peer {{64498}}`

- Gib alle von einem bestimmten Peer empfangenen Routen aus, bestimmt durch die IP-Adresse des Peers:

`bgpgrep {{master4.mrt.bz2}} -peer {{2001:db8:dead:cafe:acd::19e}}`

- Gib alle Routen aus, die bestimmte ASNs in ihrem AS-Pfad haben:

`bgpgrep {{master6.mrt.bz2}} -aspath '{{64498 64510}}'`

- Gib Routen aus, die zu einer bestimmten Adresse führen:

`bgpgrep {{master6.mrt.bz2}} -supernet '{{2001:db8:dead:cafe:aef::5}}'`

- Gib alle Routen aus, die Communities von einem bestimmten AS haben:

`bgpgrep {{master4.mrt}} -communities \( '{{64497}}:*' \)`
