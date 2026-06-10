# github-label-sync

> Համաժամացրեք GitHub պիտակները:.
> Լրացուցիչ տեղեկություններ. <https://github.com/Financial-Times/github-label-sync>:.

- Համաժամացրեք պիտակները՝ օգտագործելով տեղական `labels.json` ֆայլը՝:

`github-label-sync --access-token {{token}} {{repository_name}}`

- Համաժամացրեք պիտակները՝ օգտագործելով հատուկ պիտակների JSON ֆայլ.:

`github-label-sync --access-token {{token}} --labels {{url|path/to/json_file}} {{repository_name}}`

- Կատարեք չոր գործարկում՝ իրականում պիտակները համաժամացնելու փոխարեն.:

`github-label-sync --access-token {{token}} --dry-run {{repository_name}}`

- Պահպանեք պիտակները, որոնք `labels.json`-ում չեն՝:

`github-label-sync --access-token {{token}} --allow-added-labels {{repository_name}}`

- Սինքրոնացրեք `$GITHUB_ACCESS_TOKEN` միջավայրի փոփոխականի միջոցով.:

`github-label-sync {{repository_name}}`
