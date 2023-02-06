# mosh

> A Mobile Shell (`mosh`) egy robusztus és érzékeny helyettesítője az SSH-nak.`mosh` a távoli szerverekhez való kapcsolatokat a hálózatok közötti barangolás során is fenntartja. További információ: <https://mosh.org>.

- Csatlakozás egy távoli kiszolgálóhoz:

`mosh {{username}}@{{remote_host}}`

- Csatlakozás egy távoli kiszolgálóhoz egy adott azonosítóval (privát kulcs):

`mosh --ssh="ssh -i {{path/to/key_file}}" {{username}}@{{remote_host}}`

- Csatlakozás egy távoli kiszolgálóhoz egy adott porton keresztül:

`mosh --ssh="ssh -p {{2222}}" {{username}}@{{remote_host}}`

- Parancs futtatása egy távoli kiszolgálón:

`mosh {{remote_host}} -- {{command -with -flags}}`

- Mosh UDP port kiválasztása (hasznos, ha a `{{remote_host}}` NAT mögött van):

`mosh -p {{124}} {{username}}@{{remote_host}}`

- Használat, ha a `mosh-server` bináris a szabványos elérési útvonalon kívül van:

`mosh --server={{path/to/bin/}}mosh-server {{remote_host}}`
