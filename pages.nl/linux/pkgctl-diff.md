# pkgctl diff

> Vergelijk pakketbestanden met behulp van verschillende modi.
> Bekijk ook: `pkgctl`.
> Meer informatie: <https://man.archlinux.org/man/pkgctl-diff.1>.

- Vergelijk pakketbestanden in tar-inhoud [l]ijst verschillende modus (standaard):

`pkgctl diff --list {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in [d]iffoscope verschillende modus:

`pkgctl diff --diffoscope {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in `.PKGINFO` verschillende modus:

`pkgctl diff --pkginfo {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in `.BUILDINFO` verschillende modus:

`pkgctl diff --buildinfo {{pad/naar/bestand|pkgname}}`
