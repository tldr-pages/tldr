# pabcnetcclear

> Preprocess and compile PascalABC.NET source files.
> More information: <http://pascalabc.net>.

- Compile a source file into an executable with the same name:

`pabcnetcclear {{path/to/file.pas}}`

- Compile a source file into an executable with the same name along with or without debug info:

`pabcnetcclear /Debug:{{0|1}} {{path/to/file.pas}}`

- Allow units to be searched in a path while compiling a source file into an executable with the same name:

`pabcnetcclear /SearchDir:{{path/to/dir}} {{path/to/file.pas}}`
