# auracle

> Auracle is a command line tool used to interact with Arch Linux's User Repository, commonly referred to as the AUR.
> More information: <https://github.com/falconindy/auracle>.

- Find packages in the AUR by regular expression:

`auracle search {{regexp}}`

- Print detailed information about packages:

`auracle info {{packagename}} {{packagename}}`

- Show the contents of a source file for a/multiple package(s) (e.g. the PKGBUILD):

`auracle show {{packagename}} {{packagename}}`

- Display updates for installed AUR packages:

`auracle outdated`
