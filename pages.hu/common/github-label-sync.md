# github-label-sync

> Parancssori felület a GitHub-címkék szinkronizálásához. További információ: <https://github.com/Financial-Times/github-label-sync>.

- Címkék szinkronizálása egy helyi `labels.json` fájl segítségével:

`github-label-sync --access-token {{token}} {{repository_name}}`

- Címkék szinkronizálása egy adott címkék JSON fájl használatával:

`github-label-sync --access-token {{token}} --labels {{url|path/to/json_file}} {{repository_name}}`

- Szárazfutás végrehajtása a címkék tényleges szinkronizálása helyett:

`github-label-sync --access-token {{token}} --dry-run {{repository_name}}`

- Tartsa meg azokat a címkéket, amelyek nincsenek a `labels.json`:

`github-label-sync --access-token {{token}} --allow-added-labels {{repository_name}}`

- Szinkronizálás a `GITHUB_ACCESS_TOKEN` környezeti változó használatával:

`github-label-sync {{repository_name}}`
