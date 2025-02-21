# print

> Z Shell (`zsh`) builtin. Prints arguments, similar to `echo`.
> See also: `echo`, `printf`, `zsh`.
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Print input:

`print "Hello" "World"`

- Print separated by newline(s):

`print -l "Line1" "Line 2" "Line3"`

- Print without trailing newline:

`print -n "Hello"; print "World"`

- Enable backslash escapes:

`print -e "Line 1\nLine2"`

- Print arguments as described by `printf` (for greater portability across shells, consider using the `printf` command instead):

`print -f "%s is %d years old.\n" "Alice" 30`
