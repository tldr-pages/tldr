# rpmconf

> Handle `.rpmnew`, `.rpmsave`, and `.rpmorig` files left over by package upgrades.
> See also: `rpm`.
> More information: <https://manned.org/rpmconf.8>.

- List leftover files and interactively choose what to do with each of them:

`sudo rpmconf {{[-a|--all]}}`

- Delete orphaned `.rpmnew` and `.rpmsave` files:

`sudo rpmconf {{[-a|--all]}} {{[-c|--clean]}}`
