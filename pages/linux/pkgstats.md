# pkgstats

> Submit and view Arch Linux package popularity statistics.
> More information: <https://github.com/archlinux-de/pkgstats-cli#usage>.

- Send installed package data:

`pkgstats submit`

- View the sent data:

`pkgstats submit {{[-d|--dump-json]}}`

- Search for packages:

`pkgstats search {{search_term}}`

- Limit search result count (10 by default):

`pkgstats search {{search_term}} {{[-l|--limit]}} {{count}}`

- Pick packages for comparison:

`pkgstats show {{package1 package2 ...}}`

- Display help:

`pkgstats {{[-h|--help]}}`
