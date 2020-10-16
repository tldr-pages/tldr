# zsh

> Move (usually, rename) files matching the regex pattern to corresponding files having names of the form given by destination.
> More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Below renames ‘foo.lis’ to ‘foo.txt’, and so on.

`zmv '(*).lis' '$1.txt'`

- No execution: print what would happen, but don’t do it:

`zmv -n '(*).lis' '$1.txt'`

- Interactive: show each line to be executed and ask the user whether to execute it.

`zmv -i '(*).lis' '$1.txt'`
