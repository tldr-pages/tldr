# bob

> Manage and switch between Neovim versions.
> More information: <https://github.com/MordechaiHadad/bob>.

- Install and switch to the specified version of Neovim:

`bob use {{nightly|stable|latest|version_string|commit_hash}}`

- List installed and currently used versions of Neovim:

`bob list`

- Uninstall the specified version of Neovim:

`bob uninstall {{nightly|stable|latest|version_string|commit_hash}}`

- Uninstall Neovim and erase any changes `bob` has made:

`bob erase`

- Roll back to a previous nightly version:

`bob rollback`
