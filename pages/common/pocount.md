# pocount

> Translate Toolkit utility to get translation progress from file, supporting several formats.
> More information: <https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/pocount.html>.

- Print a colorful table with the translation progress of a file:

`pocount {{path/to/file/file.po}}`

- Print translation progress of various files, one line per file:

`pocount --short {{translation_*.ts}}`

- Generate a CSV file with the translation progress of various files:

`pocount --csv {{translation_*.ts}} > {{path/to/translation_progress.csv}}`
