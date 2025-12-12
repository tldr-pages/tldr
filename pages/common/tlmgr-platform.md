# tlmgr platform

> Manage TeX Live platforms.
> More information: <https://www.tug.org/texlive/doc/tlmgr.html#platform>.

- List all available platforms in the package repository:

`tlmgr {{[arch|platform]}} list`

- Add the executables for a specific platform:

`sudo tlmgr {{[arch|platform]}} add {{platform}}`

- Remove the executables for a specific platform:

`sudo tlmgr {{[arch|platform]}} remove {{platform}}`

- Auto-detect and switch to the current platform:

`sudo tlmgr {{[arch|platform]}} set auto`

- Switch to a specific platform:

`sudo tlmgr {{[arch|platform]}} set {{platform}}`
