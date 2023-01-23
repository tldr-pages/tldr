# sftp

> Secure File Transfer Program. Interaktív program fájlok másolására hosztok között SSH-n keresztül. Nem interaktív fájlátvitelhez lásd: `scp` vagy `rsync`. További információ: <https://manned.org/sftp>.

- Csatlakozás egy távoli kiszolgálóhoz, és interaktív parancsmódba lépés:

`sftp {{remote_user}}@{{remote_host}}`

- Csatlakozás egy másik porton keresztül:

`sftp -P {{remote_port}} {{remote_user}}@{{remote_host}}`

- Csatlakozás egy előre meghatározott állomás használatával (a `~/.ssh/config` oldalon):

`sftp {{host}}`

- Távoli fájl átvitele a helyi rendszerre:

`get {{/path/remote_file}}`

- Helyi fájl átvitele a távoli rendszerre:

`put {{/path/local_file}}`

- Távoli könyvtár átvitele a helyi rendszerre rekurzív módon (működik a `put` oldalon is):

`get -R {{/path/remote_directory}}`

- A helyi gépen lévő fájlok listájának lekérdezése:

`lls`

- A távoli gépen lévő fájlok listájának lekérdezése:

`ls`
