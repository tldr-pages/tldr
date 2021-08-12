# github-label-sync

> O interfață de linie de comandă pentru sincronizarea etichetelor GitHub.
> Mai multe informaţii: <https://npmjs.com/package/github-label-sync>

- Sincronizarea etichetelor utilizând un fişier local `labels.json':

`github-label-sync --access-token {{token}} {{repository_name}}`

- Sincronizarea etichetelor utilizând un fișier JSON specific etichete:

`github-label-sync --access-token {{token}} --labels {{url|path/to/json_file}} {{repository_name}}`

- Efectuați o rulare uscată în loc să sincronizați efectiv etichete:

`github-label-sync --access-token {{token}} --dry-run {{repository_name}}`

- Păstrați etichetele care nu sunt în `labels.json':

`github-label-sync --access-token {{token}} --allow-added-labels {{repository_name}}`

- Sincronizarea folosind variabila de mediu `GITHUB_ACCES_TOKEN`:

`github-label-sync {{repository_name}}`
