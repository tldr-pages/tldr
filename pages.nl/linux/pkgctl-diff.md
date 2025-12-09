# pkgctl diff

> Vergelijk pakketbestanden met behulp van verschillende modi.
> Zie ook: `pkgctl`.
> Meer informatie: <https://manned.org/pkgctl-diff>.

- Vergelijk pakketbestanden in tar-inhoud [l]ijst verschillende modus (standaard):

`pkgctl diff {{[-l|--list]}} {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in [d]iffoscope verschillende modus:

`pkgctl diff {{[-d|--diffoscope]}} {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in `.PKGINFO` verschillende modus:

`pkgctl diff {{[-p|--pkginfo]}} {{pad/naar/bestand|pkgname}}`

- Vergelijk pakketbestanden in `.BUILDINFO` verschillende modus:

`pkgctl diff {{[-b|--buildinfo]}} {{pad/naar/bestand|pkgname}}`
