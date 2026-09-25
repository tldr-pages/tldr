# print

> Z Shell (`zsh`) ingebouwd commando. Print argumenten, vergelijkbaar met `echo`.
> Zie ook: `echo`, `printf`, `zsh`.
> Meer informatie: <https://zsh.sourceforge.io/Doc/Release/Shell-Builtin-Commands.html>.

- Print invoer:

`print "Hello" "World"`

- Print gescheiden door regeleinde(n):

`print -l "Line1" "Line 2" "Line3"`

- Print zonder afsluitend regeleinde:

`print -n "Hello"; print "World"`

- Schakel backslash-escapes in:

`print -e "Line 1\nLine2"`

- Print argumenten zoals beschreven door `printf` (overweeg voor betere overdraagbaarheid tussen shells om het `printf`-commando te gebruiken):

`print -f "%s is %d years old.\n" "Alice" 30`
