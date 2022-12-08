# apx

> Package management utility for Vanilla OS.
> Install packages inside managed containers from multiple sources (`apx` supports --aur,--dnf flags in all commands).
> More information: <https://github.com/Vanilla-OS/apx>.

- Initialize the container:

`apx init`

- Install package(s) in the constainer:

`apx install {{package1 package2 ...}}`

- Remove package(s) from the container:

`apx remove {{package1 package2 ...}}`

- Search for packages:

`apx search {{package1 package2 ...}}`

- Enter the managed container shell to execute commands (type `exit` to exit the container):

`apx enter`

- Update the list of available packages in the managed container:

`apx update`

- Upgrade all installed packages in the managed container to their newest available version:

`apx upgrade`
