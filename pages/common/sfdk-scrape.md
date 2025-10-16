# sfdk scrape

> Convert source code modifications to patches.
> More information: <https://github.com/sailfishos/sailfish-qtcreator/blob/master/share/qtcreator/sfdk/modules/65-maintaining-mb2/doc/command.scrape.adoc>.

- Save source modifications as patches:

`sfdk scrape`

- Preview the list of commits to be scrapped:

`sfdk scrape {{[-n|--dry-run]}}`

- Scrape while preserving the original patches file names:

`sfdk scrape --stable`

- Scrape while saving patches to a specified [o]utput directory:

`sfdk scrape {{[-o|--output-dir]}} {{directory}}`

- Scrape without removing commits from submodules after creating patches:

`sfdk scrape --keep`
