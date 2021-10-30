# zmv

> Move or rename files matching a specified extended glob pattern.
> See also `zcp` and `zln`.
> More information: <http://zsh.sourceforge.net/Doc/Release/User-Contributions.html>.

- Move files using a regular expression-like pattern:

`zmv '{{(*).log}}' '{{$1.txt}}'`

- Preview the result of a move, without making any actual changes:

`zmv -n '{{(*).log}}' '{{$1.txt}}'`

- Interactively move files, with a prompt before every change:

`zmv -i '{{(*).log}}' '{{$1.txt}}'`

- Verbosely print each action as it's being executed:

`zmv -v '{{(*).log}}' '{{$1.txt}}'`
