# pip list

> List installed Python packages.
> More information: <https://pip.pypa.io/en/stable/cli/pip_list/>.

- List installed packages:

`pip list`

- List outdated packages that can be upgraded:

`pip list {{[-o|--outdated]}}`

- List up-to-date packages:

`pip list {{[-u|--uptodate]}}`

- List packages with JSON formatting:

`pip list --format json`

- List packages that are not required by other packages:

`pip list --not-required`

- List packages installed in user-site only:

`pip list --user`

- List packages and exclude editable packages from output:

`pip list --exclude-editable`

- List packages in freeze format (unlike `pip freeze`, does not show editable install information):

`pip list --format freeze`
