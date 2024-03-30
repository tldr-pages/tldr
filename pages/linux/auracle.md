# auracle

> Command-line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR.
> More information: <https://github.com/falconindy/auracle>.

- Display AUR packages that match a regular expression:

`auracle search '{{regular_expression}}'`

- Display information about one or more AUR packages:

`auracle info {{package1 package2 ...}}`

- Display the `PKGBUILD` file (build information) of one or more AUR packages:

`auracle show {{package1 package2 ...}}`

- Display updates for installed AUR packages:

`auracle outdated`
