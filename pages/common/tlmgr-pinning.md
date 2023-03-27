# tlmgr pinning

> The pinning action manages the pinning file.
> More information: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- Show the current pinning data:

`pinning show`

- Pin the packages matching the packages(s) to the repository repository:

`pinning add {{repository}} {{package(s)}}`

- Any packages recorded in the pinning file matching the <package>s for the given repository are removed:

`pinning remove {{repository}} {{package(s)}}`

- Remove all pinning data for repository repo:

`pinning remove repo --all`
