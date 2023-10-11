# echo

> Print given arguments.
> More information: <https://www.gnu.org/software/coreutils/echo>.

- Print a text message. Note: quotes are optional:

`echo "{{Hello World}}"`

- Print a message with environment variables:

`echo "{{My path is $PATH}}"`

- Print a message without the trailing newline:

`echo -n "{{Hello World}}"`

- Append a message to the file:

`echo "{{Hello World}}" >> {{file.txt}}`

- Enable interpretation of backslash escapes (special characters):

`echo -e "{{Column 1\tColumn 2}}"`

- Print the exit status of the last executed command (Note: In Windows Command Prompt and PowerShell the equivalent commands are `echo %errorlevel%` and `$lastexitcode` respectively):

`echo $?`
