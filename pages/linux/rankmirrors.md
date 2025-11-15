# rankmirrors

> Rank a list of Pacman mirrors by connection and opening speed.
> Writes the new mirrorlist to `stdout`.
> More information: <https://manned.org/rankmirrors>.

- Rank a mirror list:

`rankmirrors {{/etc/pacman.d/mirrorlist}}`

- Output only a given number of the top ranking servers:

`rankmirrors -n {{number}} {{/etc/pacman.d/mirrorlist}}`

- Be verbose when generating the mirrorlist:

`rankmirrors {{[-v|--verbose]}} {{/etc/pacman.d/mirrorlist}}`

- Test only a specific URL:

`rankmirrors {{[-u|--url]}} {{url}}`

- Output only the response times instead of a full mirrorlist:

`rankmirrors {{[-t|--times]}} {{/etc/pacman.d/mirrorlist}}`
