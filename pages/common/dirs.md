# dirs

> Display or manipulate the directory stack.
> The directory stack is a list of recently visited directories that can be manipulated with the `pushd` and `popd` commands.
> See also: `pushd`, `popd`.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Display the directory stack with a space between each entry:

`dirs`

- Display the directory stack with one entry per line:

`dirs -p`

- Display a numbered list of entries in the directory stack:

`dirs -v`

- Display the directory stack without the tilde-prefix (`~`):

`dirs -l`

- Display only the `n`th entry in the directory stack, starting at 0 (Bash only):

`dirs +{{n}}`

- Display only the `n`th entry in the directory stack from the last, starting at 0 (Bash only):

`dirs -{{n}}`

- Clear the directory stack:

`dirs -c`
