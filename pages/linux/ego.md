# ego

> Funtoo's official system personality management tool.
> More information: <https://funtoo-ego.readthedocs.io/en/develop/>.

- Synchronize the Portage tree:

`ego sync`

- Update the bootloader configuration:

`ego boot update`

- Read a Funtoo wiki page by name:

`ego doc {{wiki_page}}`

- Print current profile:

`ego profile show`

- Enable/Disable mix-ins:

`ego profile mix-in +{{gnome}} -{{kde-plasma-5}}`

- Query Funtoo bugs, related to a specified package:

`ego query bug {{package}}`
