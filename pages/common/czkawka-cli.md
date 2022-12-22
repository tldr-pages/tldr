# czkawka-cli

> Command-line version of `czkawka` a multi-functional app to find duplicates, empty folders, similar images and much more.
> More information: <https://github.com/qarmin/czkawka>.

- List duplicate or similar files in specific directories:

`czkawka-cli {{dup|image}} --directories {{path/to/directory1 path/to/directory2 ...}}`

- Find duplicate files in specific directories and delete them (default: `NONE`):

`czkawka-cli dup --directories {{path/to/directory1 path/to/directory2 ...}} --delete-method {{AEN|AEO|ON|OO|HARD|NONE}}`
