# test

> Evaluate condition.
> If it is true, returns 0 exit status, otherwise returns 1.

- Test if given variable is equal to given string:

`test $MY_VAR == '/bin/zsh'`

- Test if given variable is empty:

`test -z $GIT_BRANCH`

- Test if file exists:

`test -e {{filename}}`

- Test if directory not exists:

`test ! -d {{path/to/directory}}`

- If-else statement:

`test {{condition}} && echo "true" || echo "false"`
