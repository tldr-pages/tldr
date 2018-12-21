# yum

> Package management utility for RHEL, Feodra, and CentOS (for older versions).

- Synchronize list of packages and versions available. This should be run first, before running subsequent yum commands:

`yum update`

- Install a new package:

`yum install {{package}}`

- Install a new package and assume yes to all questions (also works with update, great for automated updates):

`yum -y install {{package}}`

- Find the package that provides a particular command:

`yum provides {{command}}`

- Remove a package:

`yum remove {{package}}`

- Upgrade installed packages to newest available versions:

`yum upgrade`
