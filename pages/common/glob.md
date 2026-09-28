# glob

> `glob` patterns are patterns used to match and search text.
> Note: `glob` isn't a command, but syntax to be used with other commands or the shell.
> See also: `regex`.
> More information: <https://en.wikipedia.org/wiki/Glob_(programming)>.

- Match zero or more of any characters:

`*`

- Match any single character:

`?`

- Match one character in a set of characters:

`[{{abc}}]`

- Match ranges of characters:

`[{{a-z}}][{{3-9}}]`

- Match anything but the specified character:

`[!{{a}}]`

- Match a single character not within a range:

`[!{{a-z}}]`
