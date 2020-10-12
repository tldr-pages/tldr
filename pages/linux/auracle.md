# auracle

> Auracle is a command line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR.
> More information: <https://github.com/falconindy/auracle>.

- Find packages in the AUR by regular expression:

`auracle search '{{regex}}'`

- Display package information for a space-separated list of AUR packages:

`auracle info {{packagename}} {{packagename}}`

- Display the  `PKGBUILD` file (build information) for a space-separated list of AUR packages:

`auracle show {{packagename}} {{packagename}}`

- Display updates for installed AUR packages:

`auracle outdated`
