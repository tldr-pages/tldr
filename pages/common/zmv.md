# zmv

> Move or rename files matching the regex pattern to corresponding files having names of the form given by destination.
> More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Below renames ‘foo.lis’ to ‘foo.txt’, and so on:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- Preview the command result without any changes to the files:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Interactively move files, with a prompt before every change:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- Verbosely print each command as it’s being executed:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`

- Force `cp` (copy) regardless of the name of the function. Same as `zcp`:

`zmv -C '{{(*).log}}' '{{$1.txt}}'`

- Force `ln` (link) regardless of the name of the function. Same as `zln`:

`zmv -L '{{(*).log}}' '{{$1.txt}}'`
