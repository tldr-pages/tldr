# installpkg

> Install a Slackware package.
> More information: <http://www.slackware.com/config/packages.php>.

- Install a package:

`sudo installpkg {{path/to/package.tgz}}`

- Generate a report of a simulated installation to standard out:

`installpkg -warn {{path/to/package.tgz}}`

- Create a package from current directory and its subdirectories:

`installpkg -m {{package_name.tgz}}`

- Install the contents of the current directory and subdirectories as a package with a specified name:

`sudo installpkg -r {{package_name.tgz}}`
