# rpmconf

> Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades.
> See also: `rpm`.
> More information: <https://manned.org/rpmconf.8>.

- List leftover files and interactively choose what to do with each of them:

`sudo rpmconf {{[-a|--all]}}`

- Delete orphaned RPMNEW and RPMSAVE files:

`sudo rpmconf {{[-a|--all]}} {{[-c|--clean]}}`
