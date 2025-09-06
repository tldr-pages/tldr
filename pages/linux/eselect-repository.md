# eselect repository

> An `eselect` module for configuring ebuild repositories for Portage.
> After enabling a repository, you have to run `emerge --sync repo_name` to download ebuilds.
> More information: <https://wiki.gentoo.org/wiki/Eselect/Repository>.

- List all ebuild repositories registered on <https://repos.gentoo.org>:

`eselect repository list`

- List enabled repositories:

`eselect repository list -i`

- Enable a repository from the list by its name or index from the `list` command:

`eselect repository enable {{name|index}}`

- Enable an unregistered repository:

`eselect repository add {{name}} {{rsync|git|mercurial|svn|...}} {{sync_uri}}`

- Disable repositories without removing their contents:

`eselect repository disable {{repo1 repo2 ...}}`

- Disable repositories and remove their contents:

`eselect repository remove {{repo1 repo2 ...}}`

- Create a local repository and enable it:

`eselect repository create {{name}} {{path/to/repo}}`
