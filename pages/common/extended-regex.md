# extended regex

> This page describes extended regex syntax.
> More information: <https://linuxize.com/post/regular-expressions-in-grep/>.

- Match 0 or more repetitions of previous character, class or group:

`{{a|[abc]]|(abc)}}*`

- Match 1 or more repetitions of previous character, class or group:

`{{a|[abc]]|(abc)}}+`

- Match 0 or 1 repetitions of previous character, class or group:

`{{a|[abc]]|(abc)}}?`

- Match any character from a specific set of characters:

`[{{abc}}]`

- Match any character not from a specific set of characters:

`[^{{abc}}]`

- Match one of two specific alternatives:

`{{abc}}|{{def}}`

- Group a specific pattern:

`({{abc}})`
