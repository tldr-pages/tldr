# zmv

> Move or rename files matching the regex pattern to corresponding files having names of the form given by destination.
> More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Below renames ‘foo.lis’ to ‘foo.txt’, and so on:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- Preview the command result without any changes to the files:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Interactively move files, with a prompt before every change:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`
