# check-support-status

> Azonosítsa azokat a telepített Debian csomagokat, amelyek támogatását korlátozni kellett vagy idő előtt megszüntették. További információ: <https://manpages.debian.org/latest/debian-security-support/check-support-status.html>.

- Megjeleníti azokat a csomagokat, amelyek támogatása korlátozott, már megszűnt, vagy a disztribúció életciklusának vége előtt véget ér:

`check-support-status`

- Csak olyan csomagok megjelenítése, amelyek támogatása már véget ért:

`check-support-status --type {{ended}}`

- A címsor nyomtatásának kihagyása:

`check-support-status --no-heading`
