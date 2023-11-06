# pkgctl repo

> Beheer Git verpakkingsrepositories en hun configuratie voor Arch Linux.
> Bekijk ook: `pkgctl`.
> Meer informatie: <https://man.archlinux.org/man/pkgctl-repo.1>.

- Kloon een pakketrepository (vereist het instellen van een SSH-key in uw Arch Linux GitLab-account):

`pkgctl repo clone {{pkgname}}`

- Kloon een pakketrepository via HTTPS:

`pkgctl repo clone --protocol=https {{pkgname}}`

- Maak een nieuwe GitLab pakketrepository en kloon het na het aanmaken (vereist valide GitLab API authenticatie):

`pkgctl repo create {{pkgbase}}`

- Wissel een pakketrepository naar een specifieke versie:

`pkgctl repo switch {{versie}} {{pkgbase}}`

- Open een pakketrepository's website:

`pkgctl repo web {{pkgbase}}`
