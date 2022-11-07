# apx

> Package management utility for Vanilla OS.
> It installs packages inside managed containers or directly inside host.
> More information: <https://github.com/Vanilla-OS/apx>.

- Install a package in system and also initilize the container:

`sudo apx install --sys {{package}} && apx init`

- Install package(s) in system:

`sudo apx install --sys {{package1 package2 ...}}`

- Install a package from AUR (Use `apx --aur run {{package}}` and `apx --aur remove {{package}}` to run and remove packages):

`apx --aur install {{package}}`

- Update the list of available packages:

`sudo apx --sys update`

- Upgrade all installed packages in the system to their newest available version:

`sudo apx --sys upgrade`

- Remove package(s) in system:

`sudo apx --sys remove {{package1 package ...}}`

- Enter container to install packages using `apt` (Use `exit` inside the container to exit it):

`apx enter`
