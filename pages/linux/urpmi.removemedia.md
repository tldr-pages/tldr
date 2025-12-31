# urpmi.removemedia

> Remove media in Mageia.
> Note: Mageia documentation uses medium and repository as synonymous.
> See also: `urpmi`, `urpme`, `urpmi.addmedia`, `urpmi.update`, `urpmf`, `urpmq`.
> More information: <https://man.linuxreviews.org/man8/urpmi.removemedia.8.html>.

- Remove a medium:

`sudo urpmi.removemedia {{medium}}`

- Remove [a]ll media:

`sudo urpmi.removemedia -a`

- Remove media fuzz[y] matching on media names:

`sudo urpmi.removemedia -y {{keyword}}`
