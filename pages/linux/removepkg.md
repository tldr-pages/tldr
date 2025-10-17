# removepkg

> Remove a specified Slackware package.
> More information: <http://www.slackware.com/config/packages.php>.

- Remove a package:

`sudo removepkg {{package_name}}`

- Generate a report of a simulated removal to standard out:

`removepkg -warn {{package_name}}`

- Reconstruct the package subtree in `/tmp/preserved_packages/{{package_name}}` and remove the package:

`sudo removepkg -preserve {{package_name}}`

- Copy package under `/tmp/preserved_packages/package_name` without removing:

`removepkg -copy {{package_name}}`

- Save temporary files created by `removepkg` for debugging:

`sudo removepkg -keep {{package_name}}`
