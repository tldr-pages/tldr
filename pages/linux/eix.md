# eix

> Utilities for searching local Gentoo packages.
> Update local package cache using `eix-update`.

- Search for a package:

`eix {{package_name}}`

- Search for installed packages:

`eix --installed {{package_name}}`

- Search in package descriptions:

`eix --description "{{description}}"`

- Search by package license:

`eix --license {{license}}`

- Exclude results from search:

`eix --not --license {{license}}`
