# sfdk scrape

> Converts source code modifications to patches.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/tree/master/src/tools/sfdk>

- Save source modifications as patches:

`sfdk scrape`

- Preview the list of commits to be scrapped:

`sfdk scrape --dry-run`

- Scrape while preserving the original patches file names:

`sfdk scrape --stable`

- Scrape while saving patches to a specified [o]utput directory:

`sfdk scrape -o {{directory}}`

- Scrape without removing commits from submodules after creating patches:

`sfdk scrape --keep`
