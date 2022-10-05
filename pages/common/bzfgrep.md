# bzfgrep

> Find any fixed strings separated by new lines in bzip2 compressed files using fgrep.
> More information: <https://manned.org/bzfgrep>.

- Search for lines matching the list of search strings separated by new lines in a compressed file (case-sensitive):

`bzfgrep "{{search_string}}" {{path/to/file}}`

- Search for lines matching the list of search strings separated by new lines in a compressed file (case-insensitive):

`bzfgrep --ignore-case "{{search_string}}" {{path/to/file}}`

- Search for lines that do not match the list of search strings separated by new lines in a compressed file:

`bzfgrep --invert-match "{{search_string}}" {{path/to/file}}`

- Print file name and line number for each match:

`bzfgrep --with-filename --line-number "{{search_string}}" {{path/to/file}}`

- Search for lines matching a pattern, printing only the matched text:

`bzfgrep --only-matching "{{search_string}}" {{path/to/file}}`

- Recursively search files in a bzip2 compressed tar archive for the given list of strings:

`bzfgrep --recursive "{{search_string}}" {{path/to/file}}`
