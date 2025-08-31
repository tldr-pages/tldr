# rankmirrors

> Rank a list of Pacman mirrors by connection and opening speed.
> Writes the new mirrorlist to `stdout`.
> More information: <https://manned.org/rankmirrors>.

- Rank a mirror list:

`rankmirrors {{path/to/mirrorlist}}`

- Output only a given number of the top ranking servers:

`rankmirrors -n {{number}} {{path/to/mirrorlist}}`

- Be verbose when generating the mirrorlist:

`rankmirrors {{[-v|--verbose]}} {{path/to/mirrorlist}}`

- Test only a specific URL:

`rankmirrors {{[-u|--url]}} {{url}}`

- Output only the response times instead of a full mirrorlist:

`rankmirrors {{[-t|--times]}} {{path/to/mirrorlist}}`
