# apx

> Package management utility.
> Install packages inside managed containers from multiple sources (`apx` supports --aur,--dnf, --apk flags in all commands).
> More information: <https://github.com/Vanilla-OS/apx>.

- Initialize or reinitialize a specific container:

`apx init`

- Install specific packages in the container:

`apx install {{package1 package2 ...}}`

- Install a DEB/RPM package inside the container (Use `--dnf` flag for installing RPMs):

`apx install --sideload {{path/to/package}}`

- Remove specific packages from the container:

`apx remove {{package1 package2 ...}}`

- Search for specific packages:

`apx search {{package1 package2 ...}}`

- Enter the managed container shell to execute commands (type `exit` to exit the container):

`apx enter`

- Update the list of available packages in the container:

`apx update`

- Upgrade all installed packages in the container to their newest available version:

`apx upgrade`
