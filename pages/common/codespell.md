# codespell

> Spellchecker for source code.
> More information: <https://manned.org/codespell>.

- Check for typos in all text files in the current directory, recursively:

`codespell`

- Correct all typos found in-place:

`codespell {{[-w|--write-changes]}}`

- Skip files with names that match the specified pattern (accepts a comma-separated list of patterns using wildcards):

`codespell {{[-S|--skip]}} "{{pattern}}"`

- Use a custom dictionary file when checking (`--dictionary` can be used multiple times):

`codespell {{[-D|--dictionary]}} {{path/to/file.txt}}`

- Do not check words that are listed in the specified file:

`codespell {{[-I|--ignore-words]}} {{path/to/file.txt}}`

- Do not check the specified words:

`codespell {{[-L|--ignore-words-list]}} {{ignored_word1,ignored_word2,...}}`

Print 3 lines of [C]ontext around, [B]efore, or [A]fter each match:

`codespell --{{context|before-context|after-context}} 3`

- Check file names for typos, in addition to file contents:

`codespell {{[-f|--check-filenames]}}`
