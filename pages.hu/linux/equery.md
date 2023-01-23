# equery

> A Portage csomagokkal kapcsolatos információk megtekintése. További információ: <https://wiki.gentoo.org/wiki/Equery>.

- Az összes telepített csomag listázása:

`equery list '*'`

- A telepített csomagok keresése a Portage fában és a fedvényekben:

`equery list -po {{package_name}}`

- Az adott csomagtól függő összes csomag listázása:

`equery depends {{package_name}}`

- Az összes olyan csomag listázása, amelytől egy adott csomag függ:

`equery depgraph {{package_name}}`

- Egy csomag által telepített összes fájl listázása:

`equery files --tree {{package_name}}`
