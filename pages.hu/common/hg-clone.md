# hg clone

> Egy meglévő adattár másolatának létrehozása egy új könyvtárban. További információ: <https://www.mercurial-scm.org/doc/hg.1.html#clone>.

- Adattár klónozása egy megadott könyvtárba:

`hg clone {{remote_repository_source}} {{destination_path}}`

- A tárolóhely klónozása egy adott ág fejébe, figyelmen kívül hagyva a későbbi commitokat:

`hg clone --branch {{branch}} {{remote_repository_source}}`

- Repozitórium klónozása csak a `.hg` könyvtárral, fájlok ellenőrzése nélkül:

`hg clone --noupdate {{remote_repository_source}}`

- Repozitórium klónozása egy adott revízióra, címkére vagy ágra, a teljes előzmények megtartásával:

`hg clone --updaterev {{revision}} {{remote_repository_source}}`

- Adattár klónozása egy adott revízióig, újabb előzmények nélkül:

`hg clone --rev {{revision}} {{remote_repository_source}}`
