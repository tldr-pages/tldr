# rpmconf

> Handle RPMNEW, RPMSAVE and RPMORIG files left over by package upgrades.
> See also: `rpm`.
> More information: <https://github.com/xsuchy/rpmconf>.

- List leftover files and interactively choose what to do with each of them:

`sudo rpmconf --all`

- Delete orphaned RPMNEW and RPMSAVE files:

`sudo rpmconf --all --clean`
