# xbps-query

> XBPS utility to query for package and repository information.
> See also: `xbps`.
> More information: <https://manned.org/xbps-query.1>.

- Search for a package in remote repositories using a regular expression or a keyword (if `--regex` is omitted):

`xbps-query {{[-s|--search]}} {{regular_expression|keyword}} --repository --regex`

- Show information about an installed package:

`xbps-query {{[-S|--show]}} {{package}}`

- Show information about a package in remote repositories:

`xbps-query {{[-S|--show]}} {{package}} --repository`

- List packages registered in the package database:

`xbps-query {{[-l|--list-pkgs]}}`

- List explicitly installed packages (i.e. not automatically installed as dependencies):

`xbps-query {{[-m|--list-manual-pkgs]}}`
