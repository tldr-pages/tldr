# git difftool

> Show file changes using external diff tools. Accepts the same options and arguments as Git diff.
> More information: <https://git-scm.com/docs/git-difftool>.

- List available diff tools:

`git difftool --tool-help`

- Set the default diff tool to meld:

`git config --global diff.tool "{{meld}}"`

- Use the default diff tool to show staged changes:

`git difftool --staged`

- Use a specific tool (opendiff) to show changes since a given commit:

`git difftool --tool={{opendiff}} {{commit}}`
