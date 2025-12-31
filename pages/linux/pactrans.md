# pactrans

> Install, remove, and upgrade ALPM packages.
> See also: `pacinstall`, `pacremove`.
> More information: <https://github.com/andrewgregory/pacutils/blob/master/doc/pactrans.pod>.

- Install a package from a repository:

`sudo pactrans --install {{package_name}}`

- Remove a package:

`sudo pactrans --remove {{package_name}}`

- Upgrade all installed packages:

`sudo pactrans --sysupgrade`

- Install a package file:

`sudo pactrans --file {{path/to/package.pkg.tar.zst}}`

- Replace a locally installed package with a package from a repository:

`sudo pactrans local/{{package_to_remove}} {{repository_name}}/{{package_to_install}}`

- Print what the transaction would do without performing it:

`pactrans --print-only --install {{package_name}}`
