# shellcheck

> Shell script static analysis tool

- Check a shell script

`shellcheck myscript.sh`

- Override script's shebang (valid values: sh, bash, and ksh)

`shellcheck --shell sh myscript.sh`

- Ignore certain errors

`shellcheck --exclude SC1009 test.sh`

- Ignore multiple errors

`shellcheck --exclude SC1009,SC1073 test.sh`

