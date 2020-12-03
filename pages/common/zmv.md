# zmv

> Move or rename files matching a specified regex pattern.
> More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Below renames `foo.log` to `foo.txt`, and so on:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- Preview the result of a move, without making any actual changes:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Interactively move files, with a prompt before every change:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- Verbosely print each action as it's being executed:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`

- Force `cp` (copy) regardless of the name of the function. Same as `zcp`:

`zmv -C '{{(*).log}}' '{{$1.txt}}'`

- Force `ln` (link) regardless of the name of the function. Same as `zln`:

`zmv -L '{{(*).log}}' '{{$1.txt}}'`
