# if

> Simple shell conditional.

- Echo a different thing depending on a command's success:

`{{command}} && echo "success" || echo "failure"`

- Full if syntax:

`if {{condition}}; then echo "true"; else echo "false"; fi`

- List available if conditions:

`help test`

- Test if a given variable is empty:

`if [[ -z $GIT_BRANCH ]]; then echo "true"; else echo "false"; fi`

- Test if a file exists:

`if [[ -e {{filename}} ]]; then echo "true"; else echo "false"; fi`

- If directory not exists:

`if [[ ! -d {{path/to/directory}} ]]; then echo "true"; else echo "false"; fi`
