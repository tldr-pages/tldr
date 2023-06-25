# xbps-query

> XBPS utility to query for package and repository information.
> See also: `xbps`.
> More information: <https://man.voidlinux.org/xbps-query.1>.

- Search for a package in remote repositories using a regular expression or a keyword (if `--regex` is omitted):

`xbps-query --search {{regular_expression|keyword}} --repository --regex`

- Show information about an installed package:

`xbps-query --show {{package}}`

- Show information about a package in remote repositories:

`xbps-query --show {{package}} --repository`

- List packages registered in the package database:

`xbps-query --list-pkgs`

- List explicitly installed packages (i.e. not automatically installed as dependencies):

`xbps-query --list-manual-pkgs`
