# tlmgr pinning

> The pinning action manages the pinning file.
> More information: <https://www.tug.org/texlive/doc/tlmgr.html#pinning>.

- Show the current pinning data:

`tlmgr pinning show`

- Pin the matching the packages to the given repository:

`tlmgr pinning add {{repository}} {{package1 package2 ...}}`

- Remove any packages recorded in the pinning file matching the packages for the given repository:

`tlmgr pinning remove {{repository}} {{package1 package2 ...}}`

- Remove all pinning data for the given repository:

`tlmgr pinning remove {{repository}} --all`
