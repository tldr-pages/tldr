# czkawka_cli

> Find duplicates, empty folders, similar images and much more.
> More information: <https://github.com/qarmin/czkawka/blob/master/czkawka_cli/README.md>.

- List duplicate in specific directories and write the results into a file:

`czkawka_cli dup {{[-d|--directories]}} {{path/to/directory1}} {{[-d|--directories]}} {{path/to/directory2}} {{[-f|--file-to-save]}} {{path/to/results.txt}}`

- Find duplicate files in specific directories and delete them (default: `NONE`):

`czkawka-cli dup {{[-d|--directories]}} {{path/to/directory}} {{[-D|--delete-method]}} {{AEN|AEO|ON|OO|HARD|NONE}}`

- Find similar looking image with a specific similarity level (default: `High`):

`czkawka-cli image {{[-d|--directories]}} {{path/to/directory}} {{[-s|--similarity-preset]}} {{Minimal|VerySmall|Small|Medium|High|VeryHigh|Original}} {{[-f|--file-to-save]}} {{path/to/results.txt}}`

- Display help:

`czkawka_cli {{[-h|--help]}}`
