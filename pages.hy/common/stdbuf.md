# stdbuf

> Գործարկեք հրաման՝ փոփոխված բուֆերային օպերացիաներով իր ստանդարտ հոսքերի համար:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html>:.

- Փոխեք `stdin` բուֆերի չափը մինչև 512 ԿԲ:

`stdbuf {{[-i|--input]}} 512K {{command}}`

- Փոխել `stdout` բուֆերը տողով բուֆերացվածի.:

`stdbuf {{[-o|--output]}} L {{command}}`

- Փոխեք `stderr` բուֆերը չբուֆերացվածի.:

`stdbuf {{[-e|--error]}} 0 {{command}}`
