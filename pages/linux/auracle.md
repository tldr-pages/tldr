# auracle

> Interact with Arch Linux's User Repository, commonly referred to as the AUR.
> More information: <https://github.com/falconindy/auracle>.

- Display AUR packages that match a `regex`:

`auracle search '{{regex}}'`

- Display information about one or more AUR packages:

`auracle info {{package1 package2 ...}}`

- Display the `PKGBUILD` file (build information) of one or more AUR packages:

`auracle show {{package1 package2 ...}}`

- Display updates for installed AUR packages:

`auracle outdated`
