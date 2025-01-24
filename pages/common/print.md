# print
> Z Shell ('zsh') builtin. Prints arguments, similar to 'echo'.
See also: 'echo', 'printf'
> More information: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>

- Print input:
'print "Hello" "World"'

- Print seperated by newline(s):
'print -l "Linel" "Line 2" "Line3"'

- Print without trailing newline
'print -n "Hello"; print "World"'

- Enable backslash escapes
'print -e "Line 1\nLine2"'
- Print arguments as described by 'printf'. Note: For greater portability across shells use 'printf'.

'print -f "%s is %d years old.\n" "Alice" 30'
