# apt show

> Display detailed information about packages.
> More information: <https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html>.

- Show information about a package:

`apt show {{package}}`

- Show information about multiple packages:

`apt show {{package1 package2}}`

- Show information about all available versions of a package:

`apt show {{package}} -a`

- Show only the package description:

`apt show {{package}} | grep -A5 "Description"`

- Show package information without asking for confirmation:

`apt show {{package}} -qq`

- Show information about an installed package:

`apt show {{package}} --installed`

- Show package information and dependencies:

`apt show {{package}} | grep -E "(Depends|Recommends|Suggests)"`

- Show package size information:

`apt show {{package}} | grep -E "(Download-Size|Installed-Size)"`
