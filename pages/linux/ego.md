# ego

> Funtoo's official system personality management tool.
> More information: <https://funtoo-ego.readthedocs.io/en/develop/index.html>.

- Synchronize the Portage tree:

`ego sync`

- Update bootloader configuration:

`ego boot update`

- Read a Funtoo wiki page by name:

`ego doc {{wiki_page}}`

- Print current profile:

`ego profile show`

- Enable a mix-in:

`ego profile mix-in +{{gnome}}`

- Disable a mix-in:

`ego profile mix-in -{{gnome}}`

- Query Funtoo bugs, related to a given package:

`ego query bug {{package}}`
