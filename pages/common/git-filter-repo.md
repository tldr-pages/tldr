# git filter-repo

> A versatile tool for rewriting Git history.
> See also: `bfg`.
> More information: <https://github.com/newren/git-filter-repo>.

- Replace a sensitive string in all files:

`git filter-repo --replace-text <(echo '{{find}}==>{{replacement}}')`

- Extract a single folder, keeping history:

`git-filter-repo --path {{path/to/folder}}`

- Remove a single folder, keeping history:

`git-filter-repo --path {{path/to/folder}} --invert-paths`

- Move everything from sub-folder one level up:

`git-filter-repo --path-rename {{path/to/folder/:}}`
