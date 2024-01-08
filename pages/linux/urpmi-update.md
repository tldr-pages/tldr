# urpmi.update

> Mageia's command for update the list of packages from a package repository.
> NOTE: Mageia documentation uses media and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi.update>.

- Update all enabled media:

`urpmi.update -a`

- Update specific media(s) (including not enable medias):

`urpmi.update {{media1 media2 ...}}`

- Update all medias that contain a keyword:

`urpmi.update {{Upd}}`

- Update all configured medias:

`urpmi.update e`
