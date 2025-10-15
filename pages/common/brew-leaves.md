# brew leaves

> List installed formulas that are not dependencies of another installed formula or cask.
> More information: <https://docs.brew.sh/Manpage#leaves---installed-on-request---installed-as-dependency>.

- List installed formulas that are not dependent on other installed formulas or casks:

`brew leaves`

- Only list leaves that were manually installed:

`brew leaves {{[-r|--installed-on-request]}}`

- Only list leaves that were installed as dependencies:

`brew leaves {{[-p|--installed-as-dependency]}}`

- Display help:

`brew leaves {{[-h|--help]}}`
