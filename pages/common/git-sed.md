# git sync

> Replace patterns in git-controlled files using sed.
> Part of `git-extras`.
> More information: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sed>.

- Replace the string 'this' with 'that':

`git sed '{{find_text}}' '{{replace_text}}'`

- Replace the specified text and then commit the resulting changes with a standard commit message:

`git sed -c '{{find_text}}' '{{replace_text}}'`

- Replace the specified text passing regex flags to `sed`:

`git sed -f g '{{find_text}}' '{{replace_text}}'`

- Replace a specific text from files under a given directory:

`git sed '{{find_text}}' '{{replace_text}}' -- {{path/to/directory}}`
