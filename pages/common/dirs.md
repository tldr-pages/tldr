# dirs

> Displays or manipulates the directory stack.
> The directory stack is a list of recently visited directories that can be manipulated with the `pushd` and `popd` commands.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Display the directory stack with a space between each entry:

`dirs`

- Display the directory stack with one entry per line:

`dirs -p`

- Display only the nth entry in the directory stack, starting at 0:

`dirs +{{N}}`

- Clear the directory stack:

`dirs -c`
