# peerindex

> Liest MRT TABLE_DUMPV2 Peer Index Table aus.
> Kann mit gzip, bzip2 und xz komprimierte Dateien lesen.
> Weitere Informationen: <https://gitea.it/1414codeforge/ubgpsuite>.

- Gib alle Peers aus:

`peerindex {{master6.mrt}}`

- Zeige alle Peers an, die Routing-Informationen bereitgestellt haben:

`peerindex -r {{master6.mrt}}`
