# test

> Check file types and compare values.
> Returns 0 if the condition evaluates to true, 1 if it evaluates to false.
> More information: <https://www.gnu.org/software/coreutils/test>.

- Test if a given variable is equal to a given string:

`test "{{$MY_VAR}}" == "{{/bin/zsh}}"`

- Test if a given variable is empty:

`test -z "{{$GIT_BRANCH}}"`

- Test if a file exists:

`test -f "{{path/to/file_or_directory}}"`

- Test if a directory does not exist:

`test ! -d "{{path/to/directory}}"`

- If-else statement:

`test {{condition}} && {{echo "true"}} || {{echo "false"}}`
