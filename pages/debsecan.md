# debsecan

> A tool to list vulnerabilities on a particular Debian installation. 
> More information: <https://gitlab.com/fweimer/debsecan>.

- List vulnerable installed packages on the current host:

`debsecan`

- List vulnerable installed packages of a specific suite:

`debsecan --suite {{release_code_name}}`

- List only fixed vulnerabilities of testing ("sid"):

`debsecan --suite sid --only-fixed`

- List only fixed vulnerabilities of testing ("sid") and mail to root:

`debsecan --suite {{sid}} --only-fixed --format {{report}} --mailto {{root}} --update-history`

- Upgrade vulnerable installed packages:

`sudo apt upgrade $(debsecan --only-fixed --format packages)`
