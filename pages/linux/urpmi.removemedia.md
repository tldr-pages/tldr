# urpmi.removemedia

> Remove media in Mageia.
> Note: Mageia documentation uses medium and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Remove a medium:

`sudo urpmi.removemedia {{medium}}`

- Remove all media:

`sudo urpmi.removemedia -a`

- Remove media fuzz[y] matching on media names:

`sudo urpmi.removemedia -y {{keyword}}`
