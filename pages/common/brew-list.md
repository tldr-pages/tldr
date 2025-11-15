# brew list

> List installed formulae/casks or their files.
> More information: <https://docs.brew.sh/Manpage#list-ls-options-installed_formulainstalled_cask->.

- List all installed formulae and casks:

`brew {{[ls|list]}}`

- List files belonging to an installed formula:

`brew {{[ls|list]}} {{formula}}`

- List artifacts of a cask:

`brew {{[ls|list]}} {{cask}}`

- List only formulae:

`brew {{[ls|list]}} --formula`

- List only casks:

`brew {{[ls|list]}} --cask`

- List only pinned formulae:

`brew {{[ls|list]}} --pinned`
