# eix

> Utilities for searching local Gentoo packages.

- Synchronize local cache (should be ran after installation/updating packages):

`eix-update`

- Search for a package:

`eix {{package_name}}`

- Search for installed packages:

`eix -I {{package_name}}`

- Seach in package descriptions:

`eix -S {{description}}`

- Seach by package license:

`eix -L {{license}}`

- Exclude results from search:

`eix --not -L {{license}}`
