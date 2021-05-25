# xonsh

> Python-powered, cross-platform, Unix-gazing shell.
> Write and mix sh/Python code in Xonsh (pronounced conch).
> More information: <https://xon.sh>.

- Start an interactive shell session:

`xonsh`

- Execute a single command and then exit:

`xonsh -c "{{command}}"`

- Run commands from a script file and then exit:

`xonsh {{path/to/script_file.xonsh}}`

- Define environment variables for the shell process:

`xonsh -D{{name1}}={{value1}} -D{{name2}}={{value2}}`

- Load the specified `.xonsh` or `.json` configuration files:

`xonsh --rc {{path/to/file1.xonsh}} {{path/to/file2.json}}`

- Skip loading the `.xonshrc` configuration file:

`xonsh --no-rc`
