# urpmi.removemedia

> Mageia's command for removing medias.
> NOTE: Mageia documentation uses media and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
> More information: <https://wiki.mageia.org/en/URPMI#urpmi.removemedia>.

- Remove a media:

`sudo urpmi.removemedia {{media}}`

- Remove all medias:

`sudo urpmi.removemedia -a`

- Remove medias fuzz[y] matching on media names:

`sudo urpmi.removemedia -y {{keyword}}`
