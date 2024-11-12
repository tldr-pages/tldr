# type

> Display the type of command the shell will execute.
> Note: all examples are not POSIX compliant.
> More information: <https://manned.org/type>.

- Display the type of a command:

`type {{command}}`

- Display all locations containing the specified executable (works only in Bash/fish/Zsh shells):

`type -a {{command}}`

- Display the name of the disk file that would be executed (works only in Bash/fish/Zsh shells):

`type -p {{command}}`

- Display the type of a specific command, alias/keyword/function/builtin/file (works only in Bash/fish shells):

`type -t {{command}}`
