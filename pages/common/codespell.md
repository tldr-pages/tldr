# codespell

> Spellchecker for source code.
> More information: <https://github.com/codespell-project/codespell>.

- Check for typos in all text files in the current directory, recursively:

`codespell`

- Correct all typos found in-place:

`codespell --write-changes`

- Skip files with names that match the specified pattern (accepts a comma-separated list of patterns using wildcards):

`codespell --skip "{{pattern}}"`

- Use a custom dictionary file when checking (`--dictionary` can be used multiple times):

`codespell --dictionary {{path/to/file.txt}}`

- Do not check words that are listed in the specified file:

`codespell --ignore-words {{path/to/file.txt}}`

- Do not check the specified words:

`codespell --ignore-words-list {{words,to,ignore}}`

- Print 3 lines of context around, before or after each match:

`codespell --{{context|before-context|after-context}} {{3}}`

- Check file names for typos, in addition to file contents:

`codespell --check-filenames`
