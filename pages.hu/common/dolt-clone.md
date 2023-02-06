# dolt clone

> Egy tárolóhely klónozása egy új könyvtárba. További információ: <https://docs.dolthub.com/interfaces/cli#dolt-clone>.

- Egy meglévő adattár klónozása egy adott könyvtárba (alapértelmezés szerint az adattár neve):

`dolt clone {{repository_url}} {{path/to/directory}}`

- Egy meglévő adattár klónozása és egy adott távoli (alapértelmezett az eredet) hozzáadása:

`dolt clone --remote {{remote_name}} {{repository_url}}`

- Egy meglévő tárolóhely klónozása csak egy adott ág lekérdezésével (alapértelmezett az összes ág):

`dolt clone --branch {{branch_name}} {{repository_url}}`

- Adattár klónozása egy AWS régió használatával (a profil alapértelmezett régióját használja, ha nincs megadva):

`dolt clone --aws-region {{region_name}} {{repository_url}}`

- Adattár klónozása AWS hitelesítő fájl használatával:

`dolt clone --aws-creds-file {{credentials_file}} {{repository_url}}`

- Adattár klónozása AWS hitelesítő adatok profiljának használatával (az alapértelmezett profilt használja, ha nincs megadva):

`dolt clone --aws-creds-profile {{profile_name}} {{repository_url}}`

- Adattár klónozása AWS hitelesítő adatok típusának használatával:

`dolt clone --aws-creds-type {{credentials_type}} {{repository_url}}`
