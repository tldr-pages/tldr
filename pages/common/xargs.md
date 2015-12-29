# xargs

> Reads from standard input and executes a command.

- Look for a particular import in all .py files from the current directory, recursively

`find {{.}} -name {{\*.py}} | xargs grep {{"import mylib"}}`

- Play all mp3 songs found, including those with spaces in the name

`find {{.}} -name {{\*.mp3}} -print0 | xargs -0 mpg321`

- Print all lines of a file in green color

`cat {{LICENSE.md}} | xargs -d{{"\n"}} -I{{name}} \
printf {{"\e[1;32m%s\e[0m\n"}} {{name}}`
