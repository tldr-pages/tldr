# tldr platform

> Manage TeX Live platforms.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all available platforms in the package repository:

`tlmgr platform list`

- Add the executables for a specific platform:

`sudo tlmgr platform add {{platform}}`

- Remove the executables for a specific platform:

`sudo tlmgr platform remove {{platform}}`

- Auto-detect and switch to the current platform:

`sudo tlmgr platform set {{auto}}`

- Switch to a specific platform:

`sudo tlmgr platform set {{platform}}`
