# stdbuf

> Run a command with modified buffering operations for its standard streams.

- Change stdin buffer size to 512 kiB:

`stderr --input={{512K}} {{command}}`

- Change stdout to line-buffering:

`stdbuf --output={{L}} {{command}}`

- Change stderr to unbuffered:

`stdbuf --error={{0}} {{command}}`
