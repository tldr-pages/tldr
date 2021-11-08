# git sed

> Replace patterns in git-controlled files using sed.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- Replace the specified text in the current repository:

`git sed '{{find_text}}' '{{replace_text}}'`

- Replace the specified text and then commit the resulting changes with a standard commit message:

`git sed -c '{{find_text}}' '{{replace_text}}'`

- Replace the specified text, using regular expressions:

`git sed -f g '{{find_text}}' '{{replace_text}}'`

- Replace a specific text in all files under a given directory:

`git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}`
