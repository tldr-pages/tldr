# basic regex

> This page describes basic regex syntax.
> More information: <https://linuxize.com/post/regular-expressions-in-grep/>.

- Match 0 or more repetitions of previous character, class or group:

`{{character|class|group}}*`

- Match 1 or more repetitions of previous character, class or group:

`{{character|class|group}}\+`

- Match 0 or 1 repetitions of previous character, class or group:

`{{character|class|group}}\?`

- Match any character from a specific set of characters:

`[{{characters}}]`

- Match one of two specific alternatives:

`{{alternative1}}\|{{alternative2}}`

- Group a specific pattern:

`\({{pattern}}\)`
