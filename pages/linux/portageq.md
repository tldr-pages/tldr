# portageq

> Query for information about Portage, the Gentoo Linux package manager.
> Queryable Portage-specific environment variables are listed in `/var/db/repos/gentoo/profiles/info_vars`.
> More information: <https://wiki.gentoo.org/wiki/Portageq>.

- Display the value of a Portage-specific environment variable:

`portageq envvar {{variable}}`

- Display a detailed list of repositories configured with Portage:

`portageq repos_config /`

- Display a list of repositories sorted by priority (highest first):

`portageq get_repos /`

- Display a specific piece of metadata about an atom (i.e. package name including the version):

`portageq metadata / {{ebuild|porttree|binary|...}} {{category}}/{{package}} {{BDEPEND|DEFINED_PHASES|DEPEND|...}}`
