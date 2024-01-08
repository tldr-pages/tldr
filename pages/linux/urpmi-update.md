# urpmi.update

> Mageia's command for update the list of packages from a package repository.
> NOTE: Mageia documentation uses medium and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.removemedia`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi.update>.

- Update all enabled media:

`urpmi.update -a`

- Update specific media (including disabled media):

`urpmi.update {{medium1 medium2 ...}}`

- Update all media that contain a keyword:

`urpmi.update {{upd}}`

- Update all configured media:

`urpmi.update e`
