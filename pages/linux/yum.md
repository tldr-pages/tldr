# yum

> Package management utility for RHEL, Fedora, and CentOS (for older versions).
> More information: <https://man7.org/linux/man-pages/man8/yum.8.html>.

- Install a new package:

`yum install {{package}}`

- Install a new package and assume yes to all questions (also works with update, great for automated updates):

`yum -y install {{package}}`

- Find the package that provides a particular command:

`yum provides {{command}}`

- Remove a package:

`yum remove {{package}}`

- Display available updates for installed packages:

`yum check-update`

- Upgrade installed packages to newest available versions:

`yum upgrade`
